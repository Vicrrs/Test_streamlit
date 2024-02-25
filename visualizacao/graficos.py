import plotly.express as px

def cria_mapa_receita(receita_estados):
    fig_mapa_receita = px.scatter_geo(receita_estados,
                                      lat='lat',
                                      lon='lon',
                                      scope='south america',
                                      size='Preço',
                                      template='seaborn',
                                      hover_name='Local da compra',
                                      hover_data={'lat': False, 'lon': False},
                                      title='Receita do estado')
    return fig_mapa_receita

def cria_grafico_receita_mensal(receita_mensal):
    fig_receita_mensal = px.line(receita_mensal,
                                 x='Mes',
                                 y='Preço',
                                 markers=True, 
                                 range_y=[0, receita_mensal['Preço'].max()], 
                                 color='Ano',
                                 line_dash='Ano',
                                 title='Receita Mensal')
    
    fig_receita_mensal.update_layout(yaxis_title='Receita')
    return fig_receita_mensal

def cria_grafico_receita_estados(receita_estados):
    fig_receita_estados = px.bar(receita_estados.head(),
                            x = 'Local da compra',
                            y = 'Preço',
                            text_auto=True,
                            title="Top estados (receita)")
    fig_receita_estados.update_layout(yaxis_title='Receita')
    return fig_receita_estados

def cria_grafico_receita_categorias(receita_categorias):
    fig_receita_categorias = px.bar(receita_categorias,
                                    x=receita_categorias.index,
                                    y='Preço',
                                    text_auto=True,
                                    title='Receita por categoria')
    fig_receita_categorias.update_layout(yaxis_title='Receita')
    return fig_receita_categorias
