Lista = list()
Dados = list()
Maiores = Menores = 0

for contador in range(0, 5): # Cria e copia os dados inputados
    Dados.append(input('Digite seu nome: '))
    Dados.append(int(input('Digite sua idade: ')))
    print('='*20)
    Lista.append(Dados[:])
    Dados.clear() # Exclui o dado no final da chamada

for pessoa in Lista: # Valida se as pessoas possuem a idade necessária + Soma cada usuário a sua faixa etária
    if pessoa[1] >= 18:
        print(f'[MAIOR DE IDADE]: {pessoa[0]} tem mais de 18 anos!')
        Maiores += 1
    else:
        print(f'[MENOR DE IDADE]: {pessoa[0]} tem menos de 18 anos!')
        Menores += 1

print(f'No total, houveram {Menores} menores de 18 anos, e {Maiores} maiores de 18 anos.')