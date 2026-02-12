import datetime
hoje = datetime.date.today().year

totalMaior = 0
totalMenor = 0

for pessoas in range(1, 8):
    nascimento = int(input(f'Em que ano a {pessoas}ª nasceu?'))
    idade = hoje - nascimento

    if idade >= 18:
        totalMaior += 1

    else:
        totalMenor += 1

print(f'{totalMaior} pessoas tem mais de 18 anos')
print(f'{totalMenor} pessoas são menores de idade')