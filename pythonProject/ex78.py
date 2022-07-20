lista = []
maiorv = 0
menorv = 0
for c in range(0, 5):
    lista.append(int(input(f'Digite um número para a posição {c+1}: ')))
    if c == 0:
        maiorv = menorv = lista[c]
    else:
        if lista[c] > maiorv:
            maiorv = lista[c]
        if lista[c] < menorv:
            menorv = lista[c]

print(f'Você digitou os valores: {lista}')
print(f'O maior valor foi {maiorv}')
print(f'O menor valor foi {menorv}')
