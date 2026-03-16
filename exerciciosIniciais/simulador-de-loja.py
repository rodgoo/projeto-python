print('{:=^40}'.format(' LOJAS BAIRRODRIGO '))
preco = float(input('Valor total das compras: '))

print('''
Formas de pagamento
1 - à vista em dinheiro/cheque
2 - à vista no cartão 
3 - 2x no cartão
4 - 4x ou mais no cartão ''')

opcao = int(input('Qual a opção de pagamento escolhida? '))

if opcao == 1:
    print('Nessa forma de pagamento (à vista), você ganha 10% de desconto!')
    total = preco - (preco * 10 / 100)
    print(f'Sua compra terá parcelas de R${total:.2f}')
    print(f'O total da compra foi R${preco:.2f}')

elif opcao == 2:
    print('Nessa forma de pagamento (à vista no cartão), você ganha 5% de desconto!')
    total = preco - (preco * 5 / 100)
    print(f'Sua compra terá parcelas de R${total:.2f}')
    print(f'O total da compra foi R${preco:.2f}')

elif opcao == 3:
    total = preco / 2
    print(f'Sua compra terá parcelas de R${total:.2f}')
    print(f'O total da compra foi R${preco:.2f}')

elif opcao == 4:
    parcelas = int(input('Em quantas parcelas? '))
    alertaJuros = print('Nessa opção de pagamento, com 3x ou mais no cartão, é adicionado 20% de juros dentro do valor total')
    juros = preco + (preco * 20 / 100)
    total = juros / parcelas
    print(f'Sua compra terá parcelas de R${total:.2f} COM JUROS')
    print(f'O total da compra foi R${juros:.2f}')

else:
    print('Hmm, forma de pagamento não válida, tente novamente (opções válidas: 1,2,3,4)')
