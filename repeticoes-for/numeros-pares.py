input('Pressione ENTER, e todos os números pares até 50 serão exibidos')


for pares in range(0,51):
    if pares % 2 == 0:
        print(pares, end=' | ')

print('FIM')