import pandas as pd
from sqlalchemy import create_engine

def get_connection():
    
    USER = 'postgres'
    PASSWORD = 'developer123'
    HOST = 'localhost'
    PORT = '5432'
    DATABASE = 'db_Kyros'

    connection_string = f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'
    engine = create_engine(connection_string)
    return engine
