numero = tuple(int(input(f'Digite o {i+1}º número: ')) for i in range(4))

print(f'1. Quantas vezes apareceu o valor 9?')
print(f'2. Em que posição foi digitado o primeiro valor 3?')
print(f'3. Quais foram os números PARES?')
print('='*30)

print(f'Numeros digitados {numero}')

if 9 in numero:
    print(f'O valor 9 apareceu {numero.count(9)} vez(es)')
else:
    print('O valor 9 não foi digitado')

if 3 in numero:
    print(f'O valor 3 apareceu em {numero.index(3)}ª lugar')
else:
    print('O valor 3 não foi digitado')

print(f'Os valores PARES digitados foram: ', end='')

for n in numero:
    if n % 2 == 0:
        print(n, end=', ')