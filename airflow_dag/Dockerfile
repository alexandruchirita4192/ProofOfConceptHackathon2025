FROM apache/airflow:2.5.0
USER root
RUN pip install pandas sqlalchemy pyodbc joblib scikit-learn
COPY airflow_dag /opt/airflow/dags/
USER airflow
