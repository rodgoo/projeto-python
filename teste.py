def contador(i, f, p):
    # Tratando passo zero para evitar loop infinito

    print(f'Contagem de {i} até {f} de {p} em {p}:')

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ')
            cont += p
        print('FIM!')  # Fora do while
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ')
            cont -= p
        print('FIM!')  # Fora do while


# Testes
contador(1, 10, 1)
contador(10, 0, 2)