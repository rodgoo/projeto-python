def teste():
    x = 8
    print(f'Na função teste, n vale: {n}')
    print(f'Na função teste, x vale: {x}')

#Programa Principal
n = 2
print(f'No programa principal, n vale {n}')
print('='*40)
teste()

def funcao():
    n1 = 4
    print('='*20)
    print(f'N1 EM ESCOPO vale {n1}')

n1 = 2
funcao()
print(f'N1 FORA DO ESCOPO vale {n1}')