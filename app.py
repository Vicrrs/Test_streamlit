import streamlit as st
from dados.carrega_dados import carregar_dados
from visualizacao.graficos import cria_mapa_receita, cria_grafico_receita_mensal, cria_grafico_receita_estados, cria_grafico_receita_categorias
from visualizacao.tabelas import cria_tabela_receita_estados, cria_tabela_receita_mensal, cria_tabela_receita_categoria
from utilidades.formatadores import formata_numero

st.set_page_config(layout="wide")
st.title('Dashboard de Vendas :shopping_trolley:')

dados = carregar_dados()

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
        st.metric('Receita', formata_numero(dados['Preço'].sum(), 'R$'))
    with coluna2:
        st.metric('Quantidade de Vendas', formata_numero(dados.shape[0]))
        
with aba3:
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        st.metric('Receita', formata_numero(dados['Preço'].sum(), 'R$'))
    with coluna2:
        st.metric('Quantidade de Vendas', formata_numero(dados.shape[0]))

