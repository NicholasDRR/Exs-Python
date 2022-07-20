from teste import produtos, pessoas, lista


def aum(p):
    p['novaidade'] = (p['idade'] * 1.20)
    return p


idade = map(aum, pessoas)

for i in idade:
    print(i)

