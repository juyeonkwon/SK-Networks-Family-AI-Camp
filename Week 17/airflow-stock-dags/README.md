# Apache Airflow DAGs — Stock Crawler

## 구조
```
dags/
  ├─ example_basic_python.py  # 매일 09:00 두 태스크 순차 실행
  └─ stock_crawler.py         # 평일 15:30 KRX -> NAVER 수집
requirements.txt              # 워커/이미지에 필요한 패키지
```

## 배치
1) 패키지 설치 (워커/이미지)
```bash
pip install -r requirements.txt
```

2) DB 연결정보 설정
- 환경변수 권장:
  ```bash
  export STOCK_DB_URI='mysql+pymysql://USER:PW@10.0.0.9:3306/stock'
  ```
  (systemd/env file/Composer image env 로 주입 가능)

3) DAG 배치
- 위 `dags/` 폴더의 파일을 `$AIRFLOW_HOME/dags/` 로 복사
- 예: `/opt/airflow/dags/`

4) 시간대 설정
- 코드에서 `pendulum.timezone("Asia/Seoul")` 사용
- 필요시 Airflow 설정: `core.default_timezone = Asia/Seoul`

5) 스케줄
- `example_basic_python`: `0 9 * * *`
- `stock_crawler`: `30 15 * * 1-5`

## 참고
- 운영에서는 Airflow Connection(MySQL) 사용 권장.
- 외부 API 요청 실패 대비: 재시도/타임아웃/에러 로깅 구성 필요.