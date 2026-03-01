def fatorial(numero, show=False):
    """
    -> Calcula o fatorial de um numero
    :param numero: O número que será inputado em numero_Input logo abaixo
    :param show: Mostrar ou não a conta, inicialmente com false (por padrão)
    :return: Exibe o valor do fatorial de um numero
    """

    f = 1
    for contador in range(numero, 0, -1):
        if show:
            print(contador, end='')
            if contador > 1:
                print(f' * ', end='')
            else:
                print(f' = ', end='')
        f *= contador
    return f

#Programa Principal
numero_Input = int(input('Digite um número para exibir o fatorial: '))
print(fatorial(numero_Input,show=True))
