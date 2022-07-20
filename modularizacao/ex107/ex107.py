import modulo107

preco = int(input('Digite o preço: '))

print(f'A metade de R${preco} é {modulo107.metade(preco)}')
print(f'O dobro de R${preco} é {modulo107.dobro(preco)}')
print(f'Aumentando 10%, temos R${modulo107.aumentar(preco, 10)}')
print(f'Diminuindo 10%, temos R${modulo107.diminuir(preco, 10)}')