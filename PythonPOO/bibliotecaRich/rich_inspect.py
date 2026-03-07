from rich import print
from rich import inspect

class ContaBancaria:
    """
    Cria uma conta bancária com: INSERT e DELETE
    - permitindo depósitos
    - permitindo saques
    """

    def __init__(self, id, nome, saldo=0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f'Conta: {self.id} criada com sucesso. Saldo atual U$:{self.saldo}')
        print('='*30)

    def __str__(self):
        return f'Conta: {self.id}; Nome: {self.titular}; Saldo: U$:{self.saldo:,.2f}'

    def deposito(self, valor): # Faz a configuração de depósito
        self.saldo += valor
        print(f'Depósito de U$:{valor:,.2f} realizado. ')

    def saque(self, valor): # Faz a configuração de saque
        if valor > self.saldo:
            print('-' * 30)
            print(f'Saque de U$:{valor:,.2f} não autorizado.')
            print(f'Saldo insuficiente')
            print('-' * 30)
        else:
            self.saldo -= valor
            print(f'Saque de U$:{valor:,.2f} realizado. ')
            print('='*30)

conta1 = ContaBancaria(122, "Rodrigo", 4600)

conta1.deposito(300)
conta1.saque(300)
inspect(conta1) # Usando inspect
