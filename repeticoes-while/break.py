numero = 0
while numero != 1: #Valida se número é diferente de 1. Se for, leva pra fora do programa.
    numero = int(input('Digite um número: '))
print('Número é 1. Fim do programa')
print('=' * 20)

quebra = 0
while True: #Roda pra sempre, até que receba uma ordem/condição de parada
    numero = int(input('Digite um número: '))
    if numero < 100:
        print('Número abaixo de 100. Jogue mais alto')
    elif numero == 111: # Valida se número é 111.
        break # Se número for 111 encerra a condicional
    elif numero >= 120:
        print('Vai uma dica. Número abaixo de 120 e maior que 100. Nunca disse nada...')
    elif numero <= 119 and numero > 111:
        print('Quase lá... Tá bem perto, mais pra menos...')
    elif numero >= 100 and numero <= 110:
        vaiQuebrar = 111 - numero
        print(f'Faltam alguns números para quebrar a condicão. Dica: Faltam {vaiQuebrar} números.')

print('PARABÉNSSS!! Quebra da condição usando break. Fim do programa!')