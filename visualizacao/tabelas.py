import pandas as pd

def cria_tabela_receita_estados(dados):
    receita_estados = dados.groupby('Local da compra')[['Preço']].sum()
    receita_estados = dados.drop_duplicates(subset='Local da compra')[['Local da compra', 'lat', 'lon']].merge(receita_estados, left_on='Local da compra', right_index=True).sort_values('Preço', ascending=False)
    return receita_estados


def cria_tabela_receita_mensal(dados):
    receita_mensal = dados.set_index('Data da Compra').groupby(pd.Grouper(freq='ME'))['Preço'].sum().reset_index()
    receita_mensal['Ano'] = receita_mensal['Data da Compra'].dt.year
    receita_mensal['Mes'] = receita_mensal['Data da Compra'].dt.month_name()

    return receita_mensal

def cria_tabela_receita_categoria(dados):
    receita_categorias = dados.groupby('Categoria do Produto')[['Preço']].sum().sort_values('Preço', ascending=False)
    return receita_categorias

def cria_tabela_vendas_estados(dados):
    vendas_estados = pd.DataFrame(dados.groupby('Local da compra')['Preço'].count())
    vendas_estados = dados.drop_duplicates(subset='Local da compra')[['Local da compra', 'lat', 'lon']].merge(vendas_estados, left_on='Local da compra', right_index=True).sort_values('Preço', ascending=False)
    return vendas_estados

def cria_tabela_vendas_mensal(dados):
    vendas_mensal = pd.DataFrame(dados.set_index('Data da Compra').groupby(pd.Grouper(freq='ME'))['Preço'].count()).reset_index()
    vendas_mensal['Ano'] = vendas_mensal['Data da Compra'].dt.year
    vendas_mensal['Mes'] = vendas_mensal['Data da Compra'].dt.month_name()
    return vendas_mensal

def cria_tabela_vendas_categoria(dados):
    vendas_categorias = pd.DataFrame(dados.groupby('Categoria do Produto')['Preço'].count().sort_values(ascending = False))
    return vendas_categorias

def cria_tabela_vendas_vendedores(dados):
    vendedores = pd.DataFrame(dados.groupby('Vendedor')['Preço'].agg(['sum', 'count']))
    return vendedores    
