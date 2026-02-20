Lista = []

while True:
    valor = int(input('Digite um valor: '))
    Lista.append(valor)

    resposta = input('Deseja continuar? [S/N] ').upper()

    if resposta in 'N':
        break

print('='*50)

print(f'Foram digitados {len(Lista)} elementos')

Lista.sort(reverse=True)
print(f'Os valores em ordem descrescente: {Lista}')

if 5 in Lista:
    print(f'O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado!')