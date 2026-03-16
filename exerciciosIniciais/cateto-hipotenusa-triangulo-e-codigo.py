import math

catetoO = float(input('Comprimento do cateto oposto: '))
catetoA = float(input('Comprimento do cateto adjacente: '))

Hipotenusa = (catetoA**2 + catetoO**2)**(1/2)
Hipotenusa1 = math.hypot(catetoO, catetoA)

print(f'[Resultado sem importação(nativo)] A hipotenusa vai medir {Hipotenusa:.2f}')
print(f'[Resultado com importação de (math)] A hipotenusa vai medir {Hipotenusa1:.2f}')