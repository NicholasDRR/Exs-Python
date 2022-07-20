def aumentar(p=0, v=0, format=False):
    aumento = p + (p * v / 100)
    return aumento if format is False else moeda(aumento)


def dobro(p=0, format=False):
    dob = p * 2
    return dob if format is False else moeda(dob)


def metade(p=0, format=False):
    met = p / 2
    return met if format is False else moeda(met)


def diminuir(p=0, taxa=0, format=False):
    diminuida = p - (p * taxa / 100)
    return diminuida if format is False else moeda(diminuida)


def moeda(p=0, moeda='R$'):
    return f'{moeda}{p:.2f}'.replace('.', ',')
