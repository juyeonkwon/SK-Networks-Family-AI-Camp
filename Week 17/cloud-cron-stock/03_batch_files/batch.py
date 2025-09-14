import os
import requests
from datetime import datetime, timedelta
import pymysql

# DB 연결
con = pymysql.connect(host="10.0.0.10", user='',
                      password='', port=3306)
cursor = con.cursor()

# 1분 전 시점
now_time = (datetime.now() - timedelta(minutes=1)).strftime("%Y%m%d%H%M")

# API 요청
head = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
url = f"https://api.stock.naver.com/chart/domestic/item/005930/minute?startDateTime={now_time}&endDateTime={now_time}"
r = requests.get(url, headers=head)

# DB insert
insert_sql = "INSERT INTO stock.stock_min VALUES (%s, %s, %s, %s, %s, %s, %s)"
try:
    data = r.json()[0]
    cursor.execute(insert_sql, [
        '005930',
        data['localDateTime'],
        data['currentPrice'],
        data['openPrice'],
        data['highPrice'],
        data['lowPrice'],
        data['accumulatedTradingVolume']
    ])
    con.commit()
except Exception as e:
    print("Error inserting:", e)
finally:
    cursor.close()
    con.close()
