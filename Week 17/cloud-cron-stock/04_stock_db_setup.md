# 💾 MySQL DB & 테이블 생성

```python
import pymysql

con = pymysql.connect(host="10.0.0.10", user='',
                      password='', port=3306)
cursor = con.cursor()

# 데이터베이스 생성
cursor.execute("CREATE DATABASE stock;")

# 테이블 생성
sql = """
CREATE TABLE stock.stock_min (
    stock_code               VARCHAR(30),
    localDateTime            CHAR(14),
    currentPrice             FLOAT,
    openPrice                FLOAT,
    highPrice                FLOAT,
    lowPrice                 FLOAT,
    accumulatedTradingVolume BIGINT,
    PRIMARY KEY (stock_code, localDateTime)
)
"""
cursor.execute(sql)
cursor.close()
con.close()
```

## Crontab 등록 (운영용)
```bash
crontab -e
```
등록 라인 (주중 9~16시 매분 실행):
```
*/1 9-16 * * 1-5 /home/ec2-user/workspace/batch.sh
```
