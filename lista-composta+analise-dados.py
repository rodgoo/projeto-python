Ltemporária = []
Lprincipal = [] # cria lista temporária
Maior = Menor =  0

while True:
    Ltemporária.append(input('Digite seu nome: '))
    Ltemporária.append(input('Digite seu peso: '))

    if len(Lprincipal) == 0:
        Maior = Menor = Ltemporária[1]
    else:
        if Ltemporária[1] > Maior:
            Maior = Ltemporária[1]
        if Ltemporária[1] < Menor:
            Menor = Ltemporária[1]

    Lprincipal.append(Ltemporária[:])
    Ltemporária.clear()

    resposta = input('Deseja continuar?').upper()
    if resposta in 'N':
        print('Vamos acabar com os valores')
        break

print('='*30)
print(f'No total, foram cadastros {Lprincipal} pesoas.')
print(f'Ao todo, foram cadastras {len(Lprincipal)} de pesosas')
print(f'O maior peso foi de {Maior} Kg')

for pessoa in Lprincipal:
    if pessoa == Maior:
        print(f'O valor é zero')

print(f'O menor peso foi de {Menor} Kg')
for pessoa in Lprincipal:
    if pessoa[1] == Menor:
            print([{pessoa[0]}])
print()