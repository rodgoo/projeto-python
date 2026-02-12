print('{:=^40}'.format(' PROGRESSÃO ARITMETICA '))

primeiro = int(input('Primeiro valor: '))
razao = int(input('Razão:'))
dec = primeiro + (10-1) * razao

for p in range(primeiro, dec + razao, razao):
    print(f'{p}', end=' -> ')
print('FIM DA LÓGICA.')

print('{:=^40}'.format(''))
