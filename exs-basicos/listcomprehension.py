lista = []
for numero in range(10):
    lista.append(numero)
#print(lista)

lista = [
    (numero + 1) * 2
    for numero in range(10)
    ]

print(lista)