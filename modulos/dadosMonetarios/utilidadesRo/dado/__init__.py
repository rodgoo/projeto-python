def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = input(msg).replace(',', '.').strip()

        if entrada == '':
            print(f'\033[0;31mEspaços ou campos vazios são valores inválidos!\033[m')
        elif entrada.isalpha() or entrada.strip() == '':
            print(f'\033[0;31mERRO: "{entrada}" é um preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)