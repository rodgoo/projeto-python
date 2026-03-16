estado = dict()
brasil = list()

for contador in range(0, 2):
    estado['uf'] = input('Unidade Federativa: ')
    estado['sigla'] = input('Sigla: ')

    brasil.append(estado.copy())

for um_estado in brasil:
    for chave in um_estado.values():
        print(f'O estado é: {chave}')

