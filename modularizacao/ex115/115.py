from estilo import cores, arquivo
arq = 'cadastro.txt'
if not arquivo.arquivo(arq):
    arquivo.criar(arq)
while True:
    resposta = cores.menu(['Ver pessoas cadastradas', 'Cadastrar novas pessoas', 'Sair do sistema'])
    if resposta == 1:
        cores.cabecalho('pessoas cadastradas'.upper())
        arquivo.ler(arq)
    elif resposta == 2:
        cores.cabecalho('novo cadastro'.upper())
        nome = str(input('Nome: '))
        idade = cores.leiaint('Idade: ')
        arquivo.cadastrar(arq, nome, idade)
    elif resposta == 3:
        cores.cabecalho('Saindo do sistema.')
        break
    else:
        print('ERRO: Digite uma opção válida')