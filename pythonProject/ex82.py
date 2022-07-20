completa = []
pares = []
impares = []

while True:
    valor = int(input('Digite um valor: '))
    completa.append(valor)
    if valor % 2 == 0:
        pares.append(valor)
    if valor % 2 != 0:
        impares.append(valor)
    cont = str(input('Quer continuar[S/N]: '))
    if cont in 'Nn':
        print('Programa encerrado. ')
        break
print('=-' * 20)
print(f'A lista completa é {completa}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')