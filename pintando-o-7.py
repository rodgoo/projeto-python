largura = float(input('Digite a largura de uma parede: '))
altura = float(input('Digite a altura de uma parede: '))

area = (largura * altura)
pintando= area/2

print(f'A área da parede é de: {area:.2f}m²')
print(f'Será necessário {pintando:.2f} litros de tinta para pintar essa parede de {area:.2f}m²')