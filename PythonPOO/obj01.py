# -------- DECLARAÇÃO DA CLASSE --------
class MinhaClasse:
    def __init__(self): #Método construtor

        # --------------- ÁREA DE ATRIBUTOS DE INSTÂNCIA ---------------
        self.nome = ""
        self.idade = 0

        if self.nome == "":
            self.nome = "[DESCONHECIDO]"

    # --------------- ÁREA DE MÉTODOS DE INSTÂNCIA ---------------
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return(f'O usuário {self.nome} tem {self.idade} anos')


# -------- DECLARAÇÃO DOS OBJETOS --------
objeto = MinhaClasse()
objeto.nome = 'Rodrigo'
objeto.idade = 16
objeto.aniversario()

objeto2 = MinhaClasse()
objeto2.nome = 'Pedro'
objeto2.idade = 17
objeto2.aniversario()

objeto3 = MinhaClasse()

print(objeto.mensagem())
print(objeto2.mensagem())
print(objeto3.mensagem())

# obj (Nome do objeto)
# MinhaClasse (nome da classe)
# () (Chamada de instanciação -> Instanciando um objeto / Criando um objeto)
# Chamada de Instanciação gera o Método Construtor