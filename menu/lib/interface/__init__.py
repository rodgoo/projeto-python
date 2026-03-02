def leiaInt(msg):
    while True:
        try:
            valor = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO: digite um número inteiro!')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida!')
            break
        else:
            return valor

def linha(tamanho = 40):
    return '-' * tamanho

def cabecalho(txt):
    print(linha())
    print(txt.center(40))
    print(linha())

def menu(lista):
    cabecalho('MENU PRINCIPAL - by: ro')
    c=1
    for item in lista:
        print(f'{c}. {item}')
        c+=1
    print(linha())
    opcao = leiaInt('Opção: ')
    return opcao