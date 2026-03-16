matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = somaColuna = maior = 0

# Faz a pergunta das linhas até a última
for linha in range(0, 3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f"Digite um valor para [{linha}, {coluna}]: "))
        if matriz[linha][coluna] %2 == 0: soma += matriz[linha][coluna]
        if coluna == 0:
            maior = matriz[1][coluna]
        elif matriz[1][coluna] > maior:
            maior = matriz[1][coluna]

print('='*40)

# Mostra cada linha e coluna como digitado
for linha in range(0,3):
    for coluna in range(0,3):
        #O print abaixo traz espaço de 4 caracteres, centralizando conteúdo
        print(f'[{matriz[linha][coluna]:^4}]', end='')
    print()

for linha in range(0,3):
    somaColuna += matriz[linha][2]
print('='*40)
print(f'Soma dos valores PARES: {soma}')
print(f'Soma dos valores da TERCEIRA coluna é {somaColuna}')
print(f'O maior dos valores da SEGUNDA linha é {maior}')
