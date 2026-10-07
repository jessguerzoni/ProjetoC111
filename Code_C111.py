
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

#04 - Como o uso das redes sociais varia entre faixas etárias?

#05 - A qualidade do sono varia de acordo com o gênero?

#06 - O nível acadêmico está relacionado ao tempo diário de uso?

#07 - O tipo de dispositivo está relacionado ao tempo de uso diário?

#08 - Quais plataformas são mais utilizadas em cada nível acadêmico?

#09 - O uso adicional no fim de semana varia conforme a idade?

#10 - Quais variáveis numéricas apresentam maior relação entre si?
