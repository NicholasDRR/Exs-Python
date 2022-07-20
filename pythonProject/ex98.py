def contador(i, f, p):
    print('-='*20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        c = i
        while c <= f:
            print(f'{c}  ', end='')
            c += p
        print('Fim')
    else:
        c = i
        while c >= f:
            print(f'{c}  ', end='')
            c -= p
        print('Fim')

contador(1, 10, 1)
contador(10, 0, 2)
print('-='*20)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(ini, fim, passo)



