ficha = []

while True:
    nome = input('Digite um nome: ')
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    media = (nota1 + nota2) / 2

    ficha.append([nome, [nota1, nota2], media])
    resposta = input('Quer continuar? [S/N] ').upper()

    if resposta == 'N':
        break
    if resposta not in 'SN':
        print('Resposta invalida!')
    print('='*30)

print('='*30)
print(f'{'Número':<8} {'Nome':<14} {'Média':>8} ')
print('='*30)

for indice, aluno in enumerate(ficha):
    print(f'{indice:<8}{aluno[0]:<14}{aluno[2]:>8.1f}')

while True:
    print('='*30)
    escolha = int(input('Quer ver notas de qual aluno? (999 interrompe):'))
    if escolha == '999':
        print('Finalizando...')
        break
    if escolha <= len(ficha) - 1:
        print(f'Notas de {ficha[escolha][0]} são {ficha[escolha][1]}')
print('Fim da execução!')