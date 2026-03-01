from funcoes_pacote import numeros

num = int(input('Digite um valor: '))
fat = numeros.fatorial(num)


print(f'O fatorial de {num} é {fat}!')
print('='*20)
print(f'O dobro de {num} é {numeros.dobro(num)}')
print(f'O triplo de {num} é {numeros.triplo(num)}')