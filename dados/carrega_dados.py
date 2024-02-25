import httpx
import pandas as pd

def carregar_dados():
    url = 'https://labdados.com/produtos'
    with httpx.Client() as client:
        response = client.get(url)
        dados = pd.DataFrame.from_dict(response.json())
        dados['Data da Compra'] = pd.to_datetime(dados['Data da Compra'], format='%d/%m/%Y')
        return dados
