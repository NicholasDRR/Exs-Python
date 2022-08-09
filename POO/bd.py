class basedados:
    def __init__(self):
        self.dados = {}

    def inserir(self, id, nome):
        if 'clientes' not in self.dados:
            self.dados['clientes'] = {id: nome}
        else:
            self.dados['clientes'].update({id: nome})

    def listar(self):
        for id, nome in self.dados['clientes'].items():
            print(f'{id}: {nome}')

    def deletar(self, id):
        del self.dados['clientes'][id]


base = basedados()
base.inserir(1, 'Valéria')
base.inserir(2, 'Luiz')
base.deletar(2)
base.listar()

