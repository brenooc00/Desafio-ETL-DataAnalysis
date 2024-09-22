-- Criação da tabela Fato (Vendas)
CREATE TABLE fact_sales (
    InvoiceNo VARCHAR(10),
    StockCode VARCHAR(20),
    Quantity INTEGER,
    InvoiceDate TIMESTAMP,
    CustomerID INTEGER,
    TotalSales INTEGER
);

-- Criação da Tabela Dimensão de Cliente
CREATE TABLE dim_customer (
    CustomerID INTEGER PRIMARY KEY,
    Country VARCHAR(100)
);

-- Criação da Tabela Dimensão de Produto
CREATE TABLE dim_product (
    StockCode VARCHAR(20) PRIMARY KEY,
    Description VARCHAR(255)
);

-- Criação da Tabela Dimensão de Data
CREATE TABLE dim_date (
    InvoiceDate TIMESTAMP PRIMARY KEY,
    Year INTEGER,
    Month INTEGER,
    Day INTEGER,
    Weekday INTEGER
);
