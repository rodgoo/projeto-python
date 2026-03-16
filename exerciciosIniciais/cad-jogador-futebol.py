jogador = dict ()
partidas = list()

jogador['Nome'] = input('Nome: ')
partidasJogador = int(input(f'Quntas partidas {jogador["Nome"]} jogou? '))

for c in range (0, partidasJogador):
    partidas.append(int(input(f'Quantos gols na partida {c}? ')))

jogador['Gols'] = partidas[:]
jogador['Total'] = sum(partidas)

print('='*30)
print(jogador)
print('='*30)

for k, v in jogador.items():
    print(f'{k}: {v}')
print('='*30)

print(f'O jogador {jogador['Nome']} jogou {len(jogador['Gols'])} partidas.')

for i, v in enumerate(jogador['Gols']):
    print(f' Na {i+1}ª partida, fez {v} gols.')
print(f'Total de {jogador["Total"]} gols.')