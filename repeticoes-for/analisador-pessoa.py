somaIdade= 0
mediaIdade = 0
maiorHomem = 0
maisVelho = ''
totalMulher20 = 0

for pessoa in range(1, 5):
    print(f'=== {pessoa}ª ID ===')
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo (M/F): ').strip().upper()
    somaIdade += idade

    if sexo != 'M' and sexo != 'F': # Quebra a condição se Sexo for Diferente de Masculino ou Feminino
        print('Sexo invalido, por favor, tente apenas com os valores definidos: M ou F')
        break

    if pessoa == 1:
        maiorHomem = idade
        maisVelho = nome
    if sexo in 'M' and idade > maiorHomem:
        maiorHomem = idade
        maisVelho = nome
    if sexo in 'F' and idade < 20:
        totalMulher20 += 1

mediaIdade = somaIdade / 4
print(f'Média de idade do grupo é de: {mediaIdade} anos')
print(f'O homem mais velho tem {maiorHomem} anos e se chama: {maisVelho}')
print(f'{totalMulher20} mulher(es) com menos de 20 anos')
