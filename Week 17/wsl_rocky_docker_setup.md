# 🌐 WSL--Rocky 연결 & Docker 배포 정리

## 1️⃣ WSL ↔ Rocky 네트워크 확인 및 포트 포워딩

### 1-1) WSL 내부 IP 확인

``` bash
ip a  # WSL 내부 IP 확인
```

출력 예: `inet 172.20.119.59/20`\
이 IP를 포트 포워딩 대상으로 사용합니다.

### 1-2) Windows PowerShell(관리자 권한)에서 포트 포워딩 설정

``` powershell
netsh interface portproxy add v4tov4 ^
  listenaddress=0.0.0.0 listenport=8001 ^
  connectaddress=172.20.119.59 connectport=8001

# 등록 확인
netsh interface portproxy show all

# (필요 시 삭제)
netsh interface portproxy delete v4tov4 ^
  listenaddress=0.0.0.0 listenport=8001
```

### 1-3) WSL에서 서버 실행

``` bash
python manage.py runserver 0.0.0.0:8001
```

### 1-4) Rocky 서버에서 API 호출 테스트

``` bash
curl -i -X POST "http://192.168.0.5:8001/predict/" \
     -H "Content-Type: application/json" \
     -d '{"content":"배가 고파요"}'
```

✅ **목적**\
- WSL에서 실행한 Django 서버를 Rocky 서버에서도 접근 가능하게 만듦\
- Windows → WSL → Django로 트래픽 전달하여 개발/테스트 환경 통합

------------------------------------------------------------------------

## 2️⃣ Docker를 이용한 Django 서비스 배포

### 2-1) `requirements.txt`

``` text
Django
djangorestframework
transformers
gunicorn
torch==2.7.1
```

### 2-2) `Dockerfile`

``` dockerfile
FROM python:3.11.13-slim
WORKDIR /usr/src/app

RUN apt update && apt install gcc -y

COPY . /usr/src/app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["gunicorn", "--bind", "0:8001", "senti.wsgi:application"]
```

### 2-3) Docker 명령어

``` bash
# 1. 이미지 빌드
docker build -t model_serving:0.1 .

# 2. 컨테이너 실행
docker run -itd --name serving -p 8001:8001 model_serving:0.1

# 3. 컨테이너 내부 접속 (필요 시)
docker exec -it serving /bin/bash
```

✅ **결과**\
- `model_serving:0.1` 이미지 → 독립 실행 가능한 표준 패키지\
- `serving` 컨테이너 → 백그라운드 실행, 외부에서 `:8001/predict/` 접근
가능

------------------------------------------------------------------------

## 📌 최종 요약

1.  **포트포워딩 설정** → Windows 8001 → WSL 8001 → Django 개발 서버
    연결
2.  **Docker로 표준화** → 어디서든 동일한 환경으로 실행 가능
3.  **운영 가능 환경 구축** → `gunicorn` + 포트 매핑으로 실제 서비스
    가능
