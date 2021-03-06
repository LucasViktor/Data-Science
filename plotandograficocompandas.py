# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 19:16:04 2020

@author: LucasViktor
"""
import pandas as pd
#lendo a planilha 
#A parte entre aspas é o caminho
# r é para indicar leitura
planilha = pd.read_excel(r'C:\Users\Calixto\Documents\planilha.xlsx')

#imprime a planilha na tela para o usuário
#esse passo não é necessário =D
print(planilha)

#gráfico comum
planilha.plot( x = 'Idade', y = 'Massa', color = 'blue')

#Histograma
planilha.plot(kind = 'hist', x = 'Idade', y = 'Massa', color = 'blue')

#gráfico de dispersão
planilha.plot(kind = 'scatter', x = 'Idade', y = 'Massa', color = 'blue')