from dataclasses import dataclass


@dataclass
class Pessoa:
    nome: str
    sobrenome: str

    @property
    def nomecompleto(self):
        return f'{self.nome} {self.sobrenome}'


p1 = Pessoa('Luiz', 'Fernando')
print(p1.nomecompleto)
