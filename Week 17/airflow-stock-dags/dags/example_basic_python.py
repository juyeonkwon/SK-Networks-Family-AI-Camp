# -*- coding: utf-8 -*-
"""
example_basic_python.py
매일 09:00(KST) 에 두 개의 Python 태스크를 순차 실행하는 Airflow 예제 DAG
"""
from datetime import datetime
from pendulum import timezone
from airflow import DAG
from airflow.operators.python import PythonOperator

KST = timezone("Asia/Seoul")

def hello_world():
    print("Hello, Airflow!")

def print_date(execution_date=None, **context):
    print(f"Execution date: {execution_date}")

with DAG(
    dag_id="example_basic_python",
    description="A simple DAG with two Python tasks",
    start_date=datetime(2023, 1, 1, tzinfo=KST),
    schedule_interval="0 9 * * *",  # 매일 09:00 KST
    catchup=False,
    tags=["example", "basic"],
    default_args={
        "owner": "airflow",
        "retries": 0,
    },
) as dag:
    t1 = PythonOperator(
        task_id="hello_world",
        python_callable=hello_world,
    )

    t2 = PythonOperator(
        task_id="print_date",
        python_callable=print_date,
    )

    t1 >> t2