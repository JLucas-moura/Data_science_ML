# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 22:36:13 2022

@author: myjoa
"""
import pandas as pd
import numpy as np
import statsmodels.api as sm


## Modelo de Regressão para explicar a Inadimplência Percentual
#Obtendo os dados
df = pd.read_csv('df.csv')

# filtrando pessoa fisica
df_pf = df[df['cliente'] == 'PF']


# filtrando mes de julho
df_pf_07 = df_pf[df_pf['data_base'] == '2022-07-31']
df_pf_08 = df_pf[df_pf['data_base'] == '2022-08-31']

# inserindo taxa de inadimplência
df_pf_07['inad_perc'] = df_pf_07['vencido_acima_de_15_dias']/df_pf_07['carteira_ativa']
df_pf_08['inad_perc'] = df_pf_08['vencido_acima_de_15_dias']/df_pf_08['carteira_ativa']

# ajustando o numero de operacoes maiores que 15
df_pf_07.loc[df_pf_07['numero_de_operacoes'] == '<= 15', 'numero_de_operacoes'] = 15
df_pf_07['numero_de_operacoes'] = df_pf_07['numero_de_operacoes'].astype(str).astype(int)

df_pf_08.loc[df_pf_08['numero_de_operacoes'] == '<= 15', 'numero_de_operacoes'] = 15
df_pf_08['numero_de_operacoes'] = df_pf_08['numero_de_operacoes'].astype(str).astype(int)

# tirando média de credito por operacao
df_pf_07['venc_media'] = df_pf_07['vencido_acima_de_15_dias']/df_pf_07['numero_de_operacoes']

df_pf_08['venc_media'] = df_pf_08['vencido_acima_de_15_dias']/df_pf_08['numero_de_operacoes']

# tirando média de vencido por operacao
df_pf_07['cred_media'] = df_pf_07['carteira_ativa']/df_pf_07['numero_de_operacoes']

df_pf_08['cred_media'] = df_pf_08['carteira_ativa']/df_pf_08['numero_de_operacoes']

# definindo as variaveis que queremos
df_pf_07_1 = df_pf_07[['uf','ocupacao','porte', 'modalidade', 'inad_perc', 'venc_media']]

df_pf_08_1 = df_pf_08[['uf','ocupacao','porte', 'modalidade', 'inad_perc', 'venc_media']]




## Transformando variáveis de classificação em dummies
df_pf_07_dummies = pd.get_dummies(df_pf_07_1)

df_pf_08_dummies = pd.get_dummies(df_pf_08_1)

# Lista com os nomes das colunas (serve para os dois meses)
names = list(df_pf_07_dummies)

# Variáveis removidas por conta do alto P-valor
names.remove('inad_perc')
names.remove('porte_PF - Mais de 10 a 20 salários mínimos        ')
names.remove('modalidade_PF - Veículos')
names.remove('uf_GO')
names.remove('uf_CE')
names.remove('uf_ES')
names.remove('uf_RO')
names.remove('uf_TO')
names.remove('ocupacao_PF - Aposentado/pensionista')           
names.remove('ocupacao_PF - Autônomo')
names.remove('ocupacao_PF - Empregado de empresa privada')
names.remove('ocupacao_PF - Servidor ou empregado público')

# Determinando variáveis explicativas e dependentes
X = df_pf_07_dummies[names]
y = df_pf_07_dummies['inad_perc']

# Modelo de regressão
model_1 = sm.OLS(y, X).fit()
model_1.summary()

# Modelo para mês de agosto
XX = df_pf_08_dummies[names]
yy = df_pf_08_dummies['inad_perc']

model_2 = sm.OLS(yy, XX).fit()
model_2.summary()








