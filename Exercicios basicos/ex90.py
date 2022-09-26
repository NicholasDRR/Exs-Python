resultados = {}

resultados['nome'] = str(input('Nome: '))
resultados['media'] = float(input(f'Média de {resultados["nome"]}: '))
print('=' * 20)
print(f' - Nome é igual a {resultados["nome"]}')
print(f' - Média é igual a {resultados["media"]}')

if resultados["media"] >= 7:
    resultados["situacao"] = 'Aprovado'
elif 5 <= resultados["media"] < 7:
    resultados["situacao"] = 'Recuperação'
else:
    resultados["situacao"] = 'Reprovado'

print(f' - A sua situação atual é {resultados["situacao"]}')