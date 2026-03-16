Lista = list()
for n in range(0,5):
    valor = int(input('Digite um valor: '))

    if n ==0 or valor > Lista[-1]:
        Lista.append(valor)
        print('Valor foi adicionado ao final da lista! (Por ser o maior valor)')
    else:
        pos = 0
        while pos < len(Lista):
            if valor <= Lista[pos]:
                Lista.insert(pos, valor)
                print(f'Valor foi adicionado na posição: {pos}')
                break
            pos += 1

print(f'Valores digitados em ordem: {Lista}')