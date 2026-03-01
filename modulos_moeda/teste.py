from moeda import aumentar, diminuir, dobro, metade

preco_Input = float(input('Digite o preço: '))
print(f'O AUMENTO de 10% em ${preco_Input} é ${aumentar(preco_Input, 10)}')
print(f'A DIMINUIÇÃO de 10% em ${preco_Input} é ${diminuir(preco_Input, 10)}')
print(f'O DOBRO de ${preco_Input} é ${dobro(preco_Input)}')
print(f'A METADE de ${preco_Input} é ${metade(preco_Input)}')
