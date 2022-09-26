from random import randint
from time import sleep
lista = []
lista2 = []
tot = 1
print('=' * 20)
print('      MEGA SENA      ')
print('=' * 20)
jogos = int(input('Quantos jogos você quer que eu sorteie? '))
print('-=' * 3, f'SORTEANDO {jogos} JOGOS', '-=' * 3)
for c in range(jogos):
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    lista2.append(lista[:])
    lista.clear()
for i, l in enumerate(lista2):
    print(f'Jogo {i+1}: {l}')
    sleep(2)
print('-=' * 3, 'Boa sorte!', '-=' * 3)