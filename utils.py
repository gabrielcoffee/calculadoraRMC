def escolher_opcoes(*opcoes):
    while True:
        for i in range(len(opcoes)):
            print(Style.CYAN + '[' + str(i+1) + '] ' + Style.RESET + opcoes[i])

        print(Style.RED + '[Enter]' + Style.RESET + ' Sair')

        opcao = input(Style.RED + '--> ' + Style.RESET)

        if opcao == '':
            break
        elif int(opcao) < 1 or int(opcao) > len(opcoes):
            red_print('Opção inválida, tente novamente')
        else:
            green_print(opcoes[int(opcao)-1] + '\n')
            break

    return opcao

def red_print(string):
    print(Style.RED + string + Style.RESET)

def green_print(string):
    print(Style.GREEN + string + Style.RESET)

def blue_print(string):
    print(Style.CYAN + string + Style.RESET)

def printar_grafico():
    # da pra usar esses imports
    # mas ainda n sei como só vi por cima

    # import matplotlib.pyplot
    # import numpy as np
    pass

class Style:
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    CYAN = '\033[36m'
    RESET = '\033[0m'