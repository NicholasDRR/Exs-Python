lista = []
lista2 = []
mai = men = 0
while True:
    lista2.append(str(input('Nome: ')))
    lista2.append(int(input('Peso: ')))
    if len(lista) == 0:
        mai = men = lista2[1]
    else:
        if lista2[1] > mai:
            mai = lista2[1]
        if lista2[1] < men:
            men = lista2[1]
    lista.append(lista2[:])
    lista2.clear()
    cont = str(input('Quer continuar[S/N]: '))
    if cont in 'Nn':
        print('Programa encerrado.')
        break
print(f'{len(lista)} pessoas foram cadastradas.')
print(f'Maior peso {mai}')
for c in lista:
    if c[1] == mai:
        print(f'{c[0]}')
print(f'Menor peso {men}')
for c in lista:
    if c[1] == men:
        print(f'{c[0]}')