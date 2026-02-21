Lprincipal = []  # cria lista principal
Ltemporária = []  # cria lista temporária
Maior = Menor = 0

while True:
    Ltemporária.append(input('Digite seu nome: '))
    Ltemporária.append(float(input('Digite seu peso: ')))

    if len(Lprincipal) == 0:
        Maior = Menor = Ltemporária[1]
    else:
        if Ltemporária[1] > Maior:
            Maior = Ltemporária[1]
        if Ltemporária[1] < Menor:
            Menor = Ltemporária[1]

    Lprincipal.append(Ltemporária[:])
    Ltemporária.clear()

    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Deseja continuar?').upper()[0]

        if resposta not in 'SN':
            print('Resposta invalida!')

    if resposta == 'N':
        break

print('=' * 40)
print(f'Pessoas cadastradas ao todo: {len(Lprincipal)}')
print('=' * 40)
print(f'O maior peso foi de {Maior} Kg -- ', end='')

for pessoa in Lprincipal:
    if pessoa[1] == Maior:
        print(f'Pessoas: {pessoa[0]}')

print(f'O menor peso foi de {Menor} Kg -- ', end='')

for pessoa in Lprincipal:
    if pessoa[1] == Menor:
        print(f'Pessoas: {pessoa[0]}')
print()