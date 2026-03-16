def titulo(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)

# Este é o Programa Principal
titulo('     CURSO EM VIDEO      ')
titulo('     APRENDA PYTHON      ')
titulo('     RODRIGO CARVALHO      ')

print('Soma com funções:')
def soma(a, b):
    s = a + b
    print(s)

soma(8,9)
soma(4,4)
soma(5,4)

print('='*40)
print('Contador de Variáveis:')
# Lê a variável contador e joga dentro de num
def contador(*num):
    tamanhho = len(num)
    print(f'Recebi os valores {num} e ao todo são {tamanhho} números')

contador(2,1,7)
contador(8,3)
contador(1,6,2,5,7)
