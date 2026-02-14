print('{:=^40}'.format(' Gerador de SUPER PA '))

PrimeiroValor = int(input('Digite o primeiro termo: ')) #Pede o termo ao usuário
razao = int(input('Razão: ')) #Pede a razão

termo = PrimeiroValor #Define termo
contador = 1
mais = 10
total = 0

while mais !=0:
    total += mais
    while contador <= total: #Enquanto contador não chegar ao décimo número, execute as condições a seguir
        print(f'{termo} -> ', end='')
        termo += razao
        contador += 1
    print('Pausa no programa')
    mais = int(input('Quantos mais termos você quer mostrar? '))
print('[SISTEMA] Fim do programa')
print(f'[SISTEMA] A progressão foi finalizada com: {PrimeiroValor} termo(s)')