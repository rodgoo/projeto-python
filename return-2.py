def fatorial (numero=1):
    f = 1
    for contador in range(numero, 0,-1):
        f *= contador
    return f

print('='*20)
print('FATORIAL DE NÚMEROS + input')
n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')


def fatorial (numero=1):
    f = 1
    for contador in range(numero, 0,-1):
        f *= contador
    return f

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print('='*20)
print('FATORIAL - [5] [4] e [1]')
print(f'Os resultados são: {f1}, {f2}, {f3}')
print('='*20)
