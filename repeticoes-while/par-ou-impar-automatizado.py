import random

vitorias = 0

while True:

    jogador = int(input('Digite um número: '))
    computador = random.randint(1, 10)

    soma = jogador + computador

    print(f'Você: {jogador} | Computador: {computador} | Soma: {soma}')

    # Verifica se o jogador é par ou ímpar automaticamente
    if jogador % 2 == 0:
        jogador_tipo = 'PAR'
    else:
        jogador_tipo = 'ÍMPAR'

    # Verifica resultado da soma
    if soma % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'ÍMPAR'

    print(f'Você é {jogador_tipo}')
    print(f'O resultado foi {resultado}')

    if jogador_tipo == resultado:
        print('Você venceu!')
        vitorias += 1
    else:
        print('Você perdeu!')
        print(f'Você venceu {vitorias} vezes.')

        jogar_novamente = input('Quer jogar novamente? [S/N] ').strip().upper()
        print('-' * 30)


        if jogar_novamente == 'S':
            vitorias = 0
            continue
        elif jogar_novamente != 'N':
            print('Essa não é uma opção valida!')
            break
        else:
            break

print('Fim do jogo.')
