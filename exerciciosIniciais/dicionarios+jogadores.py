time = list()
jogador = dict ()
partidas = list()

while True:
    jogador['Nome'] = input('Nome: ').upper()
    partidasJogador = int(input(f'Quntas partidas {jogador["Nome"]} jogou? '))
    partidas.clear()

    for c in range (0, partidasJogador):
        partidas.append(int(input(f'Quantos gols na partida {c+1}? ')))

    jogador['Gols'] = partidas[:]
    jogador['Total'] = sum(partidas)
    time.append(jogador.copy())

    while True:
        opcao = input('Quer continuar?').upper()[0]
        if opcao in 'SN':
            break
        print('='*30)
        print('ERRO! Opção inválida! Responda com S ou N.')
        print('='*30)
    if opcao == 'N':
        break

print('='*30)

print('COD', end='')
for i in jogador.keys():
    print(f' {str(i):<8}', end='')
print()

print('='*30)

for k, v in enumerate(time):
    print(f'{k:>4}', end='')

    for d in v.values():
        print(f' {str(d):<10}', end='')
    print()
print('='*30)

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para)'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Jogar maior do que o código de {busca}')
    else:
        print(f'Levantamento de {time[busca]['Nome']}: ')

        for i, g in enumerate(time[busca]['Gols']):
            print(f'No jogo {i+1} fez {g} gols.')
    print('='*30)
print('FIM DO PROGRAMA')