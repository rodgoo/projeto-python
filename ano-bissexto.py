import datetime #Importa uma biblioteca remota

anoAtual = int(input('Qual o ano deseja analisar? (Digite 0 para o ano atual): '))
if anoAtual == 0:
    anoAtual = datetime.date.today().year #Checa por meio da biblioteca datetime o ano local da máquina

if anoAtual % 4 == 0 and anoAtual % 100 !=0 or anoAtual % 400 == 0: #Fórmula condicional completa para verificar se o ano é ou não bissexto
    print(f'O ano {anoAtual} é bissexto!')
else:
    print(f'O ano de {anoAtual} não é uma ano bissexto!')