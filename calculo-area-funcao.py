def area(l, c):
    a = l * c
    print(f'Área do terreno {l} x {c} = {a}mª')

print('='*30)
l = float(input('Qual a largura em metros: '))
c = float(input('Qual a altura em metros: '))
print('='*30)

area(l, c)