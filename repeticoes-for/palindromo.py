frase = input('Digite uma frase para verifiar se ela é um palindromo: ').strip().upper()
palavras = frase.split()
juntar = ''.join(palavras)
inverter = ''

for letra in range(len(juntar)-1, -1, -1):
    inverter += juntar[letra]

if inverter == juntar:
    print(f'Palíndromo! {inverter}')

else:
    print('A frase digitada NÃO é um palíndromo!')

print('='*40)
print(f'FRASE JUNTA: {inverter}')
print(f'FRASE SEPARADA: {frase}')