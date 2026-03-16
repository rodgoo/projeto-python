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

numero = leiaInt('Digite um valor inteiro: ')
print(f'O valor digitado foi {numero}')
print('-'*20)


def leiaFloat(msg):
    while True:
        try:
            flutuante = float(input(msg))
        except (ValueError, TypeError):
            print('ERRO: digite um número real!')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida!')
            break
        else:
            return flutuante

numeroF = leiaFloat('Digite um valor real: ')
print(f'O valor digitado foi {numeroF}')

resultado = numero/numeroF

print('-'*20)

print(f'Resultado final: {resultado}')