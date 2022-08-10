# Associação - Usa
# Agregação - Tem
# Composição - É dono
# Herança - É

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclasse} está falando...')


class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nomeclasse} está estudando...')


class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeclasse} está comprando...')

    def falar(self):
        print(f'Estou em cliente')


class ClienteVip(Cliente):
    def __init__(self, nome, idade, sobrenome):
        super().__init__(nome, idade)
        self.sobrenome = sobrenome

    def falar(self):
        Pessoa.falar(self)
        Cliente.falar(self)
        print(f'{self.nome} {self.sobrenome} está falando')

p1 = Pessoa('Geraldo', 12)
c1 = Cliente('Luiz', 67)
cv = ClienteVip('Luiz', 47, 'Almeida')
a1 = Aluno('Pedro', 24)

print()
cv.falar()
# c1.comprar()
# a1.estudar()
# p1.falar()
