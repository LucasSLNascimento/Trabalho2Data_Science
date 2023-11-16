import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# PARTE 1 

# MEDIA: OK
# MEDIANAS: OK
# VARIANCIA E DESVIO PADRAO: ok
# MAIOR E MENOR VENDA: 

# PARTE 2

# quartis: ok
# intervalo interquartil: ok

# PARTE 3 

# PREVISAO 2028: 
# ERRO MEDIO E ERRO MEDIO PERCENTUAL:
# PREVISAO 2028 ATE 2032:


df = pd.read_csv('C:/Users/lucas/OneDrive/Documentos/Estudos/Faculdade/Semestre_6/Data_Science/Trabalho2Data_Science/Vendas.csv', index_col='Ano', parse_dates=True, sep=';')

df_2024 = df[df.index.year == 2024]
df_2025 = df[df.index.year == 2025]
df_2026 = df[df.index.year == 2026]
df_2027 = df[df.index.year == 2027]

print('Parte 1')
media_vendas = round(df['Vendas(emunidadesmonetárias)'].mean(), 2)
mediana_2024 = df_2024['Vendas(emunidadesmonetárias)'].median()
mediana_2025 = df_2025['Vendas(emunidadesmonetárias)'].median()
mediana_2026 = df_2026['Vendas(emunidadesmonetárias)'].median()
mediana_2027 = df_2027['Vendas(emunidadesmonetárias)'].median()
variancia = round(df['Vendas(emunidadesmonetárias)'].var(), 2)
desvio_padrao = round(df['Vendas(emunidadesmonetárias)'].std(), 2)
mes_menor_venda = df['Vendas(emunidadesmonetárias)'].idxmin
mes_maior_venda = df['Vendas(emunidadesmonetárias)'].idxmax

print("Média de Vendas: ", media_vendas)
print('Mediana das vendas de 2024: ', mediana_2024)
print('Mediana das vendas de 2025: ', mediana_2025)
print('Mediana das vendas de 2026: ', mediana_2026)
print('Mediana das vendas de 2027: ', mediana_2027)
print('Variância: ', variancia)
print('Desvio padrão', desvio_padrao)

print('\n\nParte 2')
vendas = df['Vendas(emunidadesmonetárias)']

q1 = np.percentile(vendas, 25)
q2 = np.percentile(vendas, 50)
q3 = np.percentile(vendas, 75)

print('q1: ', q1)
print('q2: ', q2)
print('q3: ', q3)

quartil1 = [num for num in vendas if num < q1]
quartil2 = [num for num in vendas if num >= q1 and num < q2]
quartil3 = [num for num in vendas if num >= q2 and num < q3]
quartil4 = [num for num in vendas if num >= q3]

print("Primeiro quartil: ", quartil1)
print("Segundo quartil: ", quartil2)
print("Terceiro quartil: ", quartil3)
print("Quarto quartil: ", quartil4)
print('Intervalo interquartil: ', q3 - q1)

print('\n\nParte 3')

df.index = pd.to_datetime(df.index, format='%Y')  

ts = df['Vendas(emunidadesmonetárias)']
model = sm.tsa.ExponentialSmoothing(ts, trend='add', seasonal='add', seasonal_periods=12)
model_fit = model.fit()

previsao = model_fit.forecast(steps=12) 

print("Previsão para o ano de 2028:", round(previsao.sum(), 2))

# Valores fictícios para as vendas reais de cada mês em 2028
valores_reais_2028 = np.array([20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42])
previsoes_2028 = np.array(previsao)

mae = np.mean(np.abs(valores_reais_2028 - previsoes_2028))
mape = np.mean(np.abs((valores_reais_2028 - previsoes_2028) / valores_reais_2028)) * 100

print(f"Erro Médio Absoluto (MAE): {mae}")
print(f"Erro Percentual Médio Absoluto (MAPE): {mape}%")


