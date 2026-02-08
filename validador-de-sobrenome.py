sobrenome = input('Digite o seu nome completo: ')

validador = ('rodrigues' in sobrenome.lower())

# Validação feita utilizando if de forma autônoma
if validador == True:
    print('Seu nome possui o sobrenome esperado: Rodrigues!')
else:
    print('Seu nome não possui o sobrenome esperado. Tente novamente com outro nome.')