import random
import time
import operator

jogo = {
    'player1': random.randint(1, 10),
    'player2': random.randint(1, 10),
    'player3': random.randint(1, 10),
    'player4': random.randint(1, 10)
    }

ranking = dict()
print('='*30)
print('Valores sorteados foram:')

for key, value in jogo.items():
    print(f'{key}: conseguiu o valor {value} no dado')
    time.sleep(.5)

print('='*30)

# MOSTRA O RANKING DOS JOGOS DE MAIOR PARA MENOR
print('Ranking dos jogos: MAIOR para MENOR')
ranking = sorted(jogo.items(), key = operator.itemgetter(1), reverse = True)

print(ranking)
print('='*30)

# MOSTRA A POSIÇÃO DO PLAYER POR PONTUAÇÃO
for itens, valor in enumerate(ranking):
    print(f'{itens+1}º lugar: {valor[0]} com {valor[1]} pontos')
    time.sleep(.5)