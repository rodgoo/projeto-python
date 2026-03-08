from rich import print
from rich.panel import Panel

class Produto:

    def __init__(self, nomeProduto='Desconhecido', preço='Desconhecido'): #Constructor

    # ÁREA PARA ATRIBUTOS DE INSTÂNCIA
        self.nomeProduto = nomeProduto
        self.preço = preço

    # ÁREA DE MÉTODOS DE INSTÂNCIA
    def etiqueta(self):
        conteudo = self.nomeProduto
        conteudo += f'{'-'*30}'
        preçoProduto = f'R$: {self.preço:,.2f}'
        conteudo += f' {preçoProduto}'
        etiqueta = Panel(conteudo, title='Produto')
        print(etiqueta)

print('-'*30)
p1 = Produto('iPhone 17 Pro ', 8000)
p2 = Produto('Macbook Pro ', 16500)

p1.etiqueta()
p2.etiqueta()