dados = {}
lista = []
soma = media = 0
while True:
    dados.clear()
    dados['nome'] = str(input('Nome: '))
    while True:
        dados['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if dados['sexo'] in 'MF':
            break
        print('Digite M OU F')
    dados['idade'] = int(input('Idade: '))
    soma += dados['idade']
    lista.append(dados.copy())
    while True:
        cont = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if cont in 'SN':
            break
        print('Erro, digite S ou N.')
    if cont == 'N':
        break
media = int(soma / len(lista))
print('=' * 30)
print(f'A) No total foram cadastradas {len(lista)} pessoas.')
print(f'B) A média das idades é {media}')
print('C) As mulheres cadastradadas foram ', end='')
for p in lista:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end=' ')
print()
print('D) Lista de pessoas acima ou na média de idade: ')
for p in lista:
    if p['idade'] >= media:
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<<<<Encerrado>>>>')




