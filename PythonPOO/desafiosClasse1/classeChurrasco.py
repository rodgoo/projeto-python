from rich import print
from rich.panel import Panel
class Churrasco:

    # ATRIBUTOS DE CLASSE

    consumo_padrao: float = 0.400 # Cada pessoa
    kg_preço: float = 82.40 # Valor do kg de carne

    def __init__(self, titulo, quantidade):
        self.titulo = titulo
        self.convidados = quantidade

    def __str__(self):
        return f'Evento: {self.titulo} com {self.convidados}'

    def calcular_carne(self) -> float:
        return self.convidados * Churrasco.consumo_padrao

    def calcular_total(self) -> float:
        return self.calcular_carne() * Churrasco.kg_preço

    def calcular_individual(self) -> float:
        return self.calcular_total() / self.convidados

    def analise(self):
        conteudo = f'Analisando: [green]{self.titulo}[/] '
        conteudo += f'\nConvidados: {self.convidados}'
        conteudo += f'\nCada participante comerá {Churrasco.consumo_padrao}kg '
        conteudo += f'\nSendo que o kg custa R$:{Churrasco.kg_preço}'

        conteudo += f'\n[blue][RECOMENDAÇÃO][/] Recomendo comprar {self.calcular_carne():.2f}kg de carne'
        conteudo +=f'\n[green][CUSTO TOTAL][/] Custo total R$:{self.calcular_total():,.2f}'
        conteudo +=f'\n[green][CUSTO INDIVÍDUO][/] Custo por participante R$:{self.calcular_individual():,.2f}'
        painel = Panel(conteudo, title=self.titulo.upper())
        print(painel)

churrasco1 = Churrasco('Churras dos amigos', 15)
churrasco1.analise()

churrasco2 = Churrasco('Confra de fim de ano', 100)
churrasco2.analise()