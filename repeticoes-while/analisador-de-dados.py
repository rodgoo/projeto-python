pessoas18 = totalH = mulher20 = 0
while True:
    idade = int(input('Qual a sua idade? '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Qual o seu sexo? [M/F] ').strip().upper()[0]

    if idade >= 18:
        pessoas18 += 1
    if sexo == 'M':
        totalH += 1
    if sexo == 'F' and idade < 20:
        mulher20 += 1

    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Deseja continuar? [S/N] ').strip().upper()[0]

    if resposta == 'N':
        print('=' * 20)
        break
print('Fim do programa.')
print('=' * 20)

print(f'Total de PESSOAS com 18 anos ou mais: {pessoas18}')
print(f'Total de HOMENS cadastrados: {totalH}')
print(f'Total de MULHERES com menos de 20 anos: {mulher20}')