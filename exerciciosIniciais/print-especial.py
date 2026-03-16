def write(msg):
    size = len(msg) + 4

    print('~' * size)
    print(f'  {msg}')
    print('~' * size)

#Programa Principal
write('Rodrigo Carvalho')
write('Curso de Python')
write('Gustavo Guanabara')
write('CeV')