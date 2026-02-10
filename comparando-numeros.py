n1 = int(input('Digite o 1º número:'))
n2 = int(input('Digite o 2º número:'))

if n1 > n2 and n2 < n1:
    print(f'{n1} é maior que os 2 números disponíveis!')
    maior = n1
    menor = n2

elif n2 > n1 and n1 < n2:
    print(f'{n2} é maior que os 2 números disponíveis')
    maior = n2
    menor = n1

elif n1 < n2 and n1 < n2:
    print(f'{n1} é menor que os 2 números disponíveis!')
    menor = n1
    maior = n2

elif n2 < n1 and n1 > n2:
    print(f'{n2} é menor que os 2 números disponíveis')
    menor = n2
    maior = n1

if n1 == n2:
    print(f'Aqui não existe número maior, ambos os valores são iguais')
    igual = n1

if n1 > n2 or n2 > n1 and n1 < n2 or n1 < n2 and n1 < n2 or n2 < n1 and n1 > n2:
    print(f'O maior número é {maior}')
    print(f'O menor núnero é {menor}')
else:
    print(f'Os números iguais são {igual} e {igual}')