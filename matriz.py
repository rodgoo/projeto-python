matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Faz a pergunta das linhas até a última
for linha in range(0, 3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f"Digite um valor para [{linha}, {coluna}]: "))

print('='*40)

# Mostra cada linha e coluna como digitado
for linha in range(0,3):
    for coluna in range(0,3):
        #O print abaixo traz espaço de 4 caracteres, centralizando conteúdo
        print(f'[{matriz[linha][coluna]:^4}]', end='')
    print()
