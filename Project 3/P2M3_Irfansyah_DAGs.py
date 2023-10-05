from datetime import datetime
import psycopg2 as db
from elasticsearch import Elasticsearch
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

import pandas as pd

def load_data():
    conn_string = "dbname='airflow' host='postgres' user='airflow' password='airflow'"
    conn = db.connect(conn_string)
    df = pd.read_sql("select * from table_M3", conn)
    df.to_csv('P2M3_Irfansyah_data_raw.csv',index=False)

def cleaning_data():
    dataframe = pd.read_csv('/opt/airflow/dags/P2M3_Irfansyah_data_raw.csv')
    # Mengganti nilai Gender
    dataframe['Gender'] = dataframe['Gender'].replace({'0':'male', '1':'female'})
    # Mengubah nama kolom menjadi lowercase
    dataframe.columns = [col.lower() for col in dataframe.columns]
    # Mengganti spasi dengan underscore pada nama kolom
    dataframe.columns = dataframe.columns.str.replace(' ', '_')
    # Menghapus koma atas nama kolom
    dataframe.columns = dataframe.columns.str.replace("'", '')

    dataframe.to_csv('/opt/airflow/dags/P2M3_Irfansyah_data_clean.csv', index=False)

def push_es ():
    es = Elasticsearch("http://elasticsearch:9200") # define elasticsearch ke variable
    df_cleaned=pd.read_csv('/opt/airflow/dags/P2M3_Irfansyah_data_clean.csv') # import csv clean
    for i,r in df_cleaned.iterrows(): # looping untuk masuk ke elastic search
        doc=r.to_json()
        res=es.index(index="data_cleaned", body=doc)
        print(res)  

default_args= {
    'owner': 'Irfan',
    'start_date': datetime(2023, 9, 29) }

with DAG(
    "Milestone3",
    description='Milestone3',
    schedule_interval='@yearly',
    default_args=default_args, 
    catchup=False) as dag:

    # Task 1
    load_data = PythonOperator(
        task_id='load_data',
        python_callable=load_data

    )

    # Task 2
    cleaning_data = PythonOperator(
        task_id='cleaning_data',
        python_callable=cleaning_data

    )

    #Task 3
    push_es = PythonOperator(
        task_id='push_es',
        python_callable=push_es

    )

    load_data >> cleaning_data >> push_es