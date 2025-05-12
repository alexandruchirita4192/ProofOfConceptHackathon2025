# Streamlit UI (Python)
import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

conn = 'mssql+pyodbc://sa:YourPass@localhost/PoC_DB?driver=ODBC+Driver+17+for+SQL+Server'
engine = create_engine(conn)

st.title('Sample ETL Report')
min_id = st.number_input('Minimum ID', min_value=1, value=1)

df = pd.read_sql(f"SELECT * FROM etl_table WHERE id >= {min_id}", engine)
st.dataframe(df)
