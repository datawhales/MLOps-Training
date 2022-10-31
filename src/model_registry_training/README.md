# Model Registry Training
- ML 모델을 서비스에 이용하기 위해 저장하는 방법을 알아보고 연습합니다.
- Model Registry 서버를 직접 띄워보고 모델을 저장해봅니다.

## Quick Start
**0. Setup**  
- `python==3.8.13` 버전을 이용하여 가상 환경을 구축합니다.
- 필요한 라이브러리를 다음의 명령어를 이용하여 설치합니다.
```console
$ pip install -r requirements.txt
```

## Steps
1. Run MLFlow Server Container (docker)
2. Get Data from DB (python)
3. Train Model (python)
4. Save Model to MLFlow Server (python)
5. Download Model from MLFlow Server and Load Model (python)
