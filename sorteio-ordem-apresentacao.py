import random

aluno1 = input('Primeiro aluno:')
aluno2 = input('Segundo aluno:')
aluno3 = input('Terceiro aluno:')
aluno4 = input('Quarto aluno:')

lista = [aluno1, aluno2, aluno3, aluno4]
sorteio = random.shuffle(lista)

#Resultado usando biblioteca random
print(f'A ordem de apresentação será: {lista}')

#Resultado usando (for) (nativo) feita manualmente por Rodrigo :)
print('A ordem de apresentação será:')
for lista in lista:
    print(lista)