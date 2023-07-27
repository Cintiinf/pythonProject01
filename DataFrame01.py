import pandas as pd

df = pd.DataFrame({
    'Aluno': ['Marina', 'Felipe', 'Clayton', 'Isabel'],
    'Créditos Cursados': [20, 64, 32, 24],
    'rendimento acadêmico': [8.55, 7.88, 8.17, 9.04],
    'Mês de nascimento': ['Novembro', 'Setembro', 'Janeiro', 'Julho'],
    'Curso': ['Computação', 'Estatística', 'Computação', 'Matemática']
})

print(df)

print(df.iloc[2])  # acessar uma linha do dataframe

print(df['rendimento acadêmico'])

print(df['rendimento acadêmico'].mean())

print(df.describe())  # imprime todas as estatísticas básicas do dataframe

df = pd.read_csv('drinks.csv')

print(df)

print(df.head(6))  # mostra as 6 primeiras linhas

print(df[df['country'] == 'Brazil'])
# imprime todas as linhas cujo valor na coluna country for Brazil

print(df[df['total_litres_of_pure_alcohol'] >= 12])

print(df[df['total_litres_of_pure_alcohol'] == 0].head())  #5 primeiros países

# head mostra por padrão os 5 primeiros da lista

print(df.sort_values(by='wine_servings', ascending = False).head())
# Ordena de forma decrescente países que consomem mais vinho





