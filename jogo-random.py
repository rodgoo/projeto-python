from random import randint
from time import sleep

computador = randint(1, 10) # Computador randomiza seu número escolhido
print('=-==-=' * 10)

print('Vou escolher um número entre 1 e 10, me diga qual foi...') # Computador pergunta usuário

print('=-==-=' * 10)

jogador = int(input('Qual núnero eu escolhi?')) # Usuário dá o seu palpite
print('Computador está a pensar...') # Faz um time para o jogador esperar o computador
sleep(2)

if jogador == computador: # Validação condicional (se o valor dito pelo jogador for o mesmo pensado por computador = Vitória
    print(f'Parabéns! Você me ganhou. Também pensei em {jogador}')
else: # Se o valor dito não for o mesmo que o computador pensou = Perda
    print(f'Errou, não pensei em {jogador}, pensei em {computador}')

