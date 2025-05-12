# Integrated ETL & ML Pipeline (Airflow)
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from sqlalchemy import create_engine
from airflow.operators.email import EmailOperator
from airflow.providers.slack.operators.slack_webhook import SlackWebhookOperator
import pandas as pd
import joblib

# Connection string
conn = 'mssql+pyodbc://sa:YourPass@localhost/PoC_DB?driver=ODBC+Driver+17+for+SQL+Server'

def run_etl():
    engine = create_engine(conn)
    df = pd.read_csv('source.csv')
    df['value_transformed'] = df['value'] * 2
    df.to_sql('etl_table', engine, if_exists='replace', index=False)


def predict_failure():
    engine = create_engine(conn)
    df = pd.read_sql(
        'SELECT TOP 1 CPU AS cpu, FreeMemory AS memory_free, DATEDIFF(second, Timestamp, GETDATE()) AS duration_seconds FROM HealthMetrics ORDER BY Timestamp DESC',
        engine
    )
    model = joblib.load('/path/to/failure_predictor.joblib')
    prediction = model.predict(df)[0]
    failed = int(prediction)
    engine.execute(
        "INSERT INTO batch_logs (cpu, memory_free, duration_seconds, failed) VALUES (?, ?, ?, ?)",
        df.at[0,'cpu'], df.at[0,'memory_free'], df.at[0,'duration_seconds'], failed
    )

# define alert tasks
def on_failure_callback(context):
    return SlackWebhookOperator(
        task_id='slack_notify',
        http_conn_id='slack_connection',
        message=f"Task {context['task_instance'].task_id} failed!",
    ).execute(context=context)

with DAG('etl_ml_pipeline', start_date=datetime(2025,5,1), schedule_interval='@hourly', catchup=False, default_args={'on_failure_callback': on_failure_callback}) as dag:
    etl_task = PythonOperator(task_id='run_etl', python_callable=run_etl)
    predict_task = PythonOperator(task_id='predict_failure', python_callable=predict_failure)
    alert_email = EmailOperator(
        task_id='email_notify',
        to='team@example.com',
        subject='Airflow Task Failure',
        html_content='A task has failed. Check the Airflow UI for details.'
    )
    etl_task >> predict_task >> alert_email
