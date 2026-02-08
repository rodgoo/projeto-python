entrada = input('Digite seu nome completo: ').strip()
nome = entrada.split()
ultimoNome = nome[len(nome)-1]

print('Seu primeiro nome é ',nome[0])
print('Seu último nome é ', ultimoNome)
