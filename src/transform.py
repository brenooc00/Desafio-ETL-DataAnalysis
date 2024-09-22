import pandas as pd

def clean_data(df):
    #Realiza a limpeza básica dos dados, incluindo:
    #Remoção de linhas com valores ausentes para 'CustomerID'.
    #Remoção de registros com quantidades negativas.
    #Formatação da coluna 'InvoiceDate' para datetime.

    #Remover linhas onde 'CustomerID' é nulo
    df_cleaned = df.dropna(subset=['CustomerID'])

    #Remover registros com Quantidade negativa
    df_cleaned = df_cleaned[df_cleaned['Quantity'] > 0]

    #Remover registros com preço unitário igual ou menor que zero
    df_cleaned = df_cleaned[df_cleaned['UnitPrice'] > 0]

    # Converter 'InvoiceDate' para datetime
    df_cleaned['InvoiceDate'] = pd.to_datetime(df_cleaned['InvoiceDate'])

    # Mudar nome das colunas
    df_cleaned = df_cleaned.rename(columns={'CustomerID': 'ID_Cliente', 'InvoiceNo': 'N_Fatura', 'Quantity': 'Quantidade', 'UnitPrice': 'Preço unitário','Country': 'País', 'StockCode': 'ID_Stock', 'InvoiceDate': 'Data Fatura', 'Description': 'Descrição'})

    return df_cleaned

def create_fact_table(df):
    #Cria a tabela fato de vendas, agrupando os dados por InvoiceNo, StockCode e CustomerID.
    fact_sales = df[['ID_Cliente', 'N_Fatura', 'ID_Stock', 'Quantidade', 'Preço unitário']]
    fact_sales['Data'] = df['Data Fatura'].dt.date
    fact_sales['Horário'] = pd.to_datetime(df['Data Fatura']).dt.time

    # Calcular as métricas de vendas
    fact_sales['Faturamento'] = (fact_sales['Quantidade'] * fact_sales['Preço unitário']).round(3)

    return fact_sales

def create_dimension_tables(df):
    #Cria as tabelas de dimensão (Dimensão de Cliente, Produto e Tempo).

    #Tabela Dimensão Cliente
    dim_customer = df[['ID_Cliente', 'País']].drop_duplicates()
    #.set_index('ID_Cliente')

    # Tabela Dimensão Produto
    dim_product = df[['ID_Stock', 'Descrição']].drop_duplicates()
    #.set_index('ID_Stock')

    # Tabela Dimensão Data
    # Criar tabela dimensão (dim_date)
    dim_date = df[['Data Fatura']].drop_duplicates()
    dim_date['Data'] = dim_date['Data Fatura'].dt.date
    dim_date['Horário'] = pd.to_datetime(dim_date['Data Fatura']).dt.time
    dim_date['Horas'] = dim_date['Data Fatura'].dt.hour  # Adicionando a coluna de horas
    dim_date['Dia'] = dim_date['Data Fatura'].dt.day # Adicionando a coluna de dia
    dim_date['Mês'] = dim_date['Data Fatura'].dt.month # Adicionando a coluna de mês
    dim_date['Ano'] = dim_date['Data Fatura'].dt.year # Adicionando a coluna de ano
    dim_date = dim_date[['Data', 'Horário', 'Horas', 'Dia', 'Mês', 'Ano']].drop_duplicates()


    return dim_customer, dim_product, dim_date

def transform_data(df):
    #Transformação dos dados
    #Criação da tabela fato
    #Criação das tabelas de dimensão

    # Limpeza dos dados
    df_cleaned = clean_data(df)

    # Criação das tabelas de dimensão
    dim_customer, dim_product, dim_date = create_dimension_tables(df_cleaned)

    # Criação da tabela fato
    fact_sales = create_fact_table(df_cleaned)

    return fact_sales, dim_customer, dim_product, dim_date

if __name__ == "__main__":
    
    '''
    file_path = './data/raw/OnlineRetail.xlsx'
    df = pd.read_excel(file_path)

    # Transformar os dados
    fact_sales, dim_customer, dim_product, dim_date = transform_data(df)

    # Exibir algumas informações transformadas
    print("Tabela Fato (Vendas):")
    print(fact_sales.head())
    
    print("\nTabela Dimensão (Clientes):")
    print(dim_customer.head())
    
    print("\nTabela Dimensão (Produtos):")
    print(dim_product.head())
    
    print("\nTabela Dimensão (Datas):")
    print(dim_date.head())

    # Salvar os dados transformados (opcional)
    fact_sales.to_csv('./data/transformed_fact_sales.csv', index=False)
    dim_customer.to_csv('./data/transformed_dim_customer.csv')
    dim_product.to_csv('./data/transformed_dim_product.csv')
    dim_date.to_csv('./data/transformed_dim_date.csv')
    '''