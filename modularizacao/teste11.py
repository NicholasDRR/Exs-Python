n1 = float(input('Digite o numero 1: '))
n2 = float(input('Digite o numero 2: '))
print('''1: Dividir     3: Somar
2: Multiplicar 4: Subtrair'''.center(30))
opc = int(input('Digite sua opção: '))
opr = ''
if opc == 1:
    resultado = n1 / n2
    opr = '/'
elif opc == 2:
    resultado = n1 * n2
    opr = '*'
elif opc == 3:
    resultado = n1 + n2
    opr = '+'
elif opc == 4:
    resultado = n1 - n2
    opr = '-'
else:
    print('ERRO: DIGITE UMA OPÇÃO VÁLIDA.')
print(f'{n1} {opr} {n2} : {resultado}')