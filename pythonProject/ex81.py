lista = []
while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    cont = str(input('Quer continuar[S/N]: '))
    if cont in 'Nn':
        print('Programa encerrado.')
        break

lista.sort(reverse=True)
print(f'Você digitou {len(lista)} elementos.')
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 está na lista')
else:
    print('5 não está na lista')

