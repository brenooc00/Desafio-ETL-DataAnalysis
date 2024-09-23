# Importar os módulos dos scripts criados
from extract import extract_data
from transform import transform_data
from load import load_data_to_db
from db_connection import get_connection
import logging

# Configuração básica do log
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def run_etl():
    #Executa o pipeline completo de ETL:
    #Extrai os dados do arquivo Excel.
    #Transforma os dados de acordo com a modelagem definida.
    #Carrega as tabelas transformadas no Data Warehouse (PostgreSQL).

    logging.info("Iniciando o processo de ETL...")

    # 1. Extração dos dados
    file_path = "./data/raw/OnlineRetail.xlsx"
    logging.info("Extraindo os dados...")
    raw_data = extract_data(file_path)

    # 2. Transformação dos dados
    logging.info("Transformando os dados...")
    fact_sales, dim_customer, dim_product, dim_date = transform_data(raw_data)

    # 3. Conexão ao banco de dados
    logging.info("Conectando ao banco de dados...")
    engine = get_connection()

    # 4. Carga dos dados no Data Warehouse
    logging.info("Carregando as tabelas no Data Warehouse...")

    load_data_to_db(fact_sales, 'fact_sales', engine)
    load_data_to_db(dim_customer, 'dim_customer', engine)
    load_data_to_db(dim_product, 'dim_product', engine)
    load_data_to_db(dim_date, 'dim_date', engine)

    logging.info("Processo de ETL concluído com sucesso!")

if __name__ == "__main__":
    run_etl()
