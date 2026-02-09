Seg1 = float(input('Primeiro segmento: '))
Seg2 = float(input('Segundo segmento: '))
Seg3 = float(input('Terceiro segmento: '))

if Seg1 < Seg2 + Seg3 and Seg2 < Seg1 + Seg3 and Seg3 < Seg1 + Seg2:
    print('Os segmentos inputados podem formar um triângulo!')
else:
    print('Infelizmente, as condições para formar um triângulo não consegue ser atendida. Tente novamente com outro número!')