pergunta = input('Digite um sexo (M ou F): ').strip().upper()[0]

while pergunta not in 'MF':
    pergunta = input('Valor incorreto. Tente novamente. (M ou F): ').strip().upper()[0]
print(f'Sexo {pergunta} foi registrado com sucesso!')