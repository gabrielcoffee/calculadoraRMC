import utils
import matplotlib.pyplot as plt
import numpy as np

def inicio():
    utils.blue_print('f(x) = a * b^x')

    # pega o valor de a
    while True:
        a = float(input('Insira o valor de a: '))
        b = float(input('Insira o valor de b: '))

        if a != 0 and b > 0 and b != 1:
            break
        else:
            utils.red_print('"a" deve ser diferente de 0.')
            utils.red_print('"b" deve ser maior que 0 e diferente de 1.')
            utils.red_print('Tente novamente')

    while True:
        print()
        opcao = utils.escolher_opcoes('Crescente ou decrescente',
                                      'Calcular em função de x',
                                      'Gerar gráfico')
        if opcao == '1':
            cres(a,b)
        elif opcao == '2':
            func_em_x(a,b)
        elif opcao == '3':
            gerar_graf(a,b)
        elif opcao == '':
            break

def cres(a, b):
    if b > 1:
        print('Função é CRESCENTE')
    else:
        print('Função é DECRESCENTE')

def func_em_x(a, b, x):
    x = float(input('Insira o valor de x: '))
    result = a * (b ** x)
    print('f(' + str(x) + ') = ' + str(a) + ' . ' + str(b) + '^' + str(x))
    utils.blue_print('f(' + str(x) + ') = ' + str(result))

def gerar_graf(a, b):
    # pontos de x
    x = np.arange(-2, 2, 0.001)
    # pontos de y
    y = a * b ** np.exp(x)

    plt.plot(x, y)
    plt.grid()
    plt.show()