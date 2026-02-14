r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = input('Quer continuar? (S/N) ').upper()
print('Você não quis continuar. Fim do programa. Obrigado por participar!')
print('='*30)

n=1
par = impar = 0
while n !=0:
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        par+= 1
    else:
        impar +=1
print(f'Números pares:{par}. Número ímpares: {impar}')