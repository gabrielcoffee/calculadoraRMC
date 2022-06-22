import utils
import numpy as np

def inicio():
    lin = int(input('Número de linhas da matriz: '))
    col = int(input('Número de colunas da matriz: '))
    matriz = gerar_matriz(lin, col)

    utils.green_print('\nMatriz criada:')
    printar_matriz(matriz)

    while True:
        print()
        opcao = utils.escolher_opcoes('Determinante (2x2 ou 3x3)',
                                      'Multiplicação',
                                      'Matriz transposta')
        if opcao == '1':
            utils.blue_print('Resultado: ' + str(determinante(matriz)))
        elif opcao == '2':
            multiplicar(matriz)
        elif opcao == '3':
            transposta(matriz)
        elif opcao == '':
            break


def determinante(matriz):
    lin = len(matriz)
    col = len(matriz[0])

    if lin != col:
        utils.red_print('Matriz não é quadrada...')
        return None

    ordem = lin

    if ordem == 1:
        return matriz[0][0]
    elif ordem == 2:
        return (matriz[0][0] * matriz[1][1]) - (matriz[0][1] * matriz[1][0])
    elif ordem == 3:
        det = 0

        # regra de sarrus
        sarrus = matriz
        for l in range(lin):
            sarrus[l].append(matriz[l][0])
            sarrus[l].append(matriz[l][1])

        # somas e subtrações
        for i in range(ordem):
            det += sarrus[0][i] * sarrus[1][i+1] * sarrus[2][i+2]
        for i in range(2, 5):
            det -= sarrus[0][i] * sarrus[1][i-1] * sarrus[2][i-2]

        return det

def multiplicar(matriz):
    col1 = len(matriz[0])
    lin2 = int(input('Número de linhas da segunda matriz: '))
    col2 = int(input('Número de colunas da segunda matriz: '))

    if col1 != lin2:
        utils.red_print('Multiplicação não é possivel...')
    else:
        utils.green_print('A multiplicação é possivel!\n')

        matriz2 = gerar_matriz(lin2, col2)
        A = np.array(matriz)
        B = np.array(matriz2)

        # multiplica as matrizes
        result = np.matmul(A, B)

        utils.blue_print('MATRIZ A')
        printar_matriz(A)
        utils.blue_print('\nMATRIZ B')
        printar_matriz(B)
        utils.green_print('\nRESULTADO DA MULTIPLICAÇÃO:')
        printar_matriz(result)

def transposta(matriz):
    lin = len(matriz)
    col = len(matriz[0])
    transp = []

    # transpõe matriz
    for c in range(col):
        linha = []
        for l in range(lin):
            linha.append(matriz[l][c])
        transp.append(linha)

    printar_matriz(transp)

def printar_matriz(matriz):
    lin = len(matriz)
    col = len(matriz[0])

    for l in range(lin):
        linha = ''
        for n in range(col):
            linha += '[' + str(matriz[l][n]) + ']'
        print(linha)

def gerar_matriz(linhas, colunas):
    matriz = []

    for l in range(linhas):
        linha = []
        for c in range(colunas):
            valor = int(input('Valor do elemento [' + str(l + 1) + '][' + str(c + 1) + '] da matriz: '))
            linha.append(valor)
        matriz.append(linha)

    return matriz