from menu.lib.interface import *

# Verifica se o arquivo EXISTE
def arquivoExiste(arquivo):
    try:
        a = open(arquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

# Cria o arquivo, caso não exista
def criarArquivo(arquivo):
    try:
        a = open(arquivo, 'wt+')
        a.close()
    except:
        print('Houve um erro na execução do arquivo!')
    else:
        print(f'Arquivo {a} foi criado com sucesso!')

# Lê o arquivo e retorna a leitura dos dados no código
def lerArquivo(arquivo):
    try:
        a = open(arquivo, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabecalho('Pessoas cadastradas')
        print(a.read())