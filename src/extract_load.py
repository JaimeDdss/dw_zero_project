# Imports 
import yfinance as yf 
from dotenv import load_dotenv
from sqlalchemy import create_engine
import pandas as pd
import os 

load_dotenv()

# setting environment variables
DB_HOST = os.getenv('DB_HOST_PROD')
DB_PORT = os.getenv('DB_PORT_PROD')
DB_NAME = os.getenv('DB_NAME_PROD')
DB_USER = os.getenv('DB_USER_PROD')
DB_PASS = os.getenv('DB_PASS_PROD')
DB_SCHEMA = os.getenv('DB_SCHEMA_PROD')

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine (DATABASE_URL)

# ore type codes
commodities = ['CL=F', 'GC=F', 'SI=F']

# extracting data
def data_extract(symbol, period = '2y', interval = '1d'):
    ticker = yf.Ticker(symbol)
    data = ticker.history(period = period, interval = interval)[['Close']]
    data['symbol'] = symbol
    return data

# Concat data and transforming into a pandas df
def concatenar_dados(commodities):
    todos_dados = []
    for symbol in commodities:
        dados = data_extract(symbol)
        todos_dados.append(dados)
    return pd.concat(todos_dados)

# save into a PostgreSQL database on Render
def save_postgres(df, schema= 'public'):
    df.to_sql('commodities', engine , if_exists='replace',
               index=True, index_label='Date',schema= schema)



def main():
    dados_concatenados = concatenar_dados(commodities)
    save_postgres(dados_concatenados, schema='public')

if __name__ == "__main__":
    main()