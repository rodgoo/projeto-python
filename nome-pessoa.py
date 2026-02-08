nome = input('Digite o seu nome completo:')

maisc = nome.upper()
print('Letras se tornaram maiúsculas:',maisc)

mnsc = nome.lower()
print('Letras se tornaram minúsculas:',mnsc)

letrasPrimeiroNome = nome.split()[0]
quantidadeLetrasPrimeiroNome = len(letrasPrimeiroNome)
print('Número de letras no primeiro nome:',quantidadeLetrasPrimeiroNome)

letras = len(nome.replace(" ", ""))
print('Número de letras completas:',letras)

