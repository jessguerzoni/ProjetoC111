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

print(dataset.columns)
plt.figure(figsize=(12, 5))

# Gráfico 1: média de horas de uso por nível acadêmico
plt.subplot(1, 2, 1)

sns.barplot(
    data=dataset,
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
    data=dataset,
    x='Academic_Level',
    y='Academic_Performance_GPA'
)

plt.xlabel('Nível acadêmico')
plt.ylabel('Média do GPA')
plt.title('Desempenho acadêmico')

plt.show()

#05 - O uso das redes sociais durante a noite está associado à duração e à qualidade do sono?

print(dataset.columns)

plt.figure(figsize=(12, 5))

# Gráfico 1: distribuição da qualidade do sono
plt.subplot(1, 2, 1)

sns.boxplot(
    data=ds,
    x='Late_Night_Usage',
    y='Sleep_Quality_Score'
)

plt.xlabel('Uso noturno das redes sociais')
plt.ylabel('Qualidade do sono')
plt.title('Qualidade do sono por uso noturno')

# Gráfico 2: distribuição da duração do sono
plt.subplot(1, 2, 2)

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

print(dataset.columns)
plt.figure(figsize=(12, 5))

# Gráfico 1: comparação social e estresse percebido
plt.subplot(1, 2, 1)

sns.barplot(
    data=dataset,
    x='Social_Comparison_Frequency',
    y='Perceived_Stress_Score',
    errorbar=None,
)

plt.xlabel('Frequência de comparação social')
plt.ylabel('Média do estresse percebido')
plt.title('Comparação social e estresse')

# Gráfico 2: comparação social e saúde mental
plt.subplot(1, 2, 2)

sns.boxplot(
    data=dataset,
    x='Social_Comparison_Frequency',
    y='Mental_Health_Index'
)

plt.xlabel('Frequência de comparação social')
plt.ylabel('Índice de saúde mental')
plt.title('Comparação social e saúde mental')

plt.show()

#07- O tipo de dispositivo está relacionado ao tempo de uso das redes sociais e à qualidade do sono?

plt.figure(figsize=(10, 6))
sns.boxplot(
    data = dataset,
    x = 'Device_Type',
    y = 'Daily_Usage_Hours',
    hue = 'Academic_Level'
)
plt.title('Uso diário por dispositivo e nível acadêmico')
plt.legend(title='Nível acadêmico', bbox_to_anchor=(1.02, 1),loc='upper left')
plt.tight_layout()
plt.show()

filtro_smartphones = dataset['Device_Type'].str.contains('Smartphone')
smartphones = dataset[filtro_smartphones]

notas, quantidade_notas = np.unique(smartphones['Sleep_Quality_Score'],return_counts=True)

plt.figure(figsize=(16, 5))
plt.subplot(1, 3, 1)
plt.bar(notas, quantidade_notas)
plt.xlabel('Nota de qualidade do sono')
plt.ylabel('Quantidade de estudantes')
plt.title('Qualidade do sono dos usuários de smartphones')

filtro_tablet = dataset['Device_Type'].str.contains('Tablet')
tablets = dataset[filtro_tablet]

notasT, quantidade_notasT = np.unique(tablets['Sleep_Quality_Score'],return_counts=True)

plt.subplot(1, 3, 2)
plt.bar(notasT, quantidade_notasT)
plt.xlabel('Nota de qualidade do sono')
plt.ylabel('Quantidade de estudantes')
plt.title('Qualidade do sono dos usuários de tablets')

filtro_pc = dataset['Device_Type'].str.contains('Laptop/PC')
pc = dataset[filtro_pc]

notasPC, quantidade_notasPC = np.unique(pc['Sleep_Quality_Score'],return_counts=True)

plt.subplot(1, 3, 3)
plt.bar(notasPC, quantidade_notasPC)
plt.xlabel('Nota de qualidade do sono')
plt.ylabel('Quantidade de estudantes')
plt.title('Qualidade do sono dos usuários de Laptop/PC')
plt.tight_layout()
plt.show()


# 08 - Quais plataformas são mais utilizadas em cada nível acadêmico e como o uso delas se relaciona ao estresse percebido?
# Identificar as 3 plataformas mais utilizadas no conjunto inteiro
plataformas, quantidades = np.unique(dataset['Primary_Platform'], return_counts=True)

contagem = pd.Series(quantidades, index=plataformas)
top3 = contagem.nlargest(3).index

# Filtrar cada nível acadêmico
high = dataset[dataset['Academic_Level'].str.contains('High School')]
post = dataset[dataset['Academic_Level'].str.contains('Postgraduate')]
under = dataset[dataset['Academic_Level'].str.contains('Undergraduate')]

# Contar as plataformas de cada nível acadêmico
plataformas1, quantidades1 = np.unique(high['Primary_Platform'], return_counts=True)
plataformas2, quantidades2 = np.unique(post['Primary_Platform'], return_counts=True)
plataformas3, quantidades3 = np.unique(under['Primary_Platform'], return_counts=True)

# Gráficos de pizza
plt.figure(figsize=(18, 6))

plt.subplot(1, 3, 1)
plt.pie(quantidades1, labels=plataformas1, autopct='%1.1f%%')
plt.title('High School')

plt.subplot(1, 3, 2)
plt.pie(quantidades2, labels=plataformas2, autopct='%1.1f%%')
plt.title('Postgraduate')

plt.subplot(1, 3, 3)
plt.pie(quantidades3, labels=plataformas3, autopct='%1.1f%%')
plt.title('Undergraduate')

plt.tight_layout()
plt.show()

# Boxplot: somente as 3 plataformas mais utilizadas
filtro = dataset['Primary_Platform'].isin(top3)
dados_top3 = dataset[filtro]

plt.figure(figsize=(12, 6))

sns.boxplot(
    data=dados_top3,
    x='Primary_Platform',
    y='Perceived_Stress_Score',
    hue='Academic_Level'
)

plt.title('Estresse percebido por plataforma e nível acadêmico')
plt.xlabel('Plataforma principal')
plt.ylabel('Nível de estresse percebido')

plt.tight_layout()
plt.show()

#09 - Quais faixas etárias apresentam maior tempo diário de uso das redes sociais e maior uso adicional nos finais de semana?
# Calcular as médias para cada idade
media_diaria = dataset.groupby('Age')['Daily_Usage_Hours'].mean()
media_fim_semana = dataset.groupby('Age')['Weekend_Extra_Hours'].mean()

plt.figure(figsize=(14, 5))

# Primeiro subplot: média de horas de uso diário
plt.subplot(1,2,1)
sns.lineplot(
    x=media_diaria.index,
    y=media_diaria.values,
    marker='o',
)

plt.title('Média de uso diário por idade')
plt.xlabel('Idade')
plt.ylabel('Média de horas diárias')

# Segundo subplot: média de horas extras no fim de semana
plt.subplot(1,2,2)
sns.lineplot(
    x=media_fim_semana.index,
    y=media_fim_semana.values,
    marker='o',
)

plt.title('Média de uso adicional por idade')
plt.xlabel('Idade')
plt.ylabel('Média de horas extras no fim de semana')

plt.tight_layout()
plt.show()

#10 - Quais variáveis numéricas apresentam maior relação entre si?
corr = dataset[['Daily_Usage_Hours', 'Weekend_Extra_Hours','Sleep_Duration_Hours', 'Sleep_Quality_Score','Perceived_Stress_Score', 'Mental_Health_Index',
     'Academic_Performance_GPA']].corr()

sns.heatmap(
    corr,
    annot=True,
    fmt='.2f',
    cmap='YlOrRd',
    vmin=-1,
    vmax=1)
plt.title('Correlação entre variáveis numéricas')
plt.show()
