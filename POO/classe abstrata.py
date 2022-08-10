from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self._agencia = agencia
        self._saldo = saldo
        self._conta = conta

    @property
    def agencia(self):
        return self._agencia

    @property
    def saldo(self):
        return self._saldo

    @property
    def conta(self):
        return self._conta

    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Saldo precisa ser numérico')

        self._saldo = valor

    def depositar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Valor do depósito precisa ser numérico')
        self._saldo += valor
        self.detalhes()

    def detalhes(self):
        print(f'Agência {self.agencia}', end=' ')
        print(f'Conta {self.conta}', end=' ')
        print(f'Saldo {self.saldo}')

    @abstractmethod
    def sacar(self, valor):
        pass


#######################################################################
class Poupanca(Conta):
    def sacar(self, valor):
        if self._saldo < valor:
            print('Saldo insuficiente')
            return
        self._saldo -= valor
        self.detalhes()


#######################################################################
class Corrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=100):
        super().__init__(agencia, conta, saldo)
        self._limite = limite

    @property
    def limite(self):
        return self._limite

    def sacar(self, valor):
        if (self._saldo + self.limite) < valor:
            print('Saldo insuficiente')
            return
        self._saldo -= valor
        self.detalhes()


#######################################################################
cp = Poupanca(1111, 2222, 23)
print('################################################')
cp.depositar(10)
cp.sacar(21)
cp.sacar(12)
cp.sacar(21)
print('################################################')
cc = Corrente(agencia=1111, conta=3333, saldo=0, limite=500)
cc.depositar(100)
cc.sacar(250)
cc.sacar(400)
cc.depositar(1000)
print('################################################')

