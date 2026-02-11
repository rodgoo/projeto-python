peso = float(input('Qual seu peso? (Em Kg): '))
altura = float(input('Qual é sua altura? '))

imc = peso / (altura ** 2)

print(f'O IMC encontrado foi de: {imc:.1f}')

if imc < 18.5:
    print('Você está abaixo do peso')

elif imc >= 18.5 and imc <= 25:
    print('Você está no peso normal')

elif imc >= 25 and imc <= 30:
    print('Você está com sobrepeso')

elif imc >= 30 and imc <= 40:
    print('Você está em estado de obesidade')

elif imc >= 40:
    print('Você está em estado de obesidade mórbida')