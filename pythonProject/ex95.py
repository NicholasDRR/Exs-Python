jogador = {}
lista = []
time = []
while True:
    print('-=' * 20)
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    lista.clear()
    for g in range(partidas):
        lista.append(int(input(f'  Quantos gols na partida {g+1}? ')))
        jogador['gols'] = lista[:]
        jogador['total'] = sum(lista)
    lista.clear()
    time.append(jogador.copy())
    while True:
        cont = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if cont in 'NS':
            break
        print('Digite S ou N')
    if cont == 'N':
        break
print('-=' * 20)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-=' * 20)
while True:
    cont = int(input('Mostrar dados de qual jogador?(999 pra parar) '))
    if cont == 999:
        break
    if cont >= len(time):
        print('Código inválido.')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[cont]["nome"]}: ')
        for c in range(partidas):
            print(f'No jogo {c+1} ele fez {time[cont]["gols"][c]}')

