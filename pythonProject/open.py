with open('t.txt', 'w+') as teste:
    teste.write('Linha1\n')
    teste.write('Linha2\n')
    teste.write('Linha3\n')
    teste.seek(0)
    print(teste.read())
