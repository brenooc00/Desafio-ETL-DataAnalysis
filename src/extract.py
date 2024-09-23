import pandas as pd
import os
import logging

# Configuração básica do log
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def extract_data(file_path):
    #Extrai os dados do arquivo Excel (.xlsx) e retorna um DataFrame.

    if not os.path.exists(file_path):
        logging.error(f"Arquivo {file_path} não encontrado.")
        raise FileNotFoundError(f"Arquivo {file_path} não encontrado.")
    
    try:
        # Leitura do arquivo Excel em um DataFrame
        df = pd.read_excel(file_path)
        print("Dados extraídos com sucesso!")
        logging.info("Dados extraídos com sucesso!")
        return df
    except Exception as e:
        logging.error(f"Erro ao extrair dados: {e}")
        raise


if __name__ == "__main__":
    '''
    # Caminho para o arquivo Excel
    file_path = "../data/raw/OnlineRetail.xlsx"
    
    # Chamada da função para extrair os dados
    data = extract_data(file_path)
    
    # Exibir as primeiras linhas para verificar se a extração foi bem-sucedida
    print(data.head())
    '''