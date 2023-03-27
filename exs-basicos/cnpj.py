import re
import random

regressivo = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]  # Lista com os valores da fórmula


# Função pra validar
def valida(cnpj):
    cnpj = numeros(cnpj)
    try:
        if numsequencia(cnpj):
            return False
    except:
        return False
    try:
        novo = calcuca(cnpj, digito=1)
        novo = calcuca(cnpj=novo, digito=2)
    except:
        return False

    if novo == cnpj:
        return True
    else:
        return False


# Retorna o cnpj com apenas números
def numeros(cnpj):
    return re.sub(r'\D', '', cnpj)


# Verifica se o cnpj recebido são uma sequência de números iguais
def numsequencia(cnpj):
    sequencia = cnpj[0] * len(cnpj)
    if sequencia == cnpj:
        print('É uma sequência')
        return True
    else:
        return False


# Retorna o cálculo da fórmula
def calcuca(cnpj, digito):
    if digito == 1:
        regressivos = regressivo[1:]
        novo = cnpj[:-2]
    elif digito == 2:
        regressivos = regressivo
        novo = cnpj
    else:
        return None
    total = 0
    for i, c in enumerate(regressivos):
        total += int(cnpj[i]) * c
    digito = 11 - (total % 11)
    digito = digito if digito <= 9 else 0
    return f'{novo}{digito}'


# Gera CNPJ
def gera():
    digito1 = random.randint(0, 9)
    digito2 = random.randint(0, 9)
    bloco1 = random.randint(100, 999)
    bloco2 = random.randint(100, 999)
    bloco3 = '0001'
    cnpj = f'{digito1}{digito2}{bloco1}{bloco2}{bloco3}00'
    novo = calcuca(cnpj=cnpj, digito=1)
    novo = calcuca(cnpj=novo, digito=2)
    return novo


def formata(cnpj):
    cnpj = numeros(cnpj)
    formatado = f'{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]}'
    return formatado


for count in range(10):
    cnpj = gera()
    formatado = formata(cnpj)
    print(f'{count+1}: {formatado}')
