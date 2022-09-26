def maior(* num):
    cont = maior = 0
    print('-=' * 20)
    print('Analisando os valores passados...')
    print('( ', end='')
    for c in num:
        cont += 1
        print(f'{c} ', end='')
        if cont == 0:
            maior = cont
        else:
            if c > maior:
                maior = c
    print(')')
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor encontrado foi {maior}')






maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 8)
maior(1, 2)
maior()
