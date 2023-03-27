from modularizacao.teste import pessoas, lista, produtos

test2 = filter(lambda p: p['preço'] > 20, produtos)
test1 = filter(lambda x: x > 5, lista)
test = filter(lambda i: i['idade'] > 30, pessoas)


for c in test:
    print(c)
print(list(test1))
for c in test2:
    print(c)