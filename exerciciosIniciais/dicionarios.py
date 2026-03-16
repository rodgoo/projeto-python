id = {
    'nome':'Rodrigo',
    'idade':18,
    'sexo':'M'
}

print('='*40)

print(f'Usuário tem:', id['nome'])
print(f'Idade do usuário:', id['idade'])
print(f'Sexo do usuário:', id['sexo'])

print('='*40)

print(f'KEYS mostra (valor0):',id.keys())
print(f'VALUES mostra (resultado_do_valor):',id.values())
print(f'ITEMS mostra (valor0 + resultado):',id.items())

print('='*40)

# Usando for pra mostrar cada valor
for chave, valor in id.items():
    print(f'{chave}: {valor}')

print('='*40)

id['peso'] = 60
print('+ Adicionado [peso] ')

print('='*40)

# Usando for pra mostrar cada valor
for chave, valor in id.items():
    print(f'{chave}: {valor}')

