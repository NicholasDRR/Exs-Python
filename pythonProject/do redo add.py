lista = []
lista2 = []


def add(tf):
    lista.append(tf)
    print(f'Valor {tf} adicionado!')

def redo():
    if not lista2:
        print('Nada a refazer')
        return
    valor = lista2.pop()
    lista.append(valor)

def undo():
    if not lista:
        print('Lista vazia')
        return
    valor = lista.pop()
    lista2.append(valor)

print('-' * 32)
print('''1: Adicionar        3: Refazer
2: Mostrar          4: Desfazer'''.center(32))
print('-' * 32)
while True:
    opc = input('Opção: ')
    if opc == '1':
        tarefa = input('Tarefa: ')
        add(tarefa)
    elif opc == '2':
        print(lista)
    elif opc == '3':
        redo()
    elif opc == '4':
        undo()
    else:
        print('Digite um número válido')
        opc = input('Opção: ')
