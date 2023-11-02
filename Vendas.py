import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

vendas = np.array([10.5, 11.2, 12, 13.5, 15.2, 14.8, 14.6, 15.3, 16, 17.2, 16.5, 18, 10.8, 11.4, 12.2, 13.7, 15.6, 15, 14.9, 15.8, 16.3, 17.4, 16.8, 18.5, 11.2, 12, 12.8, 14.2, 16, 15.4, 15.2, 16.1, 17, 17.8, 17.1, 19, 11.5, 12.3, 13.2])

vendas_2024 = np.array([10.5, 11.2, 12, 13.5, 15.2, 14.8, 14.6, 15.3, 16, 17.2, 16.5, 18])
vendas_2025 = np.array([10.8, 11.4, 12.2, 13.7, 15.6, 15, 14.9, 15.8, 16.3, 17.4, 16.8, 18.5])
vendas_2026 = np.array([11.2, 12, 12.8, 14.2, 16, 15.4, 15.2, 16.1, 17, 17.8, 17.1, 19])
vendas_2027 = np.array([11.5, 12.3, 13.2])
vendas_ordenadas = np.sort(vendas)
vendas_media = round(vendas_ordenadas.mean(), 2)

print("Parte 1")
print("Média: ", vendas_media)
print("Mediana de 2024: ", np.median(vendas_2024))
print("Mediana de 2025: ", np.median(vendas_2025))
print("Mediana de 2026: ", np.median(vendas_2026))
print("Mediana de 2027: ", np.median(vendas_2027))
print("Variância: ", round(vendas_ordenadas.var(), 2))
print("Desvio padrão: ", round(vendas_ordenadas.std(), 2))

desvio_absoluto_medio = np.mean(np.abs(vendas - vendas_media))
limite_atipicidade = 2 * desvio_absoluto_medio
valores_atipicos = vendas[np.abs(vendas - vendas_media) > limite_atipicidade]

print("Valores atípicos:", valores_atipicos)

    
print("\n\nParte 2")
q1 = np.percentile(vendas, 25)
q2 = np.percentile(vendas, 50)
q3 = np.percentile(vendas, 75)

print('q1: ', q1)
print('q2: ', q2)
print('q3: ', q3)

quartil1 = [num for num in vendas_ordenadas if num < q1]
quartil2 = [num for num in vendas_ordenadas if num >= q1 and num < q2]
quartil3 = [num for num in vendas_ordenadas if num >= q2 and num < q3]
quartil4 = [num for num in vendas_ordenadas if num >= q3]

print("Primeiro quartil: ", quartil1)
print("Segundo quartil: ", quartil2)
print("Terceiro quartil: ", quartil3)
print("Quarto quartil: ", quartil4)
print('Intervalo interquartil: ', q3 - q1)

print("\n\nParte 3")

variacao_media_absoluta = np.mean([abs(v - vendas_media) for v in vendas])
previsao_2028 = vendas_media + variacao_media_absoluta
previsao_2029 = previsao_2028 + variacao_media_absoluta
previsao_2030 = previsao_2029 + variacao_media_absoluta
previsao_2031 = previsao_2030 + variacao_media_absoluta
previsao_2032 = previsao_2031 + variacao_media_absoluta

print('Previsão de vendas para 2028: ', round(previsao_2028, 2))
print('Previsão de vendas para 2029: ', round(previsao_2029, 2))
print('Previsão de vendas para 2030: ', round(previsao_2030, 2))
print('Previsão de vendas para 2031: ', round(previsao_2031, 2))
print('Previsão de vendas para 2032: ', round(previsao_2032, 2))

erro_medio = np.mean([abs(v - previsao_2028) for v in vendas])
erro_percentual_medio = (erro_medio/np.mean(vendas))*100

print("Erro Médio:", round(erro_medio, 2))
print("Erro Percentual Médio:", round(erro_percentual_medio, 2), "%")


