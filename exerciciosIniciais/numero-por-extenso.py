contagem = ('zero', 'um', 'dois', 'três', 'quatro',
            'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
            'onze', 'doze', 'treze', 'catorze', 'quinze',
            'desesseis', 'desessete', 'dezoito', 'dezenove', 'vinte')

while True:
    numero = int(input('Digite um número inteiro (entre 0 a 20):'))

    # Verifica se o número está entre 0 e 20
    if 0 <= numero <= 20:
        print(f'Número digitado {contagem[numero]}')
    else: # Se o número estiver fora desse intervalo
        print('Número fora da contagem, tente novamente!')
        print('=' * 40)

    # Valida com o usuário se ele quer continuar
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

        if resposta not in 'SN': # Se a resposta for diferente de S ou N, exibe o alerta
            print('Resposta invalida! Responda com S ou N')
        print('=' * 40)

    # Encerra o programa caso não queira continuar.
    if resposta == 'N':
        print('Fim do programa. Até logo!')
        break