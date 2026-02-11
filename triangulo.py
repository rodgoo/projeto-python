seg1 = int(input('Digite o primeiro segmento: '))
seg2 = int(input('Digite o segundo segmento: '))
seg3 = int(input('Digite o terceiro segmento: '))

if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print('Os segmentos dados acima podem formar um triângulo!')

    if seg1 == seg2 == seg3:
        print('Triângulo do tipo: equilátero')

    elif seg1 != seg2 != seg3 != seg1:
        print('Triângulo do tipo: escaleno')

    else:
        print('Triângulo do tipo: isósceles')

else:
    print('Os segmentos dados acima não podem formar um triângulo!')
