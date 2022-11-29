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
df = pd.read_excel('heart_disease.xlsx', 'data')

df.columns

## Qual a taxa de infarto para cada variável explicativa?
## Média infartos por BMI, PhysicalHealth, MentalHealth e SleepTime. Das variaveis numericas

df_plot = df.groupby(['HeartDisease']).mean().reset_index()


df_plot = df_plot.melt(id_vars="HeartDisease",
                           value_vars=["BMI", "PhysicalHealth", "MentalHealth", "SleepTime"])

sns.barplot(data = df_plot, x="variable", y="value", hue="HeartDisease")
plt.show()

df_plot

def get_plot(variaveis, x, y):

        df_plot = df.groupby([variaveis]).mean().reset_index()
        df_plot = df_plot.melt(id_vars=variaveis,
                               value_vars=["BMI", "PhysicalHealth", "MentalHealth", "SleepTime"])
        sns.barplot(data = df_plot, x="variable", y="value", hue=variaveis)
        plt.rcParams['figure.figsize']=(x,y)
        

get_plot('HeartDisease')
get_plot('AlcoholDrinking')
get_plot('Stroke')
get_plot('DiffWalking')
get_plot('Sex')
get_plot('AgeCategory', 10, 10)
get_plot('Race')
get_plot('Diabetic')
get_plot('PhysicalActivity')
get_plot('GenHealth')
get_plot('Asthma')
get_plot('KidneyDisease')
get_plot('SkinCancer')


## Histograma
def get_hist(variavel, bins):
    plt.title(f'{variavel}')
    plt.xlabel(f'{variavel}')
    plt.ylabel('Frequência Absoluta')
    plt.hist(df[f'{variavel}'], bins, rwidth=0.9)
    plt.xticks(rotation=90)
    plt.show()

# histogramas utilizados
get_hist("BMI", 40)
get_hist("PhysicalHealth", 40)
get_hist("MentalHealth", 30)
get_hist("SleepTime", 25)
get_hist("AgeCategory", 13)


## correlação e heatmap das variáveis 

df.corr()

sns.heatmap(df.corr(), annot=True)











