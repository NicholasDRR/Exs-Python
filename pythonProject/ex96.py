def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg} x {comp} mede {a}')

print('-' * 20)
print('Controle de terrenos')
print('-' * 20)
l = float(input('Digite a largura do terreno: '))
c = float(input('Digite o comprimento do terreno: '))
area(l, c)
