import pandas as pd, matplotlib.pyplot as plt
plt.style.use('seaborn')

#Importa base de dados
df = pd.read_excel('AdventureWorks.xlsx')

#Exibe as 5 primeiras linhas da base de dados
print(df.head())

#Número de linahs e colunas
print('\n', df.shape)

#Tipos de dados
print('\n', df.dtypes)

#Receita total
print('\nReceita total: ', df['Valor Venda'].sum())

#Coluna para o custo
df['Custo'] = df['Custo Unitário'].mul(df['Quantidade'])

#Custo total (valor arredondado com 2 casas decimais)
print('\nCusto: ', round(df['Custo'].sum(), 2))

#Cálculo do lucro
df['Lucro'] = df['Valor Venda'] - df['Custo']

#Lucro (valor arredondado com 2 casas decimais)
print('\nLucro: ', round(df['Lucro'].sum(), 2))

#Coluna para o total de dias para envio do produto
df['Tempo Envio'] = df['Data Envio'] - df['Data Venda']

#Extraindo os dias restantes
df['Tempo Envio'] = (df['Data Envio'] - df['Data Venda']).dt.days

#Tipo da coluna do tempo envio
print('\n', df['Tempo Envio'].dtype)

#Média de tempo de envio para cada marca
print('\n', df.groupby('Marca')['Tempo Envio'].mean())

#Verifica se existe compos vazios
print('\n', df.isnull().sum())

#Lucro agrupado por ano e marca
print('\n', df.groupby([df['Data Venda'].dt.year, 'Marca'])['Lucro'].sum())

#Reseta o index
Lucro_ano = df.groupby([df['Data Venda'].dt.year, 'Marca'])['Lucro'].sum().reset_index()
print('\n', Lucro_ano)

#Total de produtos vendidos
print('\n', df.groupby('Produto')['Quantidade'].sum().sort_values(ascending=False))


#Gráfico para o total de produtos vendidos
df.groupby('Produto')['Quantidade'].sum().sort_values(ascending=True).plot.barh(title = 'Total de produtos vendidos')
plt.xlabel('Total')
plt.ylabel('Produto');

#Gráfico de lucro por ano
df.groupby(df['Data Venda'].dt.year)['Lucro'].sum().plot.bar(title = 'Lucro por ano')
plt.xlabel('Ano')
plt.ylabel('Lucro');

#Lucro por mês no ano de 2009
df_2009 = df[df['Data Venda'].dt.year == 2009]
df_2009.groupby(df_2009['Data Venda'].dt.month)['Lucro'].sum().plot(title = 'Lucro por mês 2009')
plt.xlabel('Mês')
plt.ylabel('Lucro');

#Lucro por marca no ano de 2009
df_2009.groupby('Marca')['Lucro'].sum().plot.bar(title = 'Lucro por marca 2009')
plt.xlabel('Marca')
plt.ylabel('Lucro');

#Lucro por classe no ano de 2009
df_2009.groupby('Classe')['Lucro'].sum().plot.bar(title = 'Lucro por classe 2009')
plt.xlabel('Classe')
plt.ylabel('Lucro');

#Dados estatísticos sobre o tempo de envio
print('\n', df['Tempo Envio'].describe())

#Gráfico de boxplot para o tempo de envio
plt.boxplot(df['Tempo Envio']);

#Histograma para o tempo de envio
plt.hist(df['Tempo Envio']);

#Tempo mínimo de envio
df['Tempo Envio'].min()

#Salva em aquivo .csv a base de dados de vendas
df.to_csv('df_vendas_novo.csv', index=False)




















