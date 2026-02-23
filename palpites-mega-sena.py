import random
import time

lista = []
listaJogos = []
totalJogos = 0

quantidadeJogos = int(input('Quantos jogos quer fazer? '))

while totalJogos < quantidadeJogos:
    contador = 0
    while True:
        numero = random.randint(1,60)
        if numero not in lista:
            lista.append(numero)
            contador += 1
        if contador >= 6:
            break

    lista.sort()
    listaJogos.append(lista[:])
    lista.clear()
    totalJogos += 1
print('='*40)
print(f'MOSTRANDO RESULTADOS PARA [{quantidadeJogos}] JOGOS SORTEADOS')
print('='*40)


for numero_jogo, lista_sorteada in enumerate(listaJogos):
    time.sleep(1)
    print(f'Jogo Nº{numero_jogo+1}: {lista_sorteada}')
    time.sleep(1)
print('='*40)
print('BOA SORTE!')
