lista = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c} número: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
print('=-' * 20)
print(f'Os valores pares foram: {lista[0]}')
print(f'Os valores ímpares foram: {lista[1]}')
print('=-' * 20)