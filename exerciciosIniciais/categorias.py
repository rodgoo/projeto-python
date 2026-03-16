import datetime

enunciado = int(input('Ano de nascimento: '))
idade =  datetime.datetime.now().year - enunciado


media = print(f'A idade do atleta é de: {idade} anos')

if idade <= 9:
    print('O atleta se encontra na classificação: MIRIM (até 9 anos)')

elif idade > 9 and idade <= 14:
    print('O atleta se encontra na classificação: INFANTIL (até 14 anos)')

elif idade <= 19:
    print('O atleta se encontra na classificação: JUNIOR (até 19 anos)')

elif idade <= 25:
    print('O atleta se encontra na classificação: SENIOR (até 25 anos)')

else:
    print('O atleta se encontra na classificação: MASTER (acima de 25 anos)')