import moeda

preco_Input = float(input('Digite o preço: '))
print(f'A METADE de {moeda.moeda(preco_Input)} é {moeda.moeda(moeda.metade(preco_Input))}')
print(f'O DOBRO de {moeda.moeda(preco_Input)} é {moeda.moeda(moeda.dobro(preco_Input))}')
print(f'O AUMENTO de 10% em {moeda.moeda(preco_Input)} é {moeda.moeda(moeda.aumentar(preco_Input, 10))}')
print(f'A REDUÇÃO de 10% em {moeda.moeda(preco_Input)} é {moeda.moeda(moeda.diminuir(preco_Input, 10))}')
