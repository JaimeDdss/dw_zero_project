# Import 
import yfinance as yf 
from dotenv import load_dotenv
import pandas as pd
import os 

# import das variaveis de ambiente

commodities = ['CL=F', 'GC=F', 'SI=F']

def data_extract(symbol, period = '2y', interval = '1d'):
    ticker = yf.Ticker('CL=F')
    data = ticker.history(period = period, interval = interval)[['Close']]
    data['symbol'] = symbol
    return data

def concatenar_dados(commodities):
    todos_dados = []
    for symbol in commodities:
        dados = data_extract(symbol)
        todos_dados.append(dados)
    return pd.concat(todos_dados)


if __name__ == '__main__':
    dados_concatenados = concatenar_dados(commodities)
    print(dados_concatenados)



# concatenar os ativos (1..2..3) -> (1)


#  Salvar no banco de dados 