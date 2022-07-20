dados = {}
lista = list()
dados['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
for c in range(partidas):
    lista.append(int(input(f'    Quantos gols na partida {c+1}? ')))
    dados['gols'] = lista[:]
    dados['total'] = sum(dados['gols'])
print('=' * 60)
print(dados)
print('=' * 60)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('=' * 60)
print(f'O jogador {dados["nome"]} jogou {partidas} partidas.')
for i, v in enumerate(dados['gols']):
    print(f'    Na partida {i+1} ele marcou {v} gols.')
print(f'No total foram {dados["total"]} gols')
