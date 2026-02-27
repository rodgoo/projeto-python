import random
import time


def sorteador(lista):
    for cont in range(0, 5):
        n = random.randint(1, 10)
        lista.append(n)
        print(f'{n}', end=' ', flush=True)
        time.sleep(.6)
    print('FINAL!!')

def somaPar(lista):
    soma=0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando valores pares de {lista} = valores pares: {soma}')
    print('-'*30)

numeros = list()
sorteador(numeros)
somaPar(numeros)
