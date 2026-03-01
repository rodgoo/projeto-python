def ficha(jogador='DESCONHECIDO', gol = 0):
    print(f'Jogador {jogador} fez {gol} gol(s)!')

nome = input('Qual o nome jogador? ')
gols = input('Quantos gols fez? ')

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 'NENHUM'

if nome.strip() == '':
    ficha(gol = gols)
else:
    ficha(nome,gols)