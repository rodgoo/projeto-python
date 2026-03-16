import time
import random

print('Bem vindo ao jogo de JOKENPO!')

print('''
Suas opções:
0 - Pedra
1 - Papel
2 - Tesoura
''')

jogadorA = int(input('Qual sua jogada?'))
time.sleep(0.5)
print('JO')
time.sleep(0.8)
print('KEN')
time.sleep(1)
print('PO!')

itens = ('PEDRA', 'PAPEL', 'TESOURA')
computadorA = random.randint(0,2)
computador = itens[computadorA]
jogador = itens[jogadorA]

if computadorA == 0: #PEDRA
    if jogadorA == 0: #PEDRA
        print(f'Houve EMPATE, o jogador escolheu {jogador}, assim como eu :| ')

    elif jogadorA == 1: #papel
        print(f'Jogador VENCEU. Jogador escolheu {jogador}, computador escolheu {computador} :/ ')

    elif jogadorA == 2: #TESOURA
        print(f'Jogador PERDEU. Jogador escolheu {jogador}, computador escolheu {computador}, vitória do computador :) ')


elif computadorA == 1: #PAPEL
    if jogadorA == 1: #PAPEL
        print(f'Houve EMPATE, o jogador escolheu {jogador}, assim como eu :| ')

    if jogadorA == 2: #TESOURA
        print(f'Jogador VENCEU. Jogador escolheu {jogador}, computador escolheu {computador} :/ ')

    if jogadorA == 0: #PEDRA
        print(f'Jogador PERDEU. Jogador escolheu {jogador}, computador escolheu {computador}, vitória do computador :) ')

elif computadorA == 2: #TESOURA
    if jogadorA == 2: #TESOURA
        print(f'Houve EMPATE, o jogador escolheu {jogador}, assim como eu :| ')

    if jogadorA == 1: #PEDRA
        print(f'Jogador VENCEU. Jogador escolheu {jogador}, computador escolheu {computador} :/ ')

    if jogadorA == 1: #TESOURA
        print(f'Jogador PERDEU. Jogador escolheu {jogador}, computador escolheu {computador}, vitória do computador :) ')

print('='*30)
print(f'Jogada do Computador: {computador}')
print(f'Jogada do Computador (valor): {computadorA}')