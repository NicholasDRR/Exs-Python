from functools import reduce
from modularizacao.teste import pessoas, lista, produtos

acumula = 0
acumula2 = 0
acumula3 = 0
for i in lista:
    acumula += i
print(acumula)

soma_lista = reduce(lambda ac, i: i + ac, lista, 0)

print(soma_lista)

for i in produtos:
    acumula2 += i['preço']
print(f'{acumula2:.2f}')

soma_dict = reduce(lambda ac, p: p['preço'] + ac, produtos, 0)

print(f'{soma_dict:.2f}')

for i in pessoas:
    acumula3 += i['idade']
print(f'{acumula3:.2f}')

soma_idade = reduce(lambda ac, i: i['idade'] + ac, pessoas, 0)

print(f'{soma_idade:.2f}')