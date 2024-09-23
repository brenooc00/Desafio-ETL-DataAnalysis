import pandas as pd
from sqlalchemy import create_engine, Integer
from db_connection import get_connection
import logging

# Configuração básica do log
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_data_to_db(df, table_name, engine):
    #Carrega os dados transformados em uma tabela do banco de dados PostgreSQL.

    dtype = {
        'N_Fatura': Integer,
        'ID_Cliente': Integer,
        'Quantidade': Integer,
        'Horas': Integer,
        'Minutos': Integer,
        'Dia': Integer,
        'Mês': Integer,
        'Ano': Integer
    }

    try:
        # Carregar o DataFrame para a tabela do banco de dados
        df.to_sql(table_name, engine, if_exists='replace', index=False, dtype=dtype)
        logging.info(f"Tabela {table_name} carregada com sucesso.")
    except Exception as e:
        logging.error(f"Erro ao carregar a tabela {table_name}: {e}")



if __name__ == "__main__":
    
    '''
    # Conectar ao banco de dados
    engine = get_connection()

    # Carregar as tabelas transformadas (fato e dimensões)
    fact_sales = pd.read_csv('./data/transformed_fact_sales.csv')
    dim_customer = pd.read_csv('./data/transformed_dim_customer.csv')
    dim_product = pd.read_csv('./data/transformed_dim_product.csv')
    dim_date = pd.read_csv('./data/transformed_dim_date.csv')

    # Carregar cada DataFrame para o banco de dados PostgreSQL
    load_data_to_db(fact_sales, 'fact_sales', engine)
    load_data_to_db(dim_customer, 'dim_customer', engine)
    load_data_to_db(dim_product, 'dim_product', engine)
    load_data_to_db(dim_date, 'dim_date', engine)
'''