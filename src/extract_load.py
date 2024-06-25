# Import 
import yfinance as yf 
from dotenv import load_dotenv
import os 

# import das variaveis de ambiente

commodities = ['CL=F', 'GC=F', 'SI=F']

def data_extract(symbol, period = '2y', interval = '1d'):
    ticker = yf.Ticker('CL=F')
    data = ticker.history(period = period, interval = interval)[['Close']]
    data['symbol'] = symbol
    return data



# pegar cotacao dos ativos

# concatenar os ativos (1..2..3) -> (1)


#  Salvar no banco de dados 