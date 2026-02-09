salario = float(input('Qual o salário do funcionário?'))

if salario <= 1250:
    aumento = salario * 0.15
    novo = salario + (salario * 15 / 100) # Salário maior de 1250 + 10%

else:
    aumento = salario * 0.10
    novo = salario + (salario * 10 / 100) # Salário menor de 1250 + 15%

print(f'Para salários com o valor R$:{salario}, houve um aumento de {aumento}%, resultando em um novo salário de R$:{novo}')
