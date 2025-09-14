# 15–16주차 Django 프로젝트 README (업로드 ZIP 기준)

이 문서는 **15~16주에 걸쳐 진행된 작업**을 기반으로, Django 프로젝트(`mysite`) 내용을 요약한 README입니다.

주요 앱: `polls`, `board`, `skn`, `java_src` (정적 파일은 `static/`).


## 폴더 구조(요약)

```
mysite/
  manage.py
  db.sqlite3 (개발용, 존재할 수 있음)
  mysite/   # 프로젝트 패키지(settings, urls, asgi, wsgi)
  polls/
  board/
  skn/
  java_src/
  static/
```

## 라우팅 개요 (`mysite/urls.py`)

아래는 프로젝트 라우트 정의의 핵심 라인입니다.

```python
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
    path('admin/', admin.site.urls),
    path('skn/', views.Hello),
    path('polls/', include('polls.urls')),
    path('javacript/', include('java_src.urls')),
    path('board/', include('board.urls'))
```
> 참고: `/javacript/` 경로는 오타일 가능성이 있습니다. (`javascript` 의도 확인 권장)


## 설정 핵심 (`mysite/settings.py`)

### INSTALLED_APPS

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'skn.apps.SknConfig',
    'polls.apps.PollsConfig',
    'java_src.apps.JavaSrcConfig',
    'board.apps.BoardConfig',
    'django_extensions',
]
```
### ALLOWED_HOSTS

```python
ALLOWED_HOSTS = ['*']
```
### DATABASES (민감정보 마스킹)

```python
DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
```
- 현재 저장소에 `db.sqlite3`(개발용 DB)가 포함되어 있습니다. 실제 운영 시에는 MySQL 등 외부 DB 사용 및 `.gitignore` 권장.


## 각 앱 개요 (간단)

- **polls/**: 튜토리얼성 설문/투표 예제 구조(views, models, urls, templates 등)

- **board/**: 게시판 관련 앱(views/forms/models/urls). 관리자 등록 및 템플릿 포함.

- **skn/**: 간단한 뷰 라우팅(`skn.views.Hello` 등) 확인됨.

- **java_src/**: 자바스크립트 관련 라우트/리소스 제공(경로명 확인 요망: `/javacript/`).


## 로컬 실행(개발용)

```bash
# 가상환경 권장
pip install django django-extensions mysqlclient

# 마이그레이션 및 슈퍼유저
python manage.py migrate
python manage.py createsuperuser

# 개발 서버
python manage.py runserver 0.0.0.0:8000
```

## 보안/운영 주의사항

- `ALLOWED_HOSTS=['*']`는 개발 편의 설정입니다. 운영에서는 서비스 도메인으로 제한하세요.

- `settings.py` 내 DB 계정/비밀번호는 **환경변수(.env) / Secret**로 분리 권장 (하드코딩 금지).

- `db.sqlite3`는 개발 편의용 DB입니다. 운영에서는 외부 DB 사용 및 커밋 제외 권장.


## 15~16주 작업 요약

- **Week 15**: Django 기본 앱 구성(polls/board/skn/java_src), 라우팅 및 템플릿 동작 확인.

- **Week 16**: 설정 보강, DB 연동 확인, 개발/운영 분리 검토 및 리팩터링 포인트 정리.
