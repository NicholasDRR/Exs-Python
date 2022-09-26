lista = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    cont = str(input('Quer continuar[S/N]: '))
    if cont in 'Nn':
        break
print('-' * 26)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, l in enumerate(lista):
    print(f'{i:<4}{l[0]:<10}{l[2]:>8}')

while True:
    opc = int(input('Mostrar nota de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(lista) - 1:
        print(f'Notas de {lista[opc][0]}: {lista[opc][1]}')
