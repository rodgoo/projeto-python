lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')

print('='*20)

# Estrutura de repetição em loop, verifica cada item partindo de 0
for contador in range(0, len(lanche)):
    print(f'[FOR RANGE]: Lanche: {lanche[contador]} em {contador}º lugar')

print('='*20)

# Tuplas são IMUTÁVEIS
# lanche[1] = 'Refigerante' == 'tuple' object does not support item assignment

# Estrutura de repetição direto no elemento
for comida in lanche:
    print(f'[FOR IN]: Eu vou comer {comida}')

print('='*20)

# Me trás o DADO e a POSIÇÃO
for pos, comida in enumerate(lanche):
    print(f'[USANDO POSIÇÃO]: Eu vou comer {comida} na posição {pos}')

print('='*20)

print('DE FORMA ORDENADA (ALFABÉTICA): ',end='')
print(sorted((lanche)))

print('='*20)

a = (1,2,3,4)
b = (5,6,7,8)
c = a+b # Concatena tuplas, 4 valores em A + 4 valores em B | C = 8 valores
print('Concatenando tuplas, os itens dispostos em A+B resultam em quantidade: ',end='')
print(len(c))

print('='*20)

a = (1,2,3,4)
b = (4,6,2,8)
c = b+a
print('O números de vezes que o valor 4 aparece: ',end='')
print(c.count(4)) #Conta vezes que o valor 4 aparece dentro das variáveis dispostas

print('='*20)

a = (1,2,3,4,5,6,7,8)
b = (4,6,2,8)
c = a+b
print('Posição do código em que os elementos estão dispostos: ',end='')
print(c.index(6)) #Revela a posição no qual o elemento 4 se encontra = 0,1,2,3,4,[5] = 6 está na 5º posição

print('='*20)

a = (2,4,6)
b = (8,10,12)
c = b+a
print('Posição do código específica, limitando o início da condição em que os elementos estão dispostos: ',end='')
print(c.index(4, 2)) #Revela a posição no qual o elemento 4 se encontra, começando do elemento 2
print(c)

print('='*20)