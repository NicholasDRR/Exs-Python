from datetime import datetime
dados = {}

dados['nome'] = str(input('Nome: '))
nasc = int(input('Data de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['carteira'] = int(input('Carteira de trabalho (0 não tem): '))
if dados['carteira'] != 0:
    dados['contrato'] = int(input('Data de contratação: '))
    dados['salario'] = int(input('Salário: R$'))
    dados['aposentadoria'] = (dados['contrato'] + 35) - nasc
print('=' * 40)
for k, v in dados.items():
    print(f' - {k} tem o valor {v}')