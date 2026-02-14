print('{:=^40}'.format(' Gerador de PA '))

PrimeiroValor = int(input('Digite o primeiro termo: ')) #Pede o termo ao usuário
razao = int(input('Razão: ')) #Pede a razão

termo = PrimeiroValor #Define termo
contador = 1

while contador <= 10: #Enquanto contador não chegar ao décimo número, execute as condições a seguir
    print(f'{termo} -> ', end='')
    termo += razao
    contador += 1
print('Fim da execução')