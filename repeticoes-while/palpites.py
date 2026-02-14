import random

computador = random.randint(0,10)
print('Adivinhe um número de 0 a 10!')

acertou = False
palpites = 0

while not acertou:
    jogador = int(input('Qual seu palpite? '))
    palpites += 1

    if jogador == computador:
        acertou = True
        print(f'Parabéns, você acertou, pensei em {computador}!')
        print(f'Ao todo foram: {palpites} palpites')

    elif jogador > 10 or jogador < 0: # Se jogador foge dos números informados, exibe mensagem de erro
        print('[ALERTA] Por favor, jogue com os números de 0 a 10! ')

    else:
        if jogador < computador:
            print('[DICA] Faltam mais números')
        elif jogador > computador:
            print('[DICA] Menos números...')

