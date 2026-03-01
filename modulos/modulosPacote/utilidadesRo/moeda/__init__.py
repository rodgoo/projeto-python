def aumentar(preco = 0, taxa = 0, formato=False):
    resultado = preco + (preco * taxa/100)
    return resultado if formato is False else moeda(resultado)

def diminuir(preco = 0, taxa = 0, formato=False):
    resultado = preco - (preco * taxa/100)
    return resultado if formato is False else moeda(resultado)

def dobro(preco = 0, formato=False):
    resultado = preco * 2
    return resultado if formato is False else moeda(resultado)

def metade(preco = 0, formato=False):
    resultado = preco / 2
    return resultado if formato is False else moeda(resultado)

# Deixei padronizado em dólar propositalmente
def moeda (preco = 0, moeda = 'U$'):
    return f'{moeda}{preco:>.2f}'

def resumo(preco = 0, taxaA =10, taxaR = 5):
    print('='*30)
    print('RESUMO DO VALOR'.center(30))
    print('='*30)
    print(f'Preço Informado: {moeda(preco)}')
    print(f'Dobro do preço: {dobro(preco, True)}')
    print(f'Metade: {metade(preco, True)}')
    print('-'*30)
    print(f'{taxaA}% de Aumento: {aumentar(preco, taxaA, True)}')
    print(f'{taxaR}% de Redução: {diminuir(preco, taxaR, True)}')
    print('='*30)
