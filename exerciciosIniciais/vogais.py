palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'desenvolvedo', 'python',
            'trabalhar', 'programador', 'futuro','mercado')


for i in palavras:
    print(f'\nNa palavra {i.upper()} temos ', end='')

    for letra in i:
        if letra in 'aeiou':
            print(letra.upper(), end=' ')