# -*- coding: utf-8 -*-
"""
stock_crawler.py
평일 15:30(KST) 에 KRX 수집 -> NAVER 주식 수집 순으로 실행하는 DAG 골격
참고: DB 접속정보는 환경변수 또는 Airflow Connection 사용 권장
"""
from __future__ import annotations

import os
import logging
from datetime import datetime, timedelta
from pendulum import timezone

import requests
import pandas as pd
from sqlalchemy import create_engine

from airflow import DAG
from airflow.operators.python import PythonOperator

KST = timezone("Asia/Seoul")

# ---- DB 접속정보: 환경변수 사용 (권장) ----
# 예) export STOCK_DB_URI='mysql+pymysql://user:pw@10.0.0.9:3306/stock'
STOCK_DB_URI = os.getenv("STOCK_DB_URI")  # 없으면 None
ENGINE = create_engine(STOCK_DB_URI) if STOCK_DB_URI else None

def get_krx(**context):
    """
    TODO: KRX 수집 로직 구현 자리.
    - 예: OpenAPI/FTP/크롤링 등으로 일자별 종목/지수 메타 수집
    - 여기서는 골격만 제공 (로깅으로 대체)
    """
    logging.info("[get_krx] KRX 수집 시작")
    # 예시: df = pd.DataFrame(...)
    # context['ti'].xcom_push(key='krx_df', value=df.to_json(orient="records"))
    logging.info("[get_krx] KRX 수집 완료(placeholder)")

def get_naver(**context):
    """
    NAVER 주식 데이터 수집 예시(골격).
    - 실제 운영 시: 종목코드 리스트를 KRX 태스크/XCom/DB에서 받아 순회 처리
    - 여기서는 샘플로 005930 1개만 요청
    """
    logging.info("[get_naver] NAVER 수집 시작")
    code = "005930"
    target_time = (datetime.now() - timedelta(minutes=1)).strftime("%Y%m%d%H%M")
    url = f"https://api.stock.naver.com/chart/domestic/item/{code}/minute?startDateTime={target_time}&endDateTime={target_time}"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"
    }
    try:
        r = requests.get(url, headers=headers, timeout=10)
        r.raise_for_status()
        payload = r.json()
        if not payload:
            logging.warning("[get_naver] 응답 비어있음")
            return

        rec = payload[0]
        row = {
            "stock_code": code,
            "localDateTime": rec.get("localDateTime"),
            "currentPrice": rec.get("currentPrice"),
            "openPrice": rec.get("openPrice"),
            "highPrice": rec.get("highPrice"),
            "lowPrice": rec.get("lowPrice"),
            "accumulatedTradingVolume": rec.get("accumulatedTradingVolume"),
        }
        logging.info(f"[get_naver] row={row}")

        if ENGINE is None:
            logging.warning("[get_naver] ENGINE 미설정. DB 저장 생략")
            return

        import pymysql  # ensure driver available
        with ENGINE.begin() as conn:
            conn.execute(
                """
                INSERT INTO stock.stock_min
                (stock_code, localDateTime, currentPrice, openPrice, highPrice, lowPrice, accumulatedTradingVolume)
                VALUES (%(stock_code)s, %(localDateTime)s, %(currentPrice)s, %(openPrice)s, %(highPrice)s, %(lowPrice)s, %(accumulatedTradingVolume)s)
                """,
                row,
            )
        logging.info("[get_naver] DB insert 완료")
    except Exception as e:
        logging.exception(f"[get_naver] 오류: {e}")

with DAG(
    dag_id="stock_crawler",
    description="stock 수집",
    start_date=datetime(2025, 9, 11, tzinfo=KST),
    schedule_interval="30 15 * * 1-5",  # 평일 15:30
    catchup=False,
    tags=["stock", "naver", "krx"],
    default_args={
        "owner": "airflow",
        "retries": 0,
    },
) as dag:
    t1 = PythonOperator(
        task_id="krx",
        python_callable=get_krx,
    )

    t2 = PythonOperator(
        task_id="naver_stock",
        python_callable=get_naver,
    )

    t1 >> t2