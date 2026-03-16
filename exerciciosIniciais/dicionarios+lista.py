grupo = list()
usuario = dict()
soma = media = 0

while True:
    usuario.clear()
    usuario['Nome'] = input('Nome: ')
    while True:
        usuario['Sexo'] = input('Sexo [M/F]: ').upper()[0]
        if usuario['Sexo'] in 'MF':
            break
        print('[ERRO] Digite M ou F.')
    usuario['Idade'] = int(input('Idade: '))

    soma += usuario['Idade']
    grupo.append(usuario.copy())

    while True:
        print('='*30)
        opcao = input('Deseja continuar? [S/N] ').upper()[0]
        print('='*30)
        if opcao in 'SN':
            break
        print('='*30)
        print('[ERRO] Digite S ou N.')
        print('='*30)
    if opcao == 'N':
        break
print(f'a.) Total de {len(grupo)} pessoas cadastradas.')
media = soma / len(grupo)
print(f'b.) A MÉDIA de idade é {media:5.2f} anos.')

print(f'c.) As MULHERES cadastradas foram: ', end='')
for p in grupo:
    if p['Sexo'] in 'F':
        print(p['Nome'], end= ',')
print()

print(f'd. Lista de MÉDIA acima da média')
print('-'*30)
for p in grupo:
    if p['Idade'] >= media:
        for k, v in p.items():
            print(f' {k}: {v}', end= ' ')
    print()
    print()
print('-'*30)