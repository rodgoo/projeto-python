Lista = list()
Par = list()
Impar = list()

while True:
    Lista.append(int(input('Digite um valor: ')))
    resposta = input('Quer continuar? [S/N] ').upper()

    if resposta in 'N':
        break

for indice, valor in enumerate(Lista):
    if valor % 2 == 0:
        Par.append(valor)
    else:
        Impar.append(valor)

print(f'Lista completa: {Lista} ')
print(f'Lista de pares: {Par}')
print(f'Lista de ímpares: {Impar}')