# ⏰ Cron 서비스 설정 & 자동화 스크립트 실행

## 1️⃣ cron 서비스 설치 & 활성화
```bash
sudo yum install cronie -y
sudo systemctl status crond
sudo systemctl enable --now crond
```

## 2️⃣ 작업 디렉토리로 이동
```bash
cd ~/workspace
```

## 3️⃣ Python 테스트 스크립트 작성 & 실행
```python
# test.py
with open("./a.txt", "w") as f:
    f.write("Hi")
```

```bash
python test.py
cat a.txt  # "Hi" 출력 확인
```

## 4️⃣ 셸 스크립트 작성 & 테스트
```bash
# test.sh
#!/bin/bash
/home/ec2-user/miniconda3/bin/python /home/ec2-user/workspace/test.py

chmod +x ./test.sh
rm a.txt
./test.sh  # a.txt 생성 확인
```

## 5️⃣ crontab 등록
```bash
crontab -e
```

등록할 라인:
```
45 * * * * /home/ec2-user/workspace/test.sh
```
