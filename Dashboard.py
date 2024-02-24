import streamlit as st
import httpx
import pandas as pd
import plotly.express as px

st.title('Dashboard de Vendas :shopping_trolley:')

url = 'https://labdados.com/produtos'

with httpx.Client() as client:
    response = client.get(url)
    html_content = response.json()
    dados = pd.DataFrame.from_dict(html_content)
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

# Visualização no Streamlit
coluna1, coluna2 = st.columns(2)
with coluna1:
    st.metric('Receita', formata_numero(dados['Preço'].sum(), 'R$'))
    st.plotly_chart(fig_mapa_receita)
with coluna2:
    st.metric('Quantidade de Vendas', formata_numero(dados.shape[0]))

    
st.dataframe(dados)
