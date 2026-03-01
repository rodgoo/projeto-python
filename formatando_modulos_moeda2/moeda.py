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