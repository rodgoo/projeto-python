import time

def ajuda(com):
    help(com)



comando=''

while True:
    print('-'*30)
    comando= input('Digite um comando/biblioteca (fim para): ').lower()
    print('-'*30)
    if comando == 'fim':
        break
    else:
        print('[Máquina]: Estou pensando...')
        time.sleep(2)
        ajuda(comando)
#Programa Principal

print('FIM do programa')
print('-'*30)