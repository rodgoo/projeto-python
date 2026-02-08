sobrenome = input('Digite o seu nome completo: ')

validador = ('Rodrigues' in sobrenome)

if validador == True:
    print('Seu nome possui o sobrenome Rodrigues!')
else:
    print('Seu nome não possui o sobrenome Rodrigues. Tente novamente com outro nome.')