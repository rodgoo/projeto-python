from time import sleep
from menu.lib.interface import *

while True:
    resposta = menu(['Listar Pesssoas Cadastradas', 'Cadastrar Pessoas', 'Sair do Sistema'])

    if resposta == 1:
        print('-'*40)
        print('OPÇÃO 01...')
    elif resposta == 2:
        print('-'*40)
        print('OPÇÃO 02')
    elif resposta == 3:
        print('-'*40)
        print('Sistema sendo finalizado, até a próxima!')
        break
    else:
        print('Erro! Opção inválida!')
    sleep(2)