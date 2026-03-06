# -------- DECLARAÇÃO DA CLASSE --------
class MinhaClasse:
    """
    Essa classe cria usuários com nome e idade.
    - variável = MinhaClasse(nome, idade)
    - caso nenhum valor seja dado em nome = DESCONHECIDO
    - caso nenhum valor seja dado em idade = NÃO INFORMADO
    """
    def __init__(self, nome = 'DESCONHECIDO', idade = "NÃO INFORMADO"): #Método construtor

        # --------------- ÁREA DE ATRIBUTOS DE INSTÂNCIA ---------------
        self.nome = nome
        self.idade = idade

        # --------------- ÁREA DE MÉTODOS DE INSTÂNCIA ---------------
    def aniversario(self):
        self.idade += 1

    def __str__(self): # Dunder Method
        return(f'O usuário {self.nome} tem {self.idade} anos')

    def __getstate__(self):
        return f'Estado: nome = {self.nome}; Idade = {self.idade}'

# -------- DECLARAÇÃO DOS OBJETOS --------
print('='*30)
objeto0 = MinhaClasse("Rodrigo" ,16) #print(0)
objeto0.aniversario()


objeto1 = MinhaClasse("Pedro", 17) #print(1)
objeto1.aniversario()

print(objeto0.__dict__)
print(objeto0.__getstate__())

print('='*30)

objeto2 = MinhaClasse() #print(2)
# Repare que não foram definidos valores para a variável, forçando a mostrar valores padrões

print(objeto0.__doc__) #Dunder atrribute = (declaração de documentação, caso haja)

print(objeto0)
print(objeto1)
print(objeto2)
print(objeto2.__getstate__())

print('='*30)


# objeto (Nome do objeto)
# MinhaClasse (nome da classe)
# () (Chamada de instanciação -> Instanciando um objeto / Criando um objeto)
# Chamada de Instanciação gera o Método Construtor