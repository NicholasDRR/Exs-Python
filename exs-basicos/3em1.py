import copy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

novos_produtos = [
    {**p, 'preco': round(p['preco'] * 1.1, 2)}
    for p in copy.deepcopy(produtos)
]
produtos_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda p:p['nome'],
    reverse=True
)

produtos_preco = sorted(
    copy.deepcopy(produtos),
    key=lambda p:p['preco']
)


for p in novos_produtos:
    print(p)
print()
for p in produtos_nome:
    print(p)
print()
for p in produtos_preco:
    print(p)
    

