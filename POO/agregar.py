class Carrinho:
    def __init__(self):
        self.produtos = []

    def inserir(self, produto):
        self.produtos.append(produto)

    def listar(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)

    def soma(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return total


class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor


carrinho = Carrinho()
p1 = Produto('Camiseta', 50)
p2 = Produto('Celular', 10000)
p3 = Produto('Caneca', 15)

carrinho.inserir(p1)
carrinho.inserir(p2)
carrinho.inserir(p3)

carrinho.listar()
print(carrinho.soma())