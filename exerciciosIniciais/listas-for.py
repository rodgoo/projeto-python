valores = [] # Cria uma lista vazia pra ir adicionando valores um a um
valores.append(5)
valores.append(7)
valores.append(3)

for c, v in enumerate(valores): #Faz uma validação para cada POSIÇÃO e VALOR
    print(f'Na posição {c}, o valor foi: {v}')
print('Final da lista.')