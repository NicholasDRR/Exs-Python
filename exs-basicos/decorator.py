def criar_funcao(func):
    def interna(*args, **kwargs):
        for arg in args:
            checa(arg)
        return func(*args, **kwargs)
    return interna

def inverte(string):
    return string[::-1]


def checa(param):
    if not isinstance(param, str):
       raise TypeError('Parâmetro deve ser string')
    
criar_checando = criar_funcao(inverte)
invertida = criar_checando('123')
print(invertida)