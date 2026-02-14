print('{:=^40}'.format(' Sequência de Fibonacci '))
termos = int(input('Digite um número e mostrarei os termos desejados para a sequência de Fibonacci: '))

t1, t2 = 0, 1
print(f'{t1} -> {t2}', end='')

contador =  3

while contador <= termos:
    t3 = t1 + t2
    print(f' -> {t3}', end='')
    contador += 1
    t1 = t2
    t2 = t3
    t3 = t1 + t2


print(' -> Fim do programa.')

