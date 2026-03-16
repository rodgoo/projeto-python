Lista = [[], []]
Valor = 0

for contador in range(1, 8):
    Valor = int(input(f'Digite o valor {contador}º valor: '))

    # Verifica se o valor é PAR, senão, IMPAR
    if Valor % 2 == 0:
        Lista[0].append(Valor)
        Valor += 1
    else:
        Lista[1].append(Valor)
        Valor += 1
print('='*40)

# Classifica os números em ordem crescente
Lista[0].sort()
Lista[1].sort()

print(f'Todos os valores {Lista}')
print(f'Valores pares: {len(Lista[0])} | {Lista[0]}')
print(f'Valores impares: {len(Lista[1])} | {Lista[1]}')