def aumentar(preco = 0, taxa = 0):
    resultado = preco + (preco * taxa/100)
    return resultado

def diminuir(preco = 0, taxa = 0):
    resultado = preco - (preco * taxa/100)
    return resultado

def dobro(preco = 0):
    resultado = preco * 2
    return resultado

def metade(preco = 0):
    resultado = preco / 2
    return resultado

# Deixei padronizado em dólar propositalmente
def moeda (preco = 0, moeda = 'U$'):
    return f'{moeda}{preco:>.2f}'