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

def cria_grafico_mapa_vendas(vendas_estados):
    fig_mapa_vendas = px.scatter_geo(vendas_estados,
                                 lat='lat',
                                 lon='lon',
                                 scope='south america',
                                 fitbounds='locations',
                                 template='seaborn',
                                 size='Preço',
                                 hover_name='Local da compra',
                                 hover_data={'lat':False, 'lon':False},
                                 title='Vendas por estado')
    return fig_mapa_vendas

def cria_grafico_vendas_mensal(vendas_mensal):
    fig_vendas_mensal = px.line(vendas_mensal,
                            x='Mes',
                            y='Preço',
                            markers=True,
                            range_y=(0, vendas_mensal.max()),
                            color='Ano',
                            line_dash='Ano',
                            title='Quantidade de vendas mensal')
    fig_vendas_mensal.update_layout(yaxis_title='Quantidade de Vendas')
    
    return fig_vendas_mensal

def cria_grafico_vendas_estados(vendas_estados):
    fig_vendas_estados = px.bar(vendas_estados.head(),
                             x ='Local da compra',
                             y = 'Preço',
                             text_auto = True,
                             title = 'Top 5 estados')
    fig_vendas_estados.update_layout(yaxis_title='Quantidade de vendas')
    return fig_vendas_estados

def cria_grafico_vendas_categorias(vendas_categorias):
    fig_vendas_categorias = px.bar(vendas_categorias, 
                                text_auto = True,
                                title = 'Vendas por categoria')
    fig_vendas_categorias.update_layout(showlegend=False, yaxis_title='Quantidade de vendas')
    return fig_vendas_categorias

def cria_grafico_vendas_vendedores_por_receita(dados_vendedores, qtd_vendedores):
    # Filtra os dados para obter os 'qtd_vendedores' principais vendedores por receita
    top_vendedores = dados_vendedores.nlargest(qtd_vendedores, 'sum')
    fig = px.bar(
        top_vendedores,
        x='sum',
        y=top_vendedores.index,  # Garante que o índice tem o mesmo comprimento que a coluna 'sum'
        orientation='h',
        title=f'Top {qtd_vendedores} Vendedores por Receita'
    )
    fig.update_layout(xaxis_title='Receita', yaxis_title='Vendedor')
    return fig

def cria_grafico_vendas_vendedores_por_quantidade(dados_vendedores, qtd_vendedores):
    # Filtra os dados para obter os 'qtd_vendedores' principais vendedores por quantidade
    top_vendedores = dados_vendedores.nlargest(qtd_vendedores, 'count')
    fig = px.bar(
        top_vendedores,
        x='count',
        y=top_vendedores.index,  # Garante que o índice tem o mesmo comprimento que a coluna 'count'
        orientation='h',
        title=f'Top {qtd_vendedores} Vendedores por Quantidade de Vendas'
    )
    fig.update_layout(xaxis_title='Quantidade de Vendas', yaxis_title='Vendedor')
    return fig
