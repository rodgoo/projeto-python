import random

p1 = input('Digite o nome do aluno 1:')
p2 = input('Digite o nome do aluno 2:')
p3 = input('Digite o nome do aluno 3:')
p4 = input('Digite o nome do aluno 4:')

#Sorteador feito por Rodrigo (manualmente)
sorteador = random.randint(1,4)
print('O aluno escolhido foi:')
if sorteador == 1:
    print(p1)
if sorteador == 2:
    print(p2)
if sorteador == 3:
    print(p3)
if sorteador == 4:
    print(p4)

#Sorteador feito utilizando a biblioteca (random)
lista = [p1,p2,p3, p4]
escolher = random.choice(lista)
print(f'O aluno escolhido foi: {escolher}')