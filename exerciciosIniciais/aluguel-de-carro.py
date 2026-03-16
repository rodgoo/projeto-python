diasAlugados = int(input('Digite a quantidade de dias no qual você ficou com o carro:'))
km = float(input('Digite a quantidade de km percorridos pelo carro: '))

diaria = diasAlugados * 60
kmPercorrido = km * 0.15

custoTotal = diaria + kmPercorrido

print(f'Com {diasAlugados} diárias, o valor dos dias alugados foi de R$:{diaria}')
print(f'Com {km}km percorridos, o valor de km percorrido foi de R$:{kmPercorrido}')
print(f'Total a pagar: ({diaria} + {kmPercorrido}) = R$:{custoTotal}')
