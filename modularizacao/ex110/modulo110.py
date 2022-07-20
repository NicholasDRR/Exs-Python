def resumo(p, aum, red, format=False):
    dobro = p * 2
    metade = p / 2
    aumentado = p + (p * (aum / 100))
    diminuido = p - (p * (red / 100))
    din = 'R$'
    if format:
        p = str(f'{din} {p:.2f}'.replace('.', ','))
        dobro = str(f'{din} {dobro:.2f}'.replace('.', ','))
        metade = str(f'{din} {metade:.2f}'.replace('.', ','))
        aumentado = str(f'{din} {aumentado:.2f}'.replace('.', ','))
        diminuido = str(f'{din} {diminuido:.2f}'.replace('.', ','))
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: {p}')
    print(f'Dobro do preço: {dobro}')
    print(f'Metade do preço: {metade}')
    print(f'{aum}% de aumento: {aumentado}')
    print(f'{red}% de redução: {diminuido}')
    print('-' * 30)
