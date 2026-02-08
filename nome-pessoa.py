nome = input('Digite o seu nome completo:').strip()

print('Letras se tornaram maiúsculas:',format(nome.upper()))

print('Letras se tornaram minúsculas:',format(nome.lower()))

letrasPrimeiroNome = nome.split()[0]
quantidadeLetrasPrimeiroNome = len(letrasPrimeiroNome)
print('Número de letras no primeiro nome:',quantidadeLetrasPrimeiroNome)

letras = len(nome.replace(" ", ""))
print(f'Seu primeiro nome é {letrasPrimeiroNome} e o número de letras completas:',letras)