import datetime # Importação de biblioteca remota

idade = int(input('Olá, me fale seu ano de nascimento?'))
anoNascimento = datetime.datetime.today().year - idade # Procura pela idade - o ano atual do computador
rest = anoNascimento - 18
dataPlanejada =  18 + idade

if anoNascimento < 18:
    print(f'Você ainda não completou 18 anos, ainda possui {anoNascimento} anos')
    print(f'Seu alistamento será daqui á {rest} ano(s), em {dataPlanejada}')

elif anoNascimento == 18:
    print(f'Parabéns, você completou {anoNascimento} anos recentemente, é hora de se alistar!')

else:
    print(f'Você passou do tempo de se alistar!')
    print(f'Era pra ter se alistado há {rest} anos, em {dataPlanejada}')
