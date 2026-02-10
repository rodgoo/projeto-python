import datetime # Importação de biblioteca remota

idade = int(input('Olá, me fale seu ano de nascimento?'))
anoNascimento = datetime.datetime.now().year - idade # Procura pela idade - o ano atual do computador

if anoNascimento < 18:
    print(f'Você ainda não completou 18 anos, ainda possui {anoNascimento} anos e ainda vai se alistar')

elif anoNascimento == 18:
    print(f'Parabéns, você completou {anoNascimento} anos recentemente, é hora de se alistar!')

else:
    print(f'Você passou do tempo de se alistar!')
