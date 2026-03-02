from time import sleep
from menu.lib.interface import *
from menu.lib.arquivo import *

arq = 'arquivo.txt'

if arquivoExiste(arq):
    print('Arquivo encontrado com sucesso!')
else:
    print('Arquivo não encontrado!')
    criarArquivo(arq)


while True:
    resposta = menu(['Listar Pesssoas Cadastradas', 'Cadastrar Pessoas', 'Sair do Sistema'])

    if resposta == 1:
        print('-'*40)
        print('OPÇÃO 01...')
        lerArquivo(arq)
    elif resposta == 2:
        print('-'*40)
        print('NOVO CADASTRO')

        nome = input('Nome: ')
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)

    elif resposta == 3:
        print('-'*40)
        print('Sistema sendo finalizado, até a próxima!')
        break
    else:
        print('Erro! Opção inválida!')
    sleep(2)