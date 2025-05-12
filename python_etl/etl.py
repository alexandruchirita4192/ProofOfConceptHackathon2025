# ETL Prototype (Python)

import pandas as pd
from sqlalchemy import create_engine

# Mock source data and transform
df = pd.DataFrame({'id':[1,2,3],'value':[10,20,30]})
df.to_csv('source.csv', index=False)

df = pd.read_csv('source.csv')
df['value_transformed'] = df['value'] * 2

# Load into SQL Server
conn = 'mssql+pyodbc://sa:YourPass@localhost/PoC_DB?driver=ODBC+Driver+17+for+SQL+Server'
engine = create_engine(conn)
df.to_sql('etl_table', engine, if_exists='replace', index=False)
print("ETL load complete.")
