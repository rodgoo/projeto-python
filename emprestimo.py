valor = float(input('Valor da casa: '))
salario = float(input('Digite seu salario: '))
anos = int(input('Anos de financiamento: '))

prestacao = valor / (anos * 12)
minimo = salario * 30 / 100

print(f'Pra pagar uma casa do valor {valor} em {anos} anos.', end='')
print(f' A prestação será de {prestacao:.2f} reais')

if prestacao <= minimo:
    print('Emprestimo concedido!')
else:
    print('Emprestimo negado')