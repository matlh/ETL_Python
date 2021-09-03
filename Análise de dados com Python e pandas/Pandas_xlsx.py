#ETL com arquivos xlsx

import pandas as pd, matplotlib.pyplot as plt

df_AR = pd.read_excel('Aracaju.xlsx')
df_FZ = pd.read_excel('Fortaleza.xlsx')
df_NT = pd.read_excel('Natal.xlsx')
df_RC = pd.read_excel('Recife.xlsx')
df_SV = pd.read_excel('Salvador.xlsx')

#Junta todos os arquivos
df = pd.concat([df_AR, df_FZ, df_NT, df_RC, df_SV])

#Imprime as 10 primeiras linhas
print('\n', df.head(10))

#Imprime as 10 últimas linhas
print('\n', df.tail(10))

#Imprime os tipos do dataframe
print('\n', df.dtypes)

#Modifica o tipo de dado da coluna lojaID de int64 para object
df['LojaID'] = df['LojaID'].astype('object')

#Imprime os tipos do dataframe
print('\n', df.dtypes)

#Imprime a soma do número de campos nulos de cada coluna
print('\n', df.isnull().sum())

#Substitui os valores nulos pela média
df['Vendas'].fillna(df['Vendas'].mean(), inplace = True)

#Imprime a soma do número de campos nulos de cada coluna
print('\n', df.isnull().sum())

#Culuna de receitas
df['Receita'] = df['Vendas'].mul(df['Qtde'])

#Imprime as 10 primeiras linhas
print('\n', df.head(10))

#Imprime a maior receita
print('\nMaior receita: ', df['Receita'].max())

#Imprime menor receita
print('\nMenor receita: ', df['Receita'].min())

#Imprime as 5 linhas com maiores receitas
print('\n', df.nlargest(5, 'Receita'))

#Imprime as 5 linhas com menores receitas
print('\n', df.nsmallest(5, 'Receita'))

#Imprime a soma das receitas por cidade
print('\n', df.groupby('Cidade')['Receita'].sum())

#Imprime as 10 primeiras linhas de receita ordenadas da maior para a menor
print('\n', df.sort_values('Receita', ascending = False).head(10))

#Tranforma coluna de dados em tipo inteiro
df['Data'] = df['Data'].astype('int64')

#Verifica os tipos de cada coluna
print('\n', df.dtypes)

#Transforma coluna de datas no tipo data
df['Data'] = pd.to_datetime(df['Data'])

#Verifica os tipos de cada coluna
print('\n', df.dtypes)

#Imprime a receita por ano
print('\n', df.groupby(df['Data'].dt.year)['Receita'].sum())

#Cria nova coluna com o ano
df['Ano_venda'] = df['Data'].dt.year

#Imprime 3 amostras do dataframe
print('\n', df.sample(3))

#Extrai o dia e mês de uma venda
df['Dia_venda'], df['Mes_venda'] = (df['Data'].dt.day, df['Data'].dt.month)

#Imprime 3 amostras do dataframe
print('\n', df.sample(3))

#Cria coluna de trimestre
df['Trimestre'] = df['Data'].dt.quarter

#Imprime 3 amostras do dataframe
print('\n', df.sample(3))

#Filtra e imprime as vendas de março de 2019
vendas_marco_19 = df.loc[(df['Data'].dt.year == 2019) & (df['Data'].dt.month == 3)]
print('\n', vendas_marco_19)

#Imprime o número de vendas para o ID de cada loja 
print(df['LojaID'].value_counts(ascending=False))

#Plota o gráfico de barras verticais do número de vendas para o ID de cada loja 
print(df['LojaID'].value_counts(ascending=False).plot.bar())
#Salva o gráfico como uma imagem .png
plt.savefig('Total de vendas por cidade.png'); 

#Plota o gráfico de barras horizontais do número de vendas para o ID de cada loja 
df['LojaID'].value_counts(ascending=False).plot.barh();

#Gráfico de pizza para a reiceita por ano
print(df.groupby(df['Data'].dt.year)['Receita'].sum().plot.pie())


#Gráfico com título e nome para os eixos
print(df['Cidade'].value_counts().plot.bar(title='Total de vandas por cidade'))
plt.xlabel('Cidade')
plt.ylabel('Total de vandas');

#Gráfico com título e nome para os eixos (alterando a cor das barras para vermelho)
print(df['Cidade'].value_counts().plot.bar(title='Total de vandas por cidade', color='red'))
plt.xlabel('Cidade')
plt.ylabel('Total de vandas');

#Altera o estilo do gráfico
plt.style.use('ggplot')





