time = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio' ,
        'Cruzeiro','Flamengo','Vasco','Chapecoense',
        'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia',
        'São Paulo', 'Fluminense', 'Sport Recife',
        'EC Vitória', 'Curitiba', 'Avaí', 'Ponte Preta', 'Atlético-GO' )

print(f'1. Lista de times: {time [0:5]}')
print(f'2. Últimos 4 colocados: {time [-4:]}')
print(f'3. Times em ordem alfabetica: {sorted(time)}')
print(f'4. Time Chapecoense na {time.index("Chapecoense")+1}ª posição | Começando do 0, posição: {time.index("Chapecoense")}')