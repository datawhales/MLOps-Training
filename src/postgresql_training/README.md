# PostgreSQL Training
- Database 를 서비스에 이용하기 위한 방법을 알아보고 연습합니다.
- Local 에서 docker 를 이용해 직접 PostgreSQL 서버를 띄워봅니다.
- DB 에 테이블을 만들고, 데이터를 삽입해봅니다.
<br>

## Quick Start
**0. Setup**  
- `python==3.8.13` 버전을 이용하여 가상 환경을 구축합니다.
- 필요한 라이브러리를 다음의 명령어를 이용하여 설치합니다.
```console
$ pip install -r requirements.txt
```
<br>

**1. Pull PostgreSQL Docker Image**  
- 다음의 명령어를 terminal 에 입력하여 postgresql 의 docker image 를 pull 합니다.
```console
$ docker pull postgres:14.0
```
<br>

**2. Run PostgreSQL Container**  
- 다음의 명령어를 terminal 에 입력하여 postgresql container 를 작동시킵니다.
```console
$ docker run --name postgres-server -e POSTGRES_DB=mydatabase -e POSTGRES_USER=myuser -e POSTGRES_PASSWORD=mypassword -p 5432:5432 -d postgres:14.0
```
<br>

**3. Create Table**  
- `iris_data` 를 저장하는 테이블을 생성합니다.
- `meta.py` 의 DB 연결 정보를 이용하여 DB 에 접속하고, 쿼리를 날려 테이블을 생성하는 `create_table.py` 스크립트를 실행합니다.
```console
$ python create_table.py
```
<br>

**4. Insert Data & Query Inserted Data**  
- `iris_data` 의 첫 번째 row 를 postgresql db 의 테이블에 삽입합니다.
- `meta.py` 의 DB 연결 정보를 이용하여 DB 에 접속하고, 쿼리를 날려 데이터를 삽입하는 `insert_row.py` 스크립트를 실행합니다.
```console
$ python insert_row.py
```
데이터가 테이블에 잘 삽입되었는지 확인하기 위해 다음과 같이 `psql` 을 통해 DB 에 직접 접속하여 확인해봅니다.
```console
$ psql -U myuser -h localhost -p 5432 -d mydatabase
$ mypassword
```
<br>

**5. Insert Data Continuously**  
- `iris_data` 의 전체 row 를 5초마다 1개씩 postgresql db 의 테이블에 삽입합니다.
- `meta.py` 의 DB 연결 정보를 이용하여 DB 에 접속하고, 쿼리를 날려 데이터를 지속적으로 삽입하는 `insert_rows_cont.py` 스크립트를 실행합니다.
```console
$ python insert_rows_cont.py
```
<br>

**6. Write Dockerfile & Build Image**  
- 데이터를 지속적으로 테이블에 삽입하는 스크립트를 실행하는 도커 이미지를 빌드합니다.
- 다음과 같은 형태로 이미지를 빌드하여 [docker hub](https://hub.docker.com/)에 업로드하였습니다.
```console
$ docker build -f docker/Dockerfile -t <YOUR IMAGE NAME> .
```
- 해당 이미지를 사용하려면 다음과 같이 pull 하여 사용할 수 있습니다.
```console
$ docker pull datawhales/postgresql-training:0.1.7
```
<br>

**7. Run a Container Inserting Data to PostgreSQL Server**  
- 데이터를 삽입하는 도커 컨테이너에서 DB 컨테이너로 접속할 수 있도록 docker network 를 설정해 주어야 합니다.
- 다음과 같이 도커 네트워크를 생성합니다.
```console
$ docker network create db-network
```
- 실행 중인 DB 컨테이너를 생성한 도커 네트워크에 연결합니다.
```console
$ docker network connect db-network postgres-server
```
- DB 컨테이너가 도커 네트워크에 잘 연결되었는지 확인합니다.
```console
$ docker network inspect db-network
```
- 이제 이미지를 이용하여 도커 컨테이너를 실행합니다.
- 이 때, network 옵션에 DB 컨테이너가 연결된 도커 네트워크를 지정해 줍니다.
```console
$ docker run --name data-generator --network "db-network" --platform=linux/amd64 -d <YOUR IMAGE NAME>
```
- `psql` 을 통해 DB 에 직접 접속하여 데이터가 잘 삽입되는지 확인합니다.
```console
$ psql -U myuser -h localhost -p 5432 -d mydatabase
```
<br>

## Steps
1. Run Database Container (docker)
2. Create Table (python)
3. Insert Data (python) 
4. Query Inserted Data (postgresql)
5. Insert Data Continuously (python)
6. Write dockerfile with script and build image (docker)
7. Run a container inserting data to postgresql server (docker)
<br>

## Python Scripts Details
**`meta.py`**
- DB 의 연결 정보를 담고 있습니다.

**`create_table.py`**
- `psycopg2` 패키지를 이용해 DB 에 접속하고 테이블을 생성합니다.

**`insert_row.py`**
- `psycopg2` 패키지를 이용해 DB 에 접속하고 데이터 1개를 삽입합니다.

**`insert_rows_cont.py`**
- `psycopg2` 패키지를 이용해 DB 에 접속하고 데이터를 지속적으로 삽입합니다.
