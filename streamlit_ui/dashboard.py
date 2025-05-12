# streamlit_ui/dashboard.py
import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(conn)
st.title('PoC Analytics Dashboard')

# Plot historical CPU usage
cpu = pd.read_sql('SELECT Timestamp, CPU FROM HealthMetrics', engine)
st.line_chart(cpu.set_index('Timestamp'))

# Show recent failure predictions
logs = pd.read_sql('SELECT TOP 20 * FROM batch_logs ORDER BY duration_seconds DESC', engine)
st.dataframe(logs)
