FROM python:3.8

LABEL maintainer="Seokgi Kim <datawhales@gmail.com>"
WORKDIR /mlflow

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
    && rm -rf /var/lib/apt/lists/*

COPY . /mlflow

ENV PATH="/usr/local/bin/python3:$PATH"
RUN pip install -U pip \
    && pip install -r requirements.txt

EXPOSE 5000

CMD mlflow server --host 0.0.0.0 --port 5000
