FROM amd64/python:3.9-slim

LABEL maintainer="Seokgi Kim <datawhales@gmail.com>"
WORKDIR /usr/app

RUN apt-get update && apt-get install -y \
    curl \
    ca-certificates \
    sudo \
    git \
    bzip2 \
    libx11-6 \
    libglib2.0-0 \
    libpq-dev \
    vim \
    make \
    wget \
    lshw \
    tree \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*


ENV PATH="/usr/local/bin/python3:$PATH"

RUN pip install -U pip \
    && pip install "fastapi[all]" sqlalchemy psycopg2-binary

COPY ./my_app /usr/app

EXPOSE 7777

ENTRYPOINT uvicorn main:app --host 0.0.0.0 --port 7777 --reload
