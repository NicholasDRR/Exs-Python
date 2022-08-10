from contextlib import contextmanager


@contextmanager
def aqv(arquivo, modo):
    try:
        arquivo = open(arquivo, modo)
        print('Abrindo arquivo')
        yield arquivo
    finally:
        print('Fechando arquivo')
        arquivo.close()


class Arquivo:
    def __init__(self, arquivo, modo):
        print('Abrindo arquivo')
        self.arquivo = open(arquivo, modo)

    def __enter__(self):
        print('Retornando arquivo')
        return self.arquivo

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Fechando arquivo')
        self.arquivo.close()
        return True  # Retorna true após tratar as exceções


with Arquivo('abc.txt', 'w') as arquivo:
    arquivo.write('Teste')

with aqv('abc2.txt', 'w') as arquivo:
    arquivo.write('Teste2')
