
#ETL com arquivo CSV

import pandas as pd

df = pd.read_csv('Gapminder.csv', sep=';')

print(df.head())

df=df.rename(columns={'country':'País', 'continent':'Continente', 'year':'Ano', 'lifeExp':'Expectativa de vida', 'pop':'Pop. Total', 'gdpPercap':'PIB'})

#Imprime as 20 primeiras linhas do dataframe
print('\n', df.head(20))

#Imprime o número de linhas e colunas 
print('\nNúmero de linhas e colunas: ',df.shape)

#Imprime o nome de todas as colunas
print('\nNome das colunas: ', df.columns)

#Imprime o tipo de cada coluna
print('\nTipos de dados armazenados em cada coluna: ', df.dtypes)

#Imprime as 20 últimas linhas do datafreme
print('\n', df.tail(20))

#Imprime algumas informações estatísticas do dataframe
print('\n', df.describe())

#Imprime todos os continentes que estão no dataframe
print('\n', df['Continente'].unique())

#Localiza e imprime os dados de todos os paises da Europa
europa = df.loc[df['Continente'] == 'Europe']

print('\n', europa.head())

#Imprime o número total de paises em cada continente
print('\n', df.groupby('Continente')['País'].nunique())

#Imprime a expectativa de vida média para cada ano
print('\n', df.groupby('Ano')['Expectativa de vida'].mean())

#Imprime o PIB médio
print('\n', df['PIB'].mean())



