produtos = total = acimade1000 = menor = contador = quantidade = 0 # Item em NÚMERO
barato = ''

while True:
    item = input('Nome do produto: ')  #Item em TEXTO
    preco = float(input('Preço do produto = R$:'))
    quantidade = int(input('Quantidade = '))

    contador += 1
    quantidade = 1 * quantidade
    total += preco * quantidade

    if item != '':
        produtos += 1

    if preco >= 1000:
        acimade1000 += 1

    if contador == 1 or preco < menor:
        menor = preco
        barato = item.upper()

    resposta = ' '
    while resposta not in 'SN':
        print('---'*10)
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()
        print('---' * 10)

    if resposta == 'N':
        print('-' * 30)
        break
print('----- FIM DO PROGRAMA -----')

print(f'Total gasto na compra: R$:{total}')
print(f'Produtos acima de R$:1000: {acimade1000}')
print(f'O produto com menor valor é {barato} e custa R$:{menor} a unidade')