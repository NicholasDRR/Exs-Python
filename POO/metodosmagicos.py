class Teste:
    def __init__(self):
        pass

    def __setattr__(self, key, value):
        if key == 'nome':
            self.__dict__[key] = 'Você não pode fazer isso'
        else:
            self.__dict__[key] = value

    def __del__(self):
        print('Objeto coletado')

    def __str__(self):
        return 'TESTE'

    def __len__(self):
        return 55


a = Teste()
print(len(a))
print(a)
a.nome = 'Luiz'
print(a.nome)
