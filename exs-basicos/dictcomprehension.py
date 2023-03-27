dict = {
    'nome': 'luiz',
    'idade': 19,
    'cidade': 'sp',
}

dict2 = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor
    in dict.items()
    if chave != 'cidade'
}

list = [
    ('a', 'valor a'),
    ('b', 'valor a'),
    ('b', 'valor a'),
]

#dict3 = {
#    chave: valor
#    for chave, valor in list
#}

set = {i * 2 for i in range(10)}
print(set)