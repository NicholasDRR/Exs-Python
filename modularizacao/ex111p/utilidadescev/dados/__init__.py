def leia(p):
    valido = False
    while not valido:
        entrada = str(input(p)).replace(',', '.').strip()
        if entrada.isalpha() or len(entrada) == 0:
            print(f'\033[0;31mERRO: O PREÇO "{entrada}" É INVÁLIDO.\033[m')
        else:
            valido = True
            return float(entrada)
