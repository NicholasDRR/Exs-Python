from abc import ABC, abstractmethod
from POO.DESAFIO.Pessoas import pessoa

cliente = pessoa.Clientes


class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        self.mostrar()

    def mostrar(self):
        print(f'''Agência: {self.agencia}
Conta: {self.conta}
Saldo: {self.saldo}''')

    @abstractmethod
    def sacar(self, valor):
        pass


class Poupanca(Conta):
    def sacar(self, valor):
        if self.saldo < valor:
            print('Saldo insuficiente.')
            return
        self.saldo -= valor
        self.mostrar()


class Corrente(Conta):
    def sacar(self, valor, limite=100):
        if (self.saldo + limite) < valor:
            print('Saldo insuficiente')
            return
        self.saldo -= valor
        self.mostrar()


class Banco:
    def __init__(self):
        self.agencias = [1111, 2222, 3333]
        self.clientes = []
        self.contas = []

    def inserir_clientes(self, cliente):
        self.clientes.append(cliente)

    def inserir_contas(self, conta):
        self.contas.append(conta)

    def autenticar(self, cliente):
        if cliente not in self.clientes:
            return False
        if cliente.conta not in self.contas:
            return False
        if cliente.conta.agencia not in self.agencias:
            return False
        return True