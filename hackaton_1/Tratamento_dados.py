# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 11:50:04 2022

@author: João Lucas
"""

import pandas as pd
import numpy as np
import wget
import os
import matplotlib.pyplot as plt
from zipfile import ZipFile
import zipfile

# consolidando diretório de trabalho
os.getcwd()
os.chdir('C:\\Users\\myjoa\\Documents\\GitHub\\Data_Science_ML\\hackaton_1')

# Fórmula get_data para obter dados de trabalho
## a) Baixe a base de julho de 2022
def get_data(ano, mes):
    url = f'https://www.bcb.gov.br/pda/desig/planilha_{ano}.zip'
    arquivo = url.split('/')[-1]
    
    if not arquivo in os.listdir():
        wget.download(url)
    
    df = pd.read_csv(zipfile.ZipFile(arquivo).open(f'planilha_2022{mes}.csv'), sep=";", decimal=',')
    
    return(df)

df_07 = get_data(2022, '07')
df_08 = get_data(2022, '08')

df = pd.concat([df_07, df_08])

## b) Filtre apenas PF (pessoa física) ‘cliente’==PF
df_pf = df[df['cliente'] == 'PF' ]

## c) Ordene a base para ter a coluna na seguinte ordem e nomenclatura:
df_pf = df_pf[[ 'data_base', 'uf', 'ocupacao', 'porte', 'modalidade', 'carteira_ativa', 'vencido_acima_de_15_dias']]

## e) Elimine as variáveis que não estão em (c). Note que: se dropar
##    simplesmente as colunas a mais as linhas ficarão com redundância.
##    Usei groupby() para somar as variaveis iguais.
df_pf_1 = df_pf.groupby(['data_base', 'uf', 'ocupacao', 'porte', 'modalidade'], as_index=False)['carteira_ativa', 'vencido_acima_de_15_dias'].sum()

## f) Construa a variável inadimplência percentual

df_pf_1['inad_perc'] = df_pf_1['vencido_acima_de_15_dias']/df_pf_1['carteira_ativa']

## download arquivos csv tratados

df.to_csv ('df.csv', index = False)

df_pf_1.to_csv ('df_pf_1.csv', index = False)

