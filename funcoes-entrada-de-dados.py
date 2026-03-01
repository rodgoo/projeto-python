def Inteiro(msg):
    ok = False
    valor=0
    while True:
        numero = input(msg)
        if numero.isnumeric():
            valor = int(numero)
            ok = True
        else:
            print('ERRO! Apenas números inteiros são validos.')
            print(f'Valor digitado: {numero}')
            print('=' *20)
        if ok:
            break
    return valor

numero = Inteiro('Digite um número: ')
print(f'O número digitado foi {numero}')
print('='*20)
print('Fim do programa.')