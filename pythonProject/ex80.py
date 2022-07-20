numeros = []

for c in range(0, 5):
    valor = int(input('Digite um valor: '))
    if c == 0 or valor > numeros[-1]:
        numeros.append(valor)
    else:
        pos = 0
        while pos < len(numeros):
            if valor <= numeros[pos]:
                numeros.insert(pos, valor)
                break
            pos += 1
print(numeros)