num = int(input('Digite um número:'))
for c in range(0, num):
    print('contagem no número:',c)
print('fim da execução.')
print('='*15)

inicio = int(input('inicio:'))
fim = int(input('fim:'))
passo = int(input('passo:'))

for d in range(inicio, fim+1, passo):
    print(d)
print('fim')
print('='*15)

s=0
for e in range(0, 5):
    n = int(input('Digite um valor a ser somado:'))
    s += n
print(f'O somatório dos valores acima foi de {s}')
print('fim da execução.')
print('='*15)