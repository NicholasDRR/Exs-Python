from random import randint


def sorteio(*num):
    for c in range(0, 5):
        n = randint(1, 10)
        numero.append(n)
    print(f'Sorteando os {len(num)} valores da lista: {numero}: ')


def somapar(lista):
    par = 0
    for v in lista:
        if v % 2 == 0:
            par += v
    print(f'Somando os valores pares de {lista} temos: {par}')


numero = list()
sorteio(numero)
somapar(numero)
