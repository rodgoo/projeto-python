import math
msg = int(input('Por favor, insira um número para calcular o fatorial: '))
contador = msg
fatorial = 1

print(f'Será calculado o fatorial de {msg}!')

while contador > 0:
    print(f'{contador}', end='') # mostra o número que será contado até 1
    print(' -> ' if contador > 1 else ' = ', end='')
    fatorial *= contador
    contador -= 1

print(fatorial)