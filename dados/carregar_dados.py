import httpx
import pandas as pd

def carregar_dados():
    url = 'https://labdados.com/produtos'
    with httpx.Client() as client:
        response = client.get(url)
        dados = pd.Dataframe.from_dict(response.json())
        return dados
