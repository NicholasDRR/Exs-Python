def fatorial(num, sh):
    tot = 1
    for c in range(num, 0, -1):
        tot *= c
        if sh:
            print(f'{c}', end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(' = ', end='')

    return tot




resp = str(input('Deseja mostrar o cálculo? [S/N]: ')).upper()[0]
if resp == 'S':
    show = True
else:
    show = False
print(fatorial(5, show))
