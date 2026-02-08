frase = ('EU SOU RODRIGO CARVALHO ')
print('Caractere 0:', frase[0])

# Exibe a frase original
print('EXIBE O TEXTO ORIGINAL:',frase)

# Exibe o caractere 0 até o 16 de frase
print('Estou exibindo do caractere 0 até o caractere 16 de frase:',frase[0:16])

# Exibe o caractere inicial até o 16 de frase
print('Estou exibindo do caractere inicial até o caractere 16 de frase:',frase[:16])

# Exibe do caractere 17 até o caractere final de frase
print('Estou exibindo do caractere 17 até o caractere final de frase:',frase[17:])

# Exibe todos os caracteres, pulando de 2 em 2
print('Estou exibindo toda a frase [::], porém, pulando de 2 em 2:',frase[::2])

#Contará letras maiúsculas na frase
print('Estou exibindo o número de frases que possuem letras maiúsculas',frase.upper().count('O'))

#Alterará de uma palavra padrão (nome) para (Rodrigo) na frase, caso haja
print('Altere para NOME, caso haja:',frase.replace('nome','NOME'))

# Verifica se o valor desejado está no texto digitado
print('Existe Rodrigo em frase?', 'Rodrigo' in frase)

# Procura o valor desejado no texto digitado
print('Qual posição está o texto?', frase.find('sou o Rodrigo'))

# Divide a string em novas indexações independentes
dividido = frase.split()
print('Texto dividido:',dividido)
print('Primeira string/valor do texto dividido:',dividido[0])
print('Me mostre a 4º letra da 2º string:',dividido[2])

lista = [10,20,30,40,50]
print(lista)

# Exibe do caractere 17 até o caractere final de frase
print('Estou exibindo toda a lista [::], porém, pulando de 2 em 2:',lista[::2])