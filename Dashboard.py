import streamlit as st
import httpx
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
st.title('Dashboard de Vendas :shopping_trolley:')

url = 'https://labdados.com/produtos'

with httpx.Client() as client:
    response = client.get(url)
    html_content = response.json()
    dados = pd.DataFrame.from_dict(html_content)
    dados['Data da Compra'] = pd.to_datetime(dados['Data da Compra'], format='%d/%m/%Y')
    print(dados)
    
    
def formata_numero(valor, prefixo=''):
    unidades = ['', 'mil', 'milhões'] 
    for unidade in unidades:
        if valor < 1000:
            return f'{prefixo} {valor:.2f} {unidade}'.strip() 
        valor /= 1000
    return f'{prefixo} {valor:.2f} bilhões' 

# Tabelas
receita_estados = dados.groupby('Local da compra')[['Preço']].sum()
receita_estados = dados.drop_duplicates(subset='Local da compra')[['Local da compra', 'lat', 'lon']].merge(receita_estados, left_on='Local da compra', right_index=True).sort_values('Preço', ascending=False)

receita_mensal = dados.set_index('Data da Compra').groupby(pd.Grouper(freq='M'))['Preço'].sum().reset_index()
receita_mensal['Ano'] = receita_mensal['Data da Compra'].dt.year
receita_mensal['Mes'] = receita_mensal['Data da Compra'].dt.month_name()

# Gráficos
fig_mapa_receita = px.scatter_geo(receita_estados,
                                  lat='lat',
                                  lon='lon',
                                  scope='south america',
                                  size='Preço',
                                  template='seaborn',
                                  hover_name='Local da compra',
                                  hover_data={'lat':False, 'lon':False},
                                  title='Receita do estado')


fig_receita_mensal = px.line(receita_mensal,
                                 x='Mes',
                                 y='Preço',
                                 markers=True, 
                                 range_y=[0, receita_mensal['Preço'].max()], 
                                 color='Ano',
                                 line_dash='Ano',
                                 title='Receita Mensal')
    
fig_receita_mensal.update_layout(yaxis_title='Receita')


# Visualização no Streamlit
coluna1, coluna2 = st.columns(2)
with coluna1:
    st.metric('Receita', formata_numero(dados['Preço'].sum(), 'R$'))
    st.plotly_chart(fig_mapa_receita, use_container_width=True)
with coluna2:
    st.metric('Quantidade de Vendas', formata_numero(dados.shape[0]))
    st.plotly_chart(fig_receita_mensal)

    
st.dataframe(dados)
