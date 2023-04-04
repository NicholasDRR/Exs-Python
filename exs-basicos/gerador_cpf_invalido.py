from random import randint

def formata(n):
    return ''.join(map(str, n)) 

def cria_cpf():
    
    modelo = '000-000-000.00'
    cpf = []
    
    for caracter in modelo:
        if caracter =='0':
            caracter = randint(0,9)
        cpf.append(caracter)
        
    cpf_formatado = formata(cpf)
    return cpf_formatado


print('-'*20)
print('GERADOR DE CPF'.center(20))
print('-'*20)
quantidade = int(input('Deseja gerar quantos? '))

for c in range(quantidade):
    resultado = cria_cpf()
    print(f'{c+1}: {resultado}'.center(20))