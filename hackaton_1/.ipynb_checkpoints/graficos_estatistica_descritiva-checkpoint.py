# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 21:52:40 2022

@author: myjoa
"""

### Estatística descritiva básica

## g) Avalie as variáveis de forma descritiva. Faça gráficos e tabelas de forma a
##    explicar a inadimplência. Quais os perfis de maior inadimplência.

# Lendo os dados
df_pf_1 = pd.read_csv('df_pf_1.csv')

## Quais os estados com maior carteira de crédito e suas respectivas taxas de inadimplência?
# Executando gráfico de barra para maiores carteiras de crédito por estado
data_plot_df_1 = df_pf_1.groupby(['data_base', 'uf'], as_index = False)['vencido_acima_de_15_dias',
                                                           'carteira_ativa'].sum().sort_values(by=['carteira_ativa'])

data_plot_df_1 = data_plot_df_1.pivot(index='uf',
                                      columns='data_base',
                                      values= 'carteira_ativa').reset_index().sort_values(by=['2022-07-31'])

x = list(data_plot_df_1['uf'])
x_axis = np.arange(len(x))


f = plt.figure()
f.set_figwidth(10)
f.set_figheight(5)
plt.bar(x_axis - 0.2,
        data_plot_df_1['2022-07-31'],
        color ='maroon',
        width = 0.50,
        label = "Julho")
plt.bar(x_axis + 0.2,
        data_plot_df_1['2022-08-31'],
        color ='blue',
        width = 0.50,
        label = "Agosto")
plt.xticks(x_axis, x)
plt.xlabel('Estados do País (UF)')
plt.ylabel('Carteira de Crédito Ativa')
plt.title('Carteira ativa de crédito por estado')
plt.legend()
plt.show()


# Grafico de barras empilhadas para ver a proporção de inadimplentes por carteira
data_plot_df_2 = df_pf_1.groupby(['data_base', 'uf'], as_index = False)['vencido_acima_de_15_dias',
                                                           'carteira_ativa'].sum()

data_plot_df_2['inad_perc'] = data_plot_df_2['vencido_acima_de_15_dias']/data_plot_df_2['carteira_ativa']

data_plot_df_2 = data_plot_df_2.pivot(index='uf',
                                      columns='data_base',
                                      values= 'inad_perc').reset_index().sort_values(by=['2022-07-31'])

x = list(data_plot_df_2['uf'])
x_axis = np.arange(len(x))

f = plt.figure()
f.set_figwidth(10)
f.set_figheight(5)
plt.bar(x_axis - 0.2,
        data_plot_df_2['2022-07-31'],
        color ='maroon',
        width = 0.50,
        label = 'Julho')
plt.bar(x_axis + 0.2,
        data_plot_df_2['2022-08-31'],
        color ='blue',
        width = 0.50,
        label = 'Agosto')
plt.xticks(x_axis, x)
plt.xlabel('Estados do País (UF)')
plt.ylabel('Taxa de inadimplencia')
plt.title('Taxa de inadimplencia por estado mês de julho e agosto')
plt.legend()
plt.show()

## qual a taxa de inadimplência por ocupação?
# Ajustando os dados que usaremos para o grafico
# Gráfico de barras para maiores carteiras de crédito por ocupação
data_plot_df_3 = df_pf_1.groupby(['data_base', 'ocupacao'], as_index = False)['vencido_acima_de_15_dias',
                                                           'carteira_ativa'].sum()

data_plot_df_3 = data_plot_df_3.pivot(index='ocupacao',
                                      columns='data_base',
                                      values= 'carteira_ativa').sort_values(by=['2022-07-31']).reset_index()


x = list(data_plot_df_3['ocupacao'])
x_axis = np.arange(len(x))
width = 0.4
fig, ax = plt.subplots()
ax.barh(x_axis, data_plot_df_3['2022-07-31'], width, color='maroon', label='Julho')
ax.barh(x_axis + width, data_plot_df_3['2022-08-31'], width, color='blue', label='Agosto')
ax.set(yticks = x_axis + width,
       yticklabels = data_plot_df_3['ocupacao'],
       ylim = [2*width - 1, len(x)])
plt.xlabel('Carteira Ativa')
plt.ylabel('Ocupação')
plt.title('Carteira ativa de crédito por ocupação mês de julho e agosto')
ax.legend()
plt.show()


# Gráfico com as maiores taxas de inadimplência

data_plot_df_4 = df_pf_1.groupby(['data_base', 'ocupacao'], as_index = False)['vencido_acima_de_15_dias',
                                                           'carteira_ativa'].sum()

data_plot_df_4['inad_perc'] = data_plot_df_4['vencido_acima_de_15_dias']/data_plot_df_4['carteira_ativa']

data_plot_df_4 = data_plot_df_4.pivot(index='ocupacao',
                                      columns='data_base',
                                      values= 'inad_perc').reset_index().sort_values(by=['2022-07-31'])

x = list(data_plot_df_4['ocupacao'])
x_axis = np.arange(len(x))
width = 0.4
fig, ax = plt.subplots()
ax.barh(x_axis, data_plot_df_4['2022-07-31'], width, color='maroon', label='Julho')
ax.barh(x_axis + width, data_plot_df_4['2022-08-31'], width, color='blue', label='Agosto')
ax.set(yticks = x_axis + width,
       yticklabels = data_plot_df_4['ocupacao'],
       ylim = [2*width - 1, len(x)])
plt.xlabel('Taxa de inadimplência')
plt.ylabel('Ocupação')
plt.title('Taxa de inadimplência por ocupação no mês de julho')
ax.legend()
plt.show()

## Qual a taxa de inadimplência o o tamanho das carteira de credito por renda?
# Gráfico para maiores carteiras de crédito por renda
data_plot_df_5 = df_pf_1.groupby(['data_base', 'porte'], as_index = False)['vencido_acima_de_15_dias',
                                                           'carteira_ativa'].sum()

data_plot_df_5 = data_plot_df_5.pivot(index='porte',
                                      columns='data_base',
                                      values= 'carteira_ativa').sort_values(by=['2022-07-31']).reset_index()

x = list(data_plot_df_5['porte'])
x_axis = np.arange(len(x))
width = 0.4
fig, ax = plt.subplots()
ax.barh(x_axis, data_plot_df_5['2022-07-31'], width, color='maroon', label='Julho')
ax.barh(x_axis + width, data_plot_df_5['2022-08-31'], width, color='blue', label='Agosto')
ax.set(yticks = x_axis + width,
       yticklabels = data_plot_df_5['porte'],
       ylim = [2*width - 1, len(x)])
plt.xlabel('Carteira de crédito ativa')
plt.ylabel('Porte')
plt.title('Carteira de crédito ativa por renda no mês de julho')
ax.legend()
plt.show()

# Gráfico com as taxas de inadimplência por renda
data_plot_df_6 = df_pf_1.groupby(['data_base', 'porte'], as_index = False)['vencido_acima_de_15_dias',
                                                           'carteira_ativa'].sum()

data_plot_df_6['inad_perc'] = data_plot_df_6['vencido_acima_de_15_dias']/data_plot_df_6['carteira_ativa']

data_plot_df_6 = data_plot_df_6.pivot(index='porte',
                                      columns='data_base',
                                      values= 'inad_perc').sort_values(by=['2022-07-31']).reset_index()

x = list(data_plot_df_6['porte'])
x_axis = np.arange(len(x))
width = 0.4
fig, ax = plt.subplots()
ax.barh(x_axis, data_plot_df_6['2022-07-31'], width, color='maroon', label='Julho')
ax.barh(x_axis + width, data_plot_df_6['2022-08-31'], width, color='blue', label='Agosto')
ax.set(yticks = x_axis + width,
       yticklabels = data_plot_df_6['porte'],
       ylim = [2*width - 1, len(x)])
plt.xlabel('Carteira de crédito ativa')
plt.ylabel('Porte')
plt.title('Carteira de crédito ativa por renda no mês de julho')
ax.legend()
plt.show()

## Quais as maiores modalidade de crédito e suas respectivas taxas de inadimplência?
# Gráfico para maiores carteiras de crédito por modalidade
data_plot_df_7 = df_pf_1.groupby(['data_base', 'modalidade'], as_index = False)['vencido_acima_de_15_dias',
                                                           'carteira_ativa'].sum()

data_plot_df_7 = data_plot_df_7.pivot(index='modalidade',
                                      columns='data_base',
                                      values= 'carteira_ativa').sort_values(by=['2022-07-31']).reset_index()

x = list(data_plot_df_7['modalidade'])
x_axis = np.arange(len(x))
width = 0.4
fig, ax = plt.subplots()
ax.barh(x_axis, data_plot_df_7['2022-07-31'], width, color='maroon', label='Julho')
ax.barh(x_axis + width, data_plot_df_7['2022-08-31'], width, color='blue', label='Agosto')
ax.set(yticks = x_axis + width,
       yticklabels = data_plot_df_7['modalidade'],
       ylim = [2*width - 1, len(x)])
plt.xlabel('Carteira de crédito ativa')
plt.ylabel('Modalidade')
plt.title('Carteira de crédito ativa por modalidade no mês de julho e agosto')
ax.legend()
plt.show()

# Gráfico com as taxas de inadimplencia por modalidade
data_plot_df_8 = df_pf_1.groupby(['data_base', 'modalidade'], as_index = False)['vencido_acima_de_15_dias',
                                                           'carteira_ativa'].sum()

data_plot_df_8['inad_perc'] = data_plot_df_8['vencido_acima_de_15_dias']/data_plot_df_8['carteira_ativa']

data_plot_df_8 = data_plot_df_8.pivot(index='modalidade',
                                      columns='data_base',
                                      values= 'inad_perc').sort_values(by=['2022-07-31']).reset_index()

x = list(data_plot_df_8['modalidade'])
x_axis = np.arange(len(x))
width = 0.4
fig, ax = plt.subplots()
ax.barh(x_axis, data_plot_df_8['2022-07-31'], width, color='maroon', label='Julho')
ax.barh(x_axis + width, data_plot_df_8['2022-08-31'], width, color='blue', label='Agosto')
ax.set(yticks = x_axis + width,
       yticklabels = data_plot_df_8['modalidade'],
       ylim = [2*width - 1, len(x)])
plt.xlabel('Taxa de inadimplência')
plt.ylabel('Modalidade')
plt.title('Taxa de inadimplência por modalidade no mês de julho')
ax.legend()
plt.show()

