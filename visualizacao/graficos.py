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
