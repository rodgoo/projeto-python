listagem = ('Lápis', 1.50,
            'Borracha', 2.00,
            'Caderno', 17.50,
            'Estojo', 27,
            'Transferidor', 2.00,
            'Compasso', 9.00,
            'Mochila', 15.00,
            'Canetas', 9.00,
            'Livro', 37.50
            )

print('='*40)
print(f'{'MATERIAIS ESCOLARES':^40}')
print('='*40)

for posicao in range(0, len(listagem)):
    if posicao % 2 == 0:
        print(f'{listagem[posicao]:-<30}', end=' ')
    else:
        print(f'U$:{listagem[posicao]:>7.2f}')