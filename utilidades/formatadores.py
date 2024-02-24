def formata_numero(valor, prefixo=''):
    unidades = ['', 'mil', 'milhões'] 
    for unidade in unidades:
        if valor < 1000:
            return f'{prefixo} {valor:.2f} {unidade}'.strip() 
        valor /= 1000
    return f'{prefixo} {valor:.2f} bilhões'
