preco = 1000


def imposto(preco):
    return preco * 0.3


imposto2 = lambda x: x * 0.3

print(imposto(preco))
print(imposto2(preco))

precos = [100, 500, 10, 50]

impostos = list(map(lambda x: x * 0.3, precos))

print(impostos)
