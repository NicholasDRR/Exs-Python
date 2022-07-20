import modulo108

preco = float(input('Digite o preço: R$'))

print(f'A metade de {modulo108.moeda(preco)} é {modulo108.metade(preco, True)}')
print(f'O dobro de {modulo108.moeda(preco)} é {modulo108.dobro(preco, True)}')
print(f'Aumentando 10%, temos {modulo108.aumentar(preco, 10, True)}')
print(f'Diminuindo 10%, temos {modulo108.diminuir(preco, 10, True)}')
