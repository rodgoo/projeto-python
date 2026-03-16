import time

def contador(i, f, p):
    if p < 0:
        p = passo * (-1)
    if p == 0:
        p = 1

    print(f'Contagem de {i} até {f} de {p} em {p}')
    time.sleep(1)
    print('='*30)


    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ', flush=True)
            time.sleep(.5)
            cont += p
        print('FIM')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ', flush=True)
            time.sleep(.5)
            cont-= p
        print('FIM')

contador(1,10,1)
contador(10,0,2)
print('Sua vez de personalizar a contagem!')

inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador (inicio, fim, passo)