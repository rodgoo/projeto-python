n1 = int(input('Digite o 1º número:'))
n2 = int(input('Digite o 2º número:'))
n3 = int(input('Digite o 3º número:'))

if n1 > n2 and n1 > n3:
    print(f'{n1} é maior que os 3 números disponíveis!')
    maior = n1

elif n2 > n1 and n2 > n3:
    print(f'{n2} é maior que os 3 números disponíveis')
    maior = n2

if n3 > n1 and n3 > n2:
    print(f'{n3} é maior que os 3 números disponíveis')
    maior = n3


if n1 < n2 and n1 < n3:
    print(f'{n1} é menor que os 3 números disponíveis!')
    menor = n1

elif n2 < n1 and n2 < n3:
    print(f'{n2} é menor que os 3 números disponíveis')
    menor = n2

if n3 < n1 and n3 < n2:
    print(f'{n3} é menor que os 3 números disponíveis')
    menor = n3

print(f'O maior número é {maior}')
print(f'O menor núnero é {menor}')