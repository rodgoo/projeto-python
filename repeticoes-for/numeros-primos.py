num = int(input('Digite um número inteiro: '))
contagem = 0
nPrimos = 0


for c in range(1, num + 1):
    if num % c == 0:
        contagem += 1
        print(f'Número Primo: {c}')
    else:
        nPrimos += 1

print(f'O número {num} foi divisível {contagem} vez(es)')

if contagem == 2:
    print('Este número é PRIMO')
else:
    print('Este número NÃO É PRIMO')

print('='*40)




