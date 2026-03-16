comando = int(input('Digita um número e vou te falar se é par ou ímpar'))
resultado = comando % 2

if  resultado == 0:
    print(f'Resultado de {comando} é {resultado}. Então é Par')
else:
    print(f'Resultado de {comando} é {resultado}. Então é Impar')