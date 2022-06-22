import math
import sys
import matrizes
import segundograu
import exponenciais
import utils

def iniciar():
    while True:
        utils.blue_print('\n========= MENU =========')
        opcao = utils.escolher_opcoes('Função segundo grau',
                                      'Funções exponenciais',
                                      'Matrizes')
        if opcao == '1':
            segundograu.inicio()
        elif opcao == '2':
            exponenciais.inicio()
        elif opcao == '3':
            matrizes.inicio()
        elif opcao == '':
            sys.exit('Programa finalizado')

if __name__ == '__main__':
    iniciar()