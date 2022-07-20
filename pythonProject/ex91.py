from random import randint
from time import sleep
from operator import itemgetter
resultados = {
'Jogador 1': randint(1, 6),
'Jogador 2': randint(1, 6),
'Jogador 3': randint(1, 6),
'Jogador 4': randint(1, 6)
}
ranking = ()
print('Valores sorteados: ')
print('=' * 26)
for k, v in resultados.items():
    print(f'{k} tirou {v} no dado.')
print('=' * 26)
ranking = sorted(resultados.items(), key=itemgetter(1), reverse=True)
print('Ranking: ')
for i, v in enumerate(ranking):
    print(f'{i+ 1} lugar: {v[0]} com {v[1]} pontos')
