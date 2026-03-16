num = int(input('Digite um número inteiro:'))
print('''Escolha uma das bases para conversão
1 - para binario
2 - para octal
3 - para hexadecimal''')

opcao = int(input('Digite uma opcao: '))

if opcao == 1:
    print(f'{bin(num)[2:]} em binario')
    print(f'Seu código em binário: {bin(num)[:2]}')

elif opcao == 2:
    print(f'{oct(num)[2:]} em octal')
    print(f'Seu código em octal: {oct(num)[:2]}')

elif opcao == 3:
    print(f'{hex(num)[2:]} em hexadecimal')
    print(f'Seu código em hexadecimal: {hex(num)[:2]}')

else:
    print('Nenhum das bases reconhecidas, tente novamente (opções válidas: 1,2,3)')