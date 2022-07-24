if __name__ == '__main__':
    lista = []
    redo = []
    while True:
        todo = input('Digite uma tarefa [undo, redo, ls]: ')
        if todo == 'ls':
            print(lista)
            continue
        elif todo == 'redo '