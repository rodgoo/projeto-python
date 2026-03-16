numero = []
maior = 0
menor = 0

for i in range(0, 5):
    numero.append(int(input(f'Digite um valor para a posição {i}: ')))
    if  i == 0:
        maior = menor = numero[i]
    else:
        if numero[i] > maior:
            maior = numero[i]
        if numero[i] < menor:
            menor = numero[i]

print(f'Foram digitados os valores {numero}')
print('='*50)

print(f'O maior valor digitado foi: {maior} | Posição: ', end='')
for indice, valor in enumerate(numero):
    if valor == maior:
        print(f'{indice}')


print(f'O menor valor digitado foi: {menor} | Posição: ', end='')
for indice, valor in enumerate(numero):
    if valor == menor:
        print(f'{indice}')

