import time
from time import sleep

print('Olá! Informe dois valores abaixo e escolha uma das opções a seguir')

primeiroValor = int(input('Primeiro valor: '))
segundoValor = int(input('Segundo valor: '))
escolhaOpcao = 0
while escolhaOpcao != 5:
    print('''
    1 - somar
    2 - multiplicar
    3 - maior
    4 - novos dados
    5 - sair do programa
    ''')
    escolhaOpcao = int(input('Escolha uma das opções acima: '))

    if escolhaOpcao == 1:
        soma = primeiroValor + segundoValor
        print(f'A soma realizada entre {primeiroValor} + {segundoValor} = {soma}')

    elif escolhaOpcao == 2:
        multiplicar = primeiroValor * segundoValor
        print(f'A multiplicação realizada entre {primeiroValor} x {segundoValor} = {multiplicar}')

    elif escolhaOpcao == 3:
        if primeiroValor > segundoValor:
            maior = primeiroValor
        elif segundoValor > primeiroValor:
            maior = segundoValor
        print(f'O maior valor entre {primeiroValor} e {segundoValor} = {maior}')

    elif escolhaOpcao == 4:
        print('Escolha os números novamente')
        primeiroValor = int(input('Primeiro valor: '))
        segundoValor = int(input('Segundo valor: '))

    elif escolhaOpcao == 5:
        print('[LOGOFF] O programa está sendo finalizado...')
        sleep(1.2)
        print('[LOGOFF] Quase lá...')
        sleep(1)
        print('[LOGOFF] Até logo!')
        sleep(.8)

    else:
        print('[AVISO] Opção invalida, tente novamente')

    print('=' * 40)
    sleep(2)
print('[Sistema] FIM DO PROGRAMA')
