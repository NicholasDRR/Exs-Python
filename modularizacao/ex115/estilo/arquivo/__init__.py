def arquivo(aqv):
    try:
        a = open(aqv, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar(aqv):
    try:
        a = open(aqv, "wt+")
        a.close()
    except:
        print('Houve um erro na criação do arquivo.')
    else:
        print(f'Arquivo {aqv} criado com sucesso.')


def ler(aqv):
    try:
        a = open(aqv, "rt")
    except:
        print('Houve um erro em abrir o arquivo.')
    else:
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30} {dado[1]:<3}')
    finally:
        a.close()


def cadastrar(aqv, nome='Desconhecido', idade='0'):

    try:
        a = open(aqv, "at")
    except:
        print('Houve um erro na abertura do arquivo.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na hora de escrever os dados')
        else:
            print(f'Novo registro de {nome}')
        finally:
            a.close()




