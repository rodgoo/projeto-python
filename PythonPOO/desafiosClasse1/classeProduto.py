class Produto:

    def __init__(self, nomeProduto='Desconhecido', preço='Desconhecido'): #Constructor

    # ÁREA PARA ATRIBUTOS DE INSTÂNCIA
        self.nomeProduto = nomeProduto
        self.preço = preço

    # ÁREA DE MÉTODOS DE INSTÂNCIA
    def comando(self):
        return(f'Produto: {self.nomeProduto} | Valor: R$:{self.preço:,.2f}')

print('-'*30)
p1 = Produto('iPhone 17 Pro', 8000)
p2 = Produto('Macbook Pro', 16500)

print(p1.comando())
print(p2.comando())
print('-'*30)