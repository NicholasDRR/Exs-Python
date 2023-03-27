import pandas as pd
import plotly.express as px

# Passo 1: Importar a base de dados
tabela = pd.read_csv('telecom_users.csv')
# Passo 2: Visualizar a base de dados
# Entender as informações disponíveis
# Descobrir os erros da base de dados
# Excluir colunas inúteis
tabela = tabela.drop('Unnamed: 0', axis=1)  # Axis = 1 representa coluna (0 representa linha)
tabela = tabela.drop('IDCliente', axis=1)
# Passo 3: Tratamento de dados (resolver os erros da base de dados)
# Informações do tipo correto 1- Ajudar TotalGasto
tabela['TotalGasto'] = pd.to_numeric(tabela['TotalGasto'], errors='coerce')  # Transforma o valor em numérico

# Informações vazias (tabela.info() mostra o contador de valores vazios)

# Colunas vazias
tabela = tabela.dropna(how='all', axis=1)  # Exclui COLUNAS onde todos valores estiverem vazios
# Linhas com alguma infomação vazia
tabela = tabela.dropna(how='any', axis=0)  # Exclui LINHAS onde ALGUM valor estiver vazio

# Passo 4: Ánalise inicial dos dados
# Cancelamentos: 26%
#print(tabela['Churn'].value_counts(normalize=True).map('{:.1%}'.format))  # Mostra a porcentagem dos valores da coluna 'Churn'

# Passo 5: Descobrir o motivo dos cancelamentos
for colunas in tabela.columns:
    coluna = colunas
    # Etapa 1: Cria o gráfico
    grafico = px.histogram(tabela,  x=coluna, color='Churn')
    # Etapa 2: Exibe o gráfico
    grafico.show()
