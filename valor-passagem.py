distancia = float(input('Qual a distância da viagem?'))
print(f'Você começará uma viagem de {distancia}km')

if distancia <= 200:
    preço1 = distancia * 0.50
    print(f'Sua viagem está abaixo da distância de {distancia}km. O preço da sua passagem será de {preço1:.2f} pela distância de {distancia}km.')

else:
    preço2 = distancia * 0.45
    print(f'O preço da sua passagem será de {preço2:.2f} pela distância de {distancia}km.')

