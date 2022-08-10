class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    def inserir(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado))

    def listar(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)


class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado


c1 = Cliente('Luiz', 31)
c1.inserir('São Paulo', 'SP')

c2 = Cliente('Maria', 43)
c2.inserir('Salvador', 'BA')
c2.inserir('Rio de Janeiro', 'RJ')

print(c1.nome)
c1.listar()
print()
print(c2.nome)
c2.listar()
