import time

while True:
    numero = int(input('Digite um valor para ver a tabuada: '))
    if numero < 0:
        break

    print(f'Saquei! Mostrando a tabuada do valor {numero}')
    time.sleep(1)
    print('=' * 30)
    time.sleep(1)
    for c in range(1, 11):
        print(f'{numero} x {c} = {numero*c}')
    print ('='*30)
print('Tabuada não funcionará para numeros negativos, programa encerrado. Tente novamente com números positivos ')
