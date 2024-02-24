import streamlit as st
from dados.carrega_dados import carrega_dados
from visualizacao.graficos import cria_mapa_receita
from visualizacao.tabelas import cria_tabela_receita_estados
from utilidades.formatadores import formata_numero

st.title('Dashboard de Vendas :shopping_trolley:')

dados = carrega_dados()

receita_estados = cria_tabela_receita_estados(dados)
fig_mapa_receita = cria_mapa_receita(receita_estados)

coluna1, coluna2 = st.columns(2)
with coluna1:
    st.metric('Receita', formata_numero(dados['Preço'].sum(), 'R$'))
    st.plotly_chart(fig_mapa_receita)
with coluna2:
    st.metric('Quantidade de Vendas', formata_numero(dados.shape[0]))

st.dataframe(dados)
