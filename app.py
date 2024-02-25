import streamlit as st
from dados.carrega_dados import carregar_dados
from visualizacao.graficos import cria_mapa_receita, cria_grafico_receita_mensal
from visualizacao.tabelas import cria_tabela_receita_estados, cria_tabela_receita_mensal
from utilidades.formatadores import formata_numero

st.set_page_config(layout="wide")
st.title('Dashboard de Vendas :shopping_trolley:')

dados = carregar_dados()

receita_estados = cria_tabela_receita_estados(dados)
fig_mapa_receita = cria_mapa_receita(receita_estados)

receita_mensal = cria_tabela_receita_mensal(dados)
fig_receita_mensal = cria_grafico_receita_mensal(receita_mensal)

coluna1, coluna2 = st.columns(2)
with coluna1:
    st.metric('Receita', formata_numero(dados['Preço'].sum(), 'R$'))
    st.plotly_chart(fig_mapa_receita, use_container_width=True)
with coluna2:
    st.metric('Quantidade de Vendas', formata_numero(dados.shape[0]))
    st.plotly_chart(fig_receita_mensal)

st.dataframe(dados)
