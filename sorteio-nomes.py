import random

p1 = input('Digite o nome da pessoa 1:')
p2 = input('Digite o nome da pessoa 2:')
p3 = input('Digite o nome da pessoa 3:')

sorteador = random.randint(1,3)
print('Número sorteado:',sorteador)
if sorteador == 1:
    print(p1)
if sorteador == 2:
    print(p2)
if sorteador == 3:
    print(p3)
else: print('Valor não disponível em tabela')

