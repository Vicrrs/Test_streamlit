import httpx
import pandas as pd
import requests


def carregar_dados(regiao='', ano=''):
    url = 'https://labdados.com/produtos'
    params = {'regiao': regiao, 'ano': ano}
    response = requests.get(url, params=params)
    dados = pd.DataFrame.from_dict(response.json())
    dados['Data da Compra'] = pd.to_datetime(dados['Data da Compra'], format='%d/%m/%Y')
    return dados
