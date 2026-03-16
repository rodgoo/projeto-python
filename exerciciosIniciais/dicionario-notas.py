aluno = {}
aluno['Nome'] = (input('Nome: '))
aluno['Média'] = float(input(f'Média de {aluno['Nome']}:'))

if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif 5 <= aluno['Média'] < 7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'

print('='*30)

for chave, valor in aluno.items():
    print(f'{chave}: {valor}')

print('='*30)

print(f'Código completo:', aluno)