import moeda

preco_Input = float(input('Digite o preço: '))
print(f'A METADE de {moeda.moeda(preco_Input)} é {moeda.metade(preco_Input,True)}')
print(f'O DOBRO de {moeda.moeda(preco_Input)} é {moeda.dobro(preco_Input,True)}')
print(f'O AUMENTO de 10% em {moeda.moeda(preco_Input)} é {moeda.aumentar(preco_Input,10,True)}')
print(f'A REDUÇÃO de 13% em {moeda.moeda(preco_Input)} é {moeda.diminuir(preco_Input,13,True)}')
