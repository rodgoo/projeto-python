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
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]} -{dado[1]:>3} anos')
    finally:
        a.close()

# Função que cadastra os usuários no arquivo de texto
def cadastrar(arquivo, nome='Desconhecido', idade=0):
    try:
        a = open(arquivo, 'at')
    except:
        print('Erro na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Erro ao escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado com sucesso!')
            a.close()