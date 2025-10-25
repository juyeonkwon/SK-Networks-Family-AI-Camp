## 🧠 AI Bootcamp Weekly Practice Log
Daily logs from SK Networks Family AI Camp

### 📅 Duration
**2025.05 \~ 진행 중**

---

### 🧾 Overview
본 레포지토리는 AI 부트캠프 과정에서 수행한 실습 및 팀 프로젝트 내용을 주차별로 정리한 기록입니다.  
데이터 수집 → 전처리 → 모델링 → 평가 → 배포까지 전 과정을 실습하며, 아래 기술을 중심으로 학습했습니다.

* **Python, Pandas, NumPy, Matplotlib, Scikit-learn**
* **PyTorch, TensorFlow**
* **LLM 활용, Chatbot/Agent 설계**
* **데이터 시각화 및 웹 배포(Streamlit)**
* *(추가)* **Django, MySQL, Docker/Nginx/Gunicorn, Cron, Apache Airflow, CLIP(멀티모달), QLoRA/PEFT, MCP(Server/Client), uv 패키징, PostgreSQL(pgvector), GAN/확산(Stable Diffusion·DDPM·UNet), Vision Transformer, LangGraph, Midjourney**

---

### 📚 Weekly Log

| 주차          | 주제/프로젝트                                       | 주요 내용                                                                                                      | 링크 |
| ------------- | ---------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | ---- |
| Week 01       | Python 기초 & 웹 크롤링                              | 변수/반복문/함수, 파일처리, BeautifulSoup 크롤링 실습                                                          | [Week 1](https://github.com/juyeonkwon/SK-Networks-Family-AI-Camp/tree/814e1665c4da47dac884b6139d2d75987f1c5f5a/Week%201) |
| Week 02       | 로깅/예외/DB/시각화 전과정 구현                       | logging, 예외처리, MySQL 연동, matplotlib/Streamlit, 전체 파이프라인                                           | [Week 2](https://github.com/juyeonkwon/SK-Networks-Family-AI-Camp/tree/1b171da2122f1cc75318da3ad6e01afc6fe869ff/Week%202) |
| Week 03       | **1차 프로젝트: 전국 자동차 등록 시각화**             | 데이터 정제, ERD, MySQL 적재, 시각화 구조 설계, 회고                                                            | [Week 3](https://github.com/juyeonkwon/SK-Networks-Family-AI-Camp/tree/1b171da2122f1cc75318da3ad6e01afc6fe869ff/Week%203) |
| Week 04       | 회귀/분류                                            | 선형/로지스틱 회귀, 분류/평가지표, ML 구조화                                                                    | [Week 4](https://github.com/juyeonkwon/SK-Networks-Family-AI-Camp/tree/1b171da2122f1cc75318da3ad6e01afc6fe869ff/Week%204) |
| Week 05       | Decision Tree/앙상블, ML 워크플로우                   | 트리/앙상블, 하이퍼파라미터, 실전 ML 프로젝트 흐름                                                              | [Week 5](https://github.com/juyeonkwon/SK-Networks-Family-AI-Camp/tree/1b171da2122f1cc75318da3ad6e01afc6fe869ff/Week%205) |
| Week 06       | 딥러닝 기초                                           | train/test 분할, 손실/Optimizer, 에폭/배치, PyTorch 코드 구조                                                   | [Week 6](https://github.com/juyeonkwon/SK-Networks-Family-AI-Camp/tree/1b171da2122f1cc75318da3ad6e01afc6fe869ff/Week%206) |
| Week 07       | 딥러닝 실전 & API 연동                                | PyTorch MLP/CNN, 데이터 증강, FastAPI/Streamlit, 서비스화                                                       | [Week 7](https://github.com/juyeonkwon/SK-Networks-Family-AI-Camp/tree/1b171da2122f1cc75318da3ad6e01afc6fe869ff/Week%207) |
| Week 08       | Faster R-CNN, 감정 분류, 정규식                        | Object Detection, 텍스트 분류 실전, re 모듈 실습                                                                 | [Week 8](https://github.com/juyeonkwon/SK-Networks-Family-AI-Camp/tree/1b171da2122f1cc75318da3ad6e01afc6fe869ff/Week%208) |
| Week 09       | LLM 개념 및 응용 (OpenAI, 챗봇 실습 시작)             | LLM 기본, OpenAI API, 챗봇 구조, 프롬프트 엔지니어링                                                            | [Week 9](https://github.com/juyeonkwon/SK-Networks-Family-AI-Camp/tree/1b171da2122f1cc75318da3ad6e01afc6fe869ff/Week%209) |
| Week 10       | LLM 실전 ①: 텍스트 생성·요약/질의응답                 | 자연어 생성, 텍스트 요약/문서 QA, 미니 프로젝트                                                                  | [Week 10](https://github.com/juyeonkwon/SK-Networks-Family-AI-Camp/tree/1b171da2122f1cc75318da3ad6e01afc6fe869ff/Week%2010) |
| Week 11       | LLM 실전 ②: LangChain·RAG                             | LangChain, RAG 기반 문서검색, Retrieval-Augmented Generation                                                     | [Week 11](https://github.com/juyeonkwon/SK-Networks-Family-AI-Camp/tree/1b171da2122f1cc75318da3ad6e01afc6fe869ff/Week%2011) |
| Week 12       | LLM 실전 ③: 생성형 AI 서비스, 오픈소스 LLM 적용        | Ollama, open-llm, 챗봇 배포, 생성형 서비스 기획                                                                  | [Week 12](https://github.com/juyeonkwon/SK-Networks-Family-AI-Camp/tree/1b171da2122f1cc75318da3ad6e01afc6fe869ff/Week%2012) |
| Week 13   | 멀티모달·경량화·MCP 실습                           | CLIP zero-shot · VAE/이상탐지 · QLoRA/PEFT · MCP(Server/Client) | [Week 13](https://github.com/juyeonkwon/SK-Networks-Family-AI-Camp/tree/1b171da2122f1cc75318da3ad6e01afc6fe869ff/Week%2013) |
| Week 14   | 생성형 AI & 에이전트 심화                          | GAN·Stable Diffusion(DDPM/UNet) · ViT · LangChain/LangGraph(메모리/페르소나) | [Week 14](https://github.com/juyeonkwon/SK-Networks-Family-AI-Camp/tree/1b171da2122f1cc75318da3ad6e01afc6fe869ff/Week%2014) |
| Week 15–16| Django 서비스 + ETL 파이프라인(운영화 기초)        | Django 감성분석 API · WSL↔Rocky 포워딩 · Cron ETL · Airflow 스캐폴드 | [Week 15-16](https://github.com/juyeonkwon/SK-Networks-Family-AI-Camp/tree/d650e9e6a7557626fa6bb354eba431d55fdde2df/Week%2015-16) |
| Week 17   | Cron ETL & Airflow DAGs 정리                       | Cron 분봉→MySQL · `stock_min` 스키마 · Airflow DAGs 정리 | [Week 17](https://github.com/juyeonkwon/SK-Networks-Family-AI-Camp/tree/main/Week%2017) |

  
> ✅ 각 주차별 실습은 Jupyter Notebook/코드/문서로 정리되어 있으며, 주석과 시각화 중심의 학습 자료입니다.

---

### 🚀 Semi Project
* 📌 **전국 자동차 등록 현황 시각화 시스템**  
  전국 자동차 등록 통계 데이터를 수집·정제하여, 지역·차종·연료별 트렌드를 분석 및 시각화하는 웹 시스템 구현  
  → 🔗 [프로젝트 레포](https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN15-1st-6TEAM)

* 📌 **FootTrade - 축구선수 이적 예측 시스템**  
  선수의 통계, 경기력 데이터를 기반으로 이적 가능성을 예측하는 모델 구현 및 Streamlit 앱 배포  
  → 🔗 [프로젝트 레포](https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN15-2nd-3Team)

* 📌 **취업하JOB — 구직 추천 + 자소서 자동 생성 팀 프로젝트**  
  공고 수집 → 스펙 파싱 → 매칭 → LLM 자소서 생성·평가 → 산출물 제출  
  → 🔗 [프로젝트 레포](https://github.com/SKNETWORKS-FAMILY-AICAMP/skn15-3rd-2team)

* 📌 **취업하JOB — 구직 추천 + 자소서 자동 생성 팀 프로젝트(Django)**  
  구직자 스펙 입력 → 채용공고 크롤링 및 매칭 → 기업 인재상 기반 자소서 초안 생성 → LLM 기반 피드백·첨삭 루프 → Django 웹 UI 결과 시각화  
  → 🔗 [프로젝트 레포](https://github.com/SKNETWORKS-FAMILY-AICAMP/skn15-4rd-2team)

* 📌 **ASSEMBLE — 한샘 인테리어 맞춤 설계 AI 시스템**  
  한샘 시공사례 데이터셋 구축 → 텍스트·이미지 매핑 → 공간·스타일·예산 코드 기반 SLLM 파인튜닝 → Diffusion 모델 파인튜닝으로 이미지 생성·보정 → AWS 기반 웹 서비스 통합  
  → 🔗 [프로젝트 레포](https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN15-FINAL-4TEAM)
