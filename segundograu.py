import math
import utils
import matplotlib.pyplot as plt
import numpy as np

def inicio():
    try:
        while True:
            a = float(input('Insira o valor de a: '))
            if a == 0:
                utils.red_print('a deve ser diferente de 0...')
            else:
                break
        b = float(input('Insira o valor de b: '))
        c = float(input('Insira o valor de c: '))

        delta = (b*b) - (4 * a * c)
    except:
        utils.red_print('Algo deu errado, tente novamente...')

    while True:
        print()
        opcao = utils.escolher_opcoes('Calcular raízes',
                                      'Calcular em função de x',
                                      'Calcular vértice',
                                      'Gerar gráfico')
        if opcao == '1':
            calc_raiz(a,b,c, delta)
        elif opcao == '2':
            calc_func_x(a,b,c)
        elif opcao == '3':
            calc_vertice(a,b,c, delta)
        elif opcao == '4':
            gerar_graf(a,b,c)
        elif opcao == '':
            break

def calc_raiz(a,b,c, delta):

    if delta < 0:
        utils.red_print('Não tem raizes reais\n')

        delta = abs(delta)

        x1a = -b / (2 * a)
        x1b = math.sqrt(delta) / (2 * a)

        x2a = -b / (2 * a)
        x2b = -math.sqrt(delta) / (2 * a)

        if x1b < 0:
            utils.blue_print('\nX1 = ' + str(x1a) + str(x1b) + 'i')
        else:
            utils.blue_print('\nX1 = ' + str(x1a) + '+' + str(x1b) + 'i')

        if x2b < 0:
            utils.blue_print('X2 = ' + str(x2a) + str(x2b) + 'i')
        else:
            utils.blue_print('X2 = ' + str(x2a) + '+' + str(x2b) + 'i')
        return
    elif delta == 0:
        print('Duas raízes iguais')
    elif delta > 0:
        print('Duas raízes distintas')

    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)

    utils.blue_print('\nX1 = ' + str(x1))
    utils.blue_print('X2 = ' + str(x2))

def calc_func_x(a,b,c):
    x = float(input('Insira o valor de x: '))

    result = a * (x**2) + b * x + c
    utils.blue_print('f(' + str(x) + ') = ' + str(result))

def calc_vertice(a,b,c, delta):
    if a > 0:
        print('Ponto é mínimo')
    else:
        print('Ponto é máximo')

    xv = -b / (2*a)
    yv = -delta / (4*a)

    utils.blue_print('Xv = ' + str(xv))
    utils.blue_print('Yv = ' + str(yv))

def gerar_graf(a,b,c):
    # pontos de x
    x = np.arange(-2, 2, 0.001)
    # pontos de y
    y = a * (np.exp(x) ** 2) + b * np.exp(x) + c

    plt.plot(x, y)
    plt.grid()
    plt.show()