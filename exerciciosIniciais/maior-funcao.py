import time

def maior(*num):
    contador = maior = 0
    print('Valores estão sendo analisados')
    print('-'*30)

    for n in num:
        print(f'{n} ', end='', flush=True)
        time.sleep(.5)

        if contador == 0:
            maior = n
        else:
            if n > maior:
                maior = n
        contador += 1
    print(f'| Valores informados: {contador} ')
    print('-'*30)
    print(f'Maior valor: {maior} ')
    print('-'*30)

#Programa Principal
maior(2,9,4,5,7,1)
maior(8,4,0)
maior(6,9)