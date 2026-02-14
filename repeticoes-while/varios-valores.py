num = contador = soma = 0
num = int(input(f'Digite um número. (999 faz a execução parar): '))

while num != 999:
    soma += num
    contador += 1
    num = int(input(f'Digite um número. (999 faz a execução parar): '))

print(f'Você digitou {contador} números. | A soma entre esses números foi {soma}')
print('Teste finalizado, você digitou 999.')
