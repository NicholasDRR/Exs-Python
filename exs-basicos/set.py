# set nao aceita valores mutaveis
lista = [3,2,3,4,35,3,6,3,('Nicholas Ribeiro'), ('Hahaha')]
lista2 = set(lista) 
lista3 = set()

for items in lista:
    lista3.add(items)

lista3.update(('Juliano fonseca', 2, 3))
lista3.discard(35)
#lista3.clear()
print(lista3)
