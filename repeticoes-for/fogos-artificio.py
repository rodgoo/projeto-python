import time

print('{:=^40}'.format(' Fogueteria do Ro '))

input('Assim que você pressionar ENTER, a contagem dos fogos começará')
print('='*50)

for c in range(10,0, -1):
    print(f'Contagem de segundos:{c}')
    time.sleep(1)
print('FOGOS EXPLODEM, POW POW!!!')