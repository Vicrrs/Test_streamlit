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
