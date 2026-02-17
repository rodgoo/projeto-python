import random
s = random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)

print('Os valores sorteados foram:', end=' ')

for n in s:
    print(f'{n}', end=' ')

print(f'\nMaior valor sorteado: {max(s)}')
print(f'Menor valor sorteado: {min(s)}')