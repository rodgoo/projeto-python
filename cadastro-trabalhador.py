import datetime

pessoa = {}
pessoa['Nome'] = input('Digite o seu nome: ')

nascimento = int(input('Digite o seu ano de nascimento: '))
pessoa['Idade'] = datetime.datetime.now().year - nascimento
pessoa['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))


while pessoa['CTPS'] != 0:
    if pessoa['CTPS'] != 0:
            pessoa['Contratação'] = int(input('Ano de contratação: '))
            if pessoa['Contratação'] < nascimento:
                print('=' * 30)
                print('Ano de contratação inválido')
                break
            pessoa['Salário'] = float(input('Salário: '))
            pessoa['Aposentadoria'] = pessoa['Idade'] + ((pessoa['Contratação'] + 35) - datetime.datetime.now().year)
            break
    else:
        break


if pessoa['CTPS'] != 0:
    print('=' * 30)
    if pessoa['Contratação'] > nascimento:
        for key, value in pessoa.items():
            print(f' -{key}: {value}')
