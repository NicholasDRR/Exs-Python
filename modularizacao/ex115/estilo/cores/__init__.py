def linhas(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linhas())
    print(txt.center(42))
    print(linhas())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[1;93m{c} -\033[m \033[1;94m{item}\033[m')
        c += 1
    print(linhas())
    opc = leiaint('\033[32mSua opção: \033[m')
    return opc

def leiaint(msg):
    ok = False
    while not ok:
        try:
            n = int(input(msg))
            ok = True
        except (ValueError, TypeError):
            print('\033[1;31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[1;31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n
