Lprincipal = []  # cria lista principal
Ltemporária = []  # cria lista temporária
Maior = Menor = 0

while True:
    Ltemporária.append(input('Digite seu nome: '))
    Ltemporária.append(float(input('Digite seu peso: ')))

    # Lógica que vai definir Maior e Menor logo no início
    if len(Lprincipal) == 0:
        Maior = Menor = Ltemporária[1]
    else:
        if Ltemporária[1] > Maior:
            Maior = Ltemporária[1]
        if Ltemporária[1] < Menor:
            Menor = Ltemporária[1]

    Lprincipal.append(Ltemporária[:])
    Ltemporária.clear()

    # Validação da resposta
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Deseja continuar? [S/N] ').strip().upper()[0]

        if resposta not in 'SN':
            print('Resposta inválida!')

    if resposta == 'N':
        break

#  Resultados (Fora do While)
print('=' * 40)
print(f'Pessoas cadastradas ao todo: {len(Lprincipal)}')
print('=' * 40)

# Mostrando os Pesados
print(f'O maior peso foi de {Maior} Kg. Peso de: ', end='')
for pessoa in Lprincipal:
    if pessoa[1] == Maior:
        print(f'[{pessoa[0]}] ', end='')
print()  # Pula linha

# Mostrando os Leves
print(f'O menor peso foi de {Menor} Kg. Peso de: ', end='')
for pessoa in Lprincipal:
    if pessoa[1] == Menor:
        print(f'[{pessoa[0]}] ', end='')
print()