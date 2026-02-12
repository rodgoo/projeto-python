input('Pressione ENTER, e a soma entre todos os números impares e múltiplos de 1 até 500 serão exibidos')

soma = 0
contador = 0
for c in range(1,501, 2):
    if c % 3 == 0:
        soma += c
        contador += + 1
print(f'Soma dos valores solicitados é {soma}')
print(f'Números solicitados: {contador}')