def leiaint():
    ok = False
    while not ok:
        try:
            n = int(input('Digite um número inteiro: '))
            ok = True
        except (ValueError, TypeError):
            print('\033[1;31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[1;31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n


def leiafloat():
    ok = False
    while not ok:
        try:
            n = float(input('Digite um número real: '))
            ok = True
        except (ValueError, TypeError):
            print('\033[1;31mERRO: por favor, digite um número real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[1;31mEntrada de dados interrompida pelo usuário\033[m')
            return 0
        else:
            return n


print(f'O valor inteiro digitado foi {leiaint()} e o real foi {leiafloat()}')
