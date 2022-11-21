# Model Registry Training
- ML 모델을 서비스에 이용하기 위해 저장하는 방법을 알아보고 연습합니다.
- Model Registry 서버를 직접 띄워보고 모델을 저장해봅니다.
<br>

## Quick Start
**0. Setup**  
- `python==3.9.15` 버전을 이용하여 가상 환경을 구축합니다.
- 필요한 라이브러리를 다음의 명령어를 이용하여 설치합니다.
```console
$ pip install -r requirements.txt
```
<br>

**1. Run MLFlow Server**
- 다음의 명령어를 terminal 에 입력하여 mlflow server 를 실행합니다.
```console
$ mlflow server
```
- http://127.0.0.1:5000 에 접속하여 MLFlow UI Website 에 잘 접속되는지 확인합니다.
<br>

**2. Setup Experiment**
- `create_experiment.py` 를 실행하여 experiment 를 생성하고 website 에 잘 나타나는지 확인합니다.
```console
$ python create_experiment.py
```
- `create_run.py` 를 실행하여 run 을 생성하고 website 에 잘 나타나는지 확인합니다.
```console
$ python create_run.py
```
<br>

**3. Train Model & Save Model to MLFlow Server**
- `train.py` 를 다음과 같이 실행하여 모델을 학습합니다.
```console
$ python train.py
```
- Website 에 새롭게 생성된 run 을 선택하여 artifact 의 형태로 모델이 잘 저장되었는지 확인합니다.
<br>

**4. Download Model & Load Model from MLFlow Server**
- `load.py` 를 다음과 같이 실행하여 저장된 모델을 다운로드하고 불러와서 iris data 샘플에 대해 inference 를 수행합니다.
```console
$ python load_model.py
```
<br>

## Steps
1. Run MLFlow Server Container (docker)
2. Get Data from DB (python)
3. Train Model (python)
4. Save Model to MLFlow Server (python)
5. Download Model from MLFlow Server and Load Model (python)
<br>

## Python Scripts Details
**`export_data.py`**
- Docker 컨테이너로 실행되고 있는 PostgreSQL DB 의 데이터를 가져옵니다.

**`create_experiment.py`**
- MlflowClient 를 이용해 mlflow server 에 experiment 를 생성합니다.

**`create_run.py`**
- MlflowClient 를 이용해 mlflow server 에 run 을 생성합니다.

**`train.py`**
- MLFlow 의 fluent 방식을 사용해 iris data 를 학습하고 모델을 logging 합니다.

**`load_model.py`**
- MLFlow server 에 저장된 모델을 다운로드하여 불러와 데이터 샘플에 대해 inference 를 수행합니다.
