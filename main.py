import pandas as pd

s = pd.Series([1, 2, 3, 4, 5])  # matriz unidimensional
print(s)

# com índice
print(s[3])

s = pd.Series([15, 20, 12, 16, 10, 11, 12, 15, 9, 10, 12, 17],
              index=['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez'])

print(s)

print(s['jan'])

print(s[0:6])

print(s.mean())  # média de acidentes
print(s.std())  # desvio padrão
print(s.max())  # maximo
print(s.min())  # minimo

print(s.describe())  # resumo das estatisticas

print(s.sum())  # somatorio

print(s[6:].mean())  #média do segundo semestre

