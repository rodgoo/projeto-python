Lista = list()

while True:
    numero = int(input('Digite um valor: '))

    if numero not in Lista: #Se o número ainda não estiver na lista, ADICIONA o valor
        Lista.append(numero)
        print(f'Valor {numero} adicionado com sucesso!')
    else: # Se número estiver na lista, O VALOR É DUPLICADO e não executa o incremento de valores
        print('Valor duplicado! ')


    resposta = input('Deseja continuar? [S/N] ').upper()

    if resposta in 'N':
        break

print('='*50)

Lista.sort()
print(f'Foram digitados {len(Lista)} valores: {Lista}')

