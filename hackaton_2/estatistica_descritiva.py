# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 19:45:39 2022

@author: myjoa
"""

import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns


# consolidando diretório de trabalho
os.getcwd()
os.chdir('C:\\Users\\myjoa\\Documents\\GitHub\\Data_Science_ML\\hackaton_2')

# Lendo os dados
xls = pd.ExcelFile('heart_disease.xlsx')
df = pd.read_excel(xls, 'data')

df.columns

## Qual a taxa de infarto para cada variável explicativa?
## Média infartos por BMI, PhysicalHealth, MentalHealth e SleepTime. Das variaveis numericas

df_plot = df.groupby(['HeartDisease']).mean().reset_index()


df_plot = df_plot.melt(id_vars="HeartDisease",
                           value_vars=["BMI", "PhysicalHealth", "MentalHealth", "SleepTime"])

sns.barplot(data = df_plot, x="variable", y="value", hue="HeartDisease")
plt.show()

def get_plot(variaveis):
    
        df_plot = df.groupby([variaveis]).mean().reset_index()
        df_plot = df_plot.melt(id_vars=variaveis,
                               value_vars=["BMI", "PhysicalHealth", "MentalHealth", "SleepTime"])
        x = sns.barplot(data = df_plot, x="variable", y="value", hue=variaveis)
        return(x)
    
plt.show(list(df.columns))

## correlação e heatmap das variáveis 
df.corr()

sns.heatmap(df.corr(), annot=True)


df.plot










