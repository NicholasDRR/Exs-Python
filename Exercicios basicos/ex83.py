exp = str(input('Digite sua expressão: '))
lista = []
for c in exp:
    if c == '(':
        lista.append('(')
    elif c == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break

if len(lista) == 0:
    print('Sua expressão está correta')
else:
    print('Sua expressão está incorreta')
