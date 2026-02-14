resposta = 'S'
media = soma = quantidade = media = maior = menor = 0

while resposta == 'S':
    n = int(input('Digite um valor: '))
    soma += n
    quantidade += 1
    if quantidade == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

    resposta = input('Quer continuar? (S/N) ').upper().strip()[0]
media = soma / quantidade
print('Você não quis continuar. Fim do programa. Obrigado por participar!')
print(f'Números digitados: {quantidade} | Média: {media}')
print(f'Maior número digitado: {maior} | Menor número digitado: {menor}')
print('='*30)

