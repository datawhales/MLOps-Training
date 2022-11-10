FROM python:3.8

LABEL maintainer="Seokgi Kim <datawhales@gmail.com>"
WORKDIR /root

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

RUN sudo apt update && sudo apt install -y postgresql
COPY ./my_app /root
COPY requirements.txt /root/requirements.txt

ENV PATH="/usr/local/bin/python3:$PATH"
RUN pip install -U pip \
    && pip install -r requirements.txt

EXPOSE 7777

CMD uvicorn main:app --proxy-headers --host 0.0.0.0 --port 7777 --reload
