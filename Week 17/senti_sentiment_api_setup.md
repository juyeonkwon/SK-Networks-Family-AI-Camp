# 📝 Senti Sentiment API Setup (WSL)

## 🎯 목표

-   WSL에서 Django 프로젝트(`senti`)에 한국어 감성분석
    엔드포인트(`/predict/`) 추가
-   Hugging Face 파이프라인(KC-ELECTRA) + Django REST Framework로 JSON
    응답

------------------------------------------------------------------------

## 1️⃣ 네트워크 체크

``` bash
ping 192.168.56.10
ipconfig  # 윈도우에서 IP 확인
```

------------------------------------------------------------------------

## 2️⃣ 환경 준비

``` bash
conda activate torch
pip install django djangorestframework transformers accelerate
```

------------------------------------------------------------------------

## 3️⃣ Django 프로젝트 & 앱 생성

``` bash
django-admin startproject senti
cd senti
python manage.py startapp serving
```

### `senti/settings.py`

``` python
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'rest_framework',
    'serving',
]
```

### `senti/urls.py`

``` python
from django.urls import path
from serving import views

urlpatterns = [
    path('predict/', views.predict),
]
```

### `serving/views.py`

``` python
from rest_framework.decorators import api_view
from rest_framework.response import Response
from transformers import pipeline

pipe = pipeline("text-classification",
                model="nlp04/korean_sentiment_analysis_kcelectra")

@api_view(['POST'])
def predict(request):
    text = request.data.get('content') or ""
    result = pipe(text)[0]
    return Response(result)
```

------------------------------------------------------------------------

## 4️⃣ 실행 & 테스트

``` bash
python manage.py runserver 0.0.0.0:8000
```

``` bash
curl -X POST http://127.0.0.1:8000/predict/ \
     -H "Content-Type: application/json" \
     -d '{"content":"토스해달라고"}'
```

------------------------------------------------------------------------

## 5️⃣ (옵션) DB 연결 확인

``` python
import pymysql
conn = pymysql.connect(host='192.168.0.30', user='django',
                       password='', database='mydjango', port=3306)
cur = conn.cursor()
cur.execute("SELECT * FROM board_question")
rows = cur.fetchall()
conn.close()
```

------------------------------------------------------------------------

## ✅ 학습 포인트

-   Django settings 환경 분리 & DRF 라우팅
-   Hugging Face pipeline으로 간단한 API 구성
-   WSL ↔ Rocky 서버 네트워크 연결 확인
-   MySQL 연결 & ORM/Raw SQL 테스트
