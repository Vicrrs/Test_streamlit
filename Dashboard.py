import streamlit as st
from dados.carrega_dados import carregar_dados
from utilidades.formatadores import formata_numero

from visualizacao.tabelas import (
    cria_tabela_receita_estados, 
    cria_tabela_receita_mensal, 
    cria_tabela_receita_categoria, 
    cria_tabela_vendas_estados, 
    cria_tabela_vendas_mensal, 
    cria_tabela_vendas_categoria, 
    cria_tabela_vendas_vendedores)

from visualizacao.graficos import (
    cria_mapa_receita, 
    cria_grafico_receita_mensal, 
    cria_grafico_receita_estados, 
    cria_grafico_receita_categorias, 
    cria_grafico_mapa_vendas, 
    cria_grafico_vendas_estados, 
    cria_grafico_vendas_mensal, 
    cria_grafico_vendas_categorias,
    cria_grafico_vendas_vendedores_por_receita,
    cria_grafico_vendas_vendedores_por_quantidade
)


st.set_page_config(layout="wide")
st.title('Dashboard de Vendas :shopping_trolley:')

dados = carregar_dados()

regioes = ['Brasil', 'Centro-Oeste', 'Nordeste', 'Norte', 'Sudeste', 'Sul']

st.sidebar.title('Filtros')
regiao = st.sidebar.selectbox('Região', regioes)
if regiao == 'Brasil':
    regiao = ''
    
todos_anos = st.sidebar.checkbox('Dados de todo o período', value=True)
ano = '' if todos_anos else st.sidebar.slider('Ano', 2020, 2023)

dados = carregar_dados(regiao.lower(), ano)

filtro_vendedores = st.sidebar.multiselect('Vendedores', dados['Vendedor'].unique())
if filtro_vendedores:
    dados = dados[dados['Vendedor'].isin(filtro_vendedores)]

receita_estados = cria_tabela_receita_estados(dados)
fig_mapa_receita = cria_mapa_receita(receita_estados)

receita_mensal = cria_tabela_receita_mensal(dados)
fig_receita_mensal = cria_grafico_receita_mensal(receita_mensal)

fig_receita_estados = cria_grafico_receita_estados(receita_estados)

receita_categoria = cria_tabela_receita_categoria(dados)
fig_receita_categorias = cria_grafico_receita_categorias(receita_categoria)

aba1, aba2, aba3 = st.tabs(['Receita', 'Quantidade de vendas', 'Vendendores'])
with aba1:
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        st.metric('Receita', formata_numero(dados['Preço'].sum(), 'R$'))
        st.plotly_chart(fig_mapa_receita, use_container_width=True)
        st.plotly_chart(fig_receita_estados, use_container_width=True)
    with coluna2:
        st.metric('Quantidade de Vendas', formata_numero(dados.shape[0]))
        st.plotly_chart(fig_receita_mensal)
        st.plotly_chart(fig_receita_categorias, use_container_width=True)
        
with aba2:
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        vendas_estados = cria_tabela_vendas_estados(dados)
        fig_mapa_vendas = cria_grafico_mapa_vendas(vendas_estados)
        st.plotly_chart(fig_mapa_vendas, use_container_width=True)
        vendas_estados = cria_tabela_vendas_estados(dados)
        fig_vendas_estados = cria_grafico_vendas_estados(vendas_estados)
        st.plotly_chart(fig_vendas_estados, use_container_width=True)

    with coluna2:
        vendas_mensal = cria_tabela_vendas_mensal(dados)
        fig_vendas_mensal = cria_grafico_vendas_mensal(vendas_mensal)
        st.plotly_chart(fig_vendas_mensal, use_container_width=True)
        vendas_categoria = cria_tabela_vendas_categoria(dados)
        fig_vendas_categorias = cria_grafico_vendas_categorias(vendas_categoria)
        st.plotly_chart(fig_vendas_categorias, use_container_width=True)
        

with aba3:
    coluna1, coluna2 = st.columns(2)
    dados_vendedores = cria_tabela_vendas_vendedores(dados)
    qtd_vendedores = st.sidebar.number_input('Quantidade de Vendedores', min_value=1, max_value=len(dados_vendedores), value=5)

    with coluna1:
        st.metric('Total de Receita por Vendedores', formata_numero(dados_vendedores['sum'].sum(), 'R$'))
        fig_receita_vendedores = cria_grafico_vendas_vendedores_por_receita(dados_vendedores, qtd_vendedores)
        st.plotly_chart(fig_receita_vendedores, use_container_width=True)

    with coluna2:
        st.metric('Total de Vendas por Vendedores', formata_numero(dados_vendedores['count'].sum()))
        fig_quantidade_vendedores = cria_grafico_vendas_vendedores_por_quantidade(dados_vendedores, qtd_vendedores)
        st.plotly_chart(fig_quantidade_vendedores, use_container_width=True)


