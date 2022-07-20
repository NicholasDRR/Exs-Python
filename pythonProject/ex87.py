lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = c3 = mai = 0

for l in range(0, 3):
    for c in range(0 , 3):
        lista[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if lista[l][c] % 2 == 0:
            par += lista[l][c]
        if lista[1][c] > mai:
            mai = lista[1][c]
for l in range(0, 3):
    c3 += lista[l][2]
print('=-' * 14)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{lista[l][c]:^5}]', end='')
    print()
print('=-' * 14)
print(f'A soma dos valores pares é {par}.')
print(f'A soma da terceira coluna é {c3}.')
print(f'O maior valor da segunda linha é {mai}.')

