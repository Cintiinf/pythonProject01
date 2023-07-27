import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="darkgrid")

uri='room_data.txt'

room = pd.read_csv(uri)

print(room.head())

# variação de temperatura ao longo do tempo
#plt.figure(figsize=(10,5))
#plt.title('Variação da temperatura ao longo do tempo')
#sns.scatterplot(x="date", y="Temperature", data=room)  # identifica a coluna que sera o x e y
# scatter = espalhar
#plt.show()

room['date'] = pd.to_datetime(room['date'])
plt.figure(figsize=(10,5))
plt.title("Variação da temperatura ao longo do tempo")
sns.lineplot(x='date', y='Temperature', data=room)
plt.show()

# outra base de dados de hiv que não achei
hiv_uri = ''
hiv = pd.read_csv(hiv_uri)
print(hiv.head())

# visualiza como a taxa de HIV variou no mundo inteiro ao redor dos anos
plt.figure(figsize=(10,5))
plt.title('Variação da taxa média de HIV global')
sns.lineplot(x='date', y='HIV Rate', data=hiv)
plt.show()

# taxas médias por nível de renda dos países
plt.figure(figsize=(10,5))
plt.title('Variação da taxa média de HIV para níveis de renda')
sns.lineplot(x='date', y='HIV Rate', hue='Income Leve', ci=None, data=hiv)
plt.show()

# é prudente evitar representar muitas variáveis simultaneamente no mrdmo gráfico de Linha
plt.figure(figsize=(10,5))
plt.title('Variação da taxa média de HIV para cada país')
sns.lineplot(x='date', y='HIV Rate', hue='country', legend= False, data=hiv)
plt.show()


