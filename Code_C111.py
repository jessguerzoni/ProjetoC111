
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#importando arquivo e extraindo coluna
dataset = pd.read_csv('Social_media_impact_on_life_limpo.csv', delimiter=',')

print(dataset.columns)

#01 - Existe relação entre horas de uso diário e qualidade do sono?

#Agrupamento por faixas
bins = [0, 2, 3, 4, 5, 6, 7, 8, 9, 15]
labels = ['até 2', '2-3', '3-4', '4-5', '5-6', '6-7', '7-8', '8-9', '9+']
dataset['Faixa_Uso'] = pd.cut(dataset['Daily_Usage_Hours'], bins=bins, labels=labels)

# Qualidade média do sono em cada faixa
media_sono = (dataset.groupby('Faixa_Uso', observed=True)['Sleep_Quality_Score']
              .mean().reset_index())

#Gráfico de linha
plt.figure(figsize=(9, 5))
plt.plot(media_sono['Faixa_Uso'], media_sono['Sleep_Quality_Score'], marker='*', color='tab:cyan')
plt.title('Qualidade média do sono por uso diário')
plt.xlabel('Horas de uso de redes sociais')
plt.ylabel('Qualidade média do sono')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()


#02 - Existe relação entre horas de uso diário e duração do sono?

plt.figure(figsize=(9, 5))
sns.scatterplot(data=dataset, x='Daily_Usage_Hours', y='Sleep_Duration_Hours',
                alpha=0.3, color='darkgreen')
plt.title('Duração do sono X horas de uso diário')
plt.xlabel('Horas de uso diário de redes sociais')
plt.ylabel('Duração do sono')
plt.tight_layout()
plt.show()


#03 - Qual plataforma possui a maior média de horas de uso diário?

# Cálculo da média 
media_plataforma = dataset.groupby('Primary_Platform')['Daily_Usage_Hours'].mean().reset_index().sort_values(by='Daily_Usage_Hours', ascending=False)

#Grafico de barras
plt.figure(figsize=(9, 5))
barras = plt.bar(media_plataforma['Primary_Platform'],
                 media_plataforma['Daily_Usage_Hours'],
                 color='tab:cyan')
plt.bar_label(barras, fmt='%.2f')
plt.title('Média de horas de uso diário por plataforma')
plt.xlabel('Plataforma')
plt.ylabel('Média de horas de uso diário')
plt.tight_layout()
plt.show()

#04 - O nível acadêmico está relacionado ao tempo diário de uso das redes sociais e ao desempenho acadêmico dos estudantes?

ds = pd.read_csv('Social_media_impact_on_life_limpo.csv', delimiter=',')
print(ds.columns)
plt.figure(figsize=(12, 5))

# Gráfico 1: média de horas de uso por nível acadêmico
plt.subplot(1, 2, 1)

sns.barplot(
    data=ds,
    x='Academic_Level',
    y='Daily_Usage_Hours',
    errorbar=None
)

plt.xlabel('Nível acadêmico')
plt.ylabel('Média de horas de uso')
plt.title('Uso diário das redes sociais')

# Gráfico 2: média do desempenho por nível acadêmico
plt.subplot(1, 2, 2)

sns.boxplot(
    data=ds,
    x='Academic_Level',
    y='Academic_Performance_GPA'
)

plt.xlabel('Nível acadêmico')
plt.ylabel('Média do GPA')
plt.title('Desempenho acadêmico')

plt.show()

#05 - O uso das redes sociais durante a noite está associado à duração e à qualidade do sono?

ds = pd.read_csv('Social_media_impact_on_life_limpo.csv', delimiter=',')
print(ds.columns)

# Gráfico 1: média de horas de sono por uso noturno
plt.figure(figsize=(16, 5))

plt.subplot(1, 3, 1)

sns.barplot(
    data=ds,
    x='Late_Night_Usage',
    y='Sleep_Duration_Hours',
    errorbar=None
)

plt.xlabel('Uso noturno das redes sociais')
plt.ylabel('Média de horas de sono')
plt.title('Duração do sono por uso noturno')

# Gráfico 2: distribuição das horas de sono
plt.subplot(1, 3, 2)

sns.histplot(
    data=ds,
    x='Sleep_Duration_Hours',
    hue='Late_Night_Usage',
    kde=True
)

plt.xlabel('Duração do sono (horas)')
plt.ylabel('Frequência')
plt.title('Distribuição das horas de sono')

plt.show()

#06 - A frequência de comparação com outras pessoas nas redes sociais está associada ao nível de estresse percebido e ao índice de saúde mental dos estudantes?

#07 - O tipo de dispositivo está relacionado ao tempo de uso diário?

#08 - Quais plataformas são mais utilizadas em cada nível acadêmico?

#09 - O uso adicional no fim de semana varia conforme a idade?

#10 - Quais variáveis numéricas apresentam maior relação entre si?
