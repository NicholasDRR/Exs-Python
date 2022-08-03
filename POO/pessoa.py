from datetime import datetime
from random import randint


class Pessoa:
    # Pegando ano atual
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    # Método que pede os parâmetros e as informações do indivíduo
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    # Método de classe
    @classmethod
    def poranonasc(cls, nome, nasc):
        idade = cls.ano_atual - nasc
        return cls(nome, idade)

    # Método estático
    @staticmethod
    def criaid():
        return randint(10000, 19999)

    # Método para falar
    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo')
            return
        if self.falando:
            print(f'{self.nome} já está falando')
            return
        print(f'{self.nome} está falando sobre {assunto}')
        self.falando = True

    # Método para parar de falar
    def pararfalar(self):
        if not self.falando:
            print(f'{self.nome} não está falando')
            return
        print(f'{self.nome} parou de falar')
        self.falando = False

    # Método para comer
    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo...')
            return
        if self.falando:
            print(f'{self.nome} já está falando...')
            return
        print(f'{self.nome} está comendo {alimento}')
        self.comendo = True

    # Método para parar de comer
    def pararcomer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo')
            return
        print(f'{self.nome} parou de comer')
        self.comendo = False

    # Método para calcular idade
    def anonasc(self):
        return self.ano_atual - self.idade
