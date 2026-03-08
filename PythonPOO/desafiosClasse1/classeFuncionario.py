from rich import print

class Funcionario:

    empresa = 'Curso em Video'

    def __init__(self, nome='Desconhecido', setor='Desconhecido', cargo='Desconhecido'): #Constructor
    # ÁREA PARA ATRIBUTOS DE INSTÂNCIA
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    # ÁREA DE MÉTODOS DE INSTÂNCIA
    def comando(self):
        return(f' Olá! Sou [blue]{self.nome}[/] e sou [purple]{self.setor}[/] do setor de [green]{self.cargo}[/] da empresa [yellow]{self.empresa}[/]!')

print('-'*30)
funcionario1 = Funcionario('Rodrigo', 'Analista', 'Sistemas de Informação')
funcionario2 = Funcionario('Vitor', 'Funcionário', 'T.I')
print('-'*30)

print(funcionario1.comando())
print(funcionario2.comando())