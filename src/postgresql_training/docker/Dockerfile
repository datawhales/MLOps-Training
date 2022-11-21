FROM amd64/python:3.9-slim

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
    tree \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt /root/requirements.txt
COPY ./docker /root

ENV PATH="/usr/local/bin/python3:$PATH"
RUN pip install -U pip \
    && pip install -r requirements.txt

CMD ["python", "insert_rows_cont.py"]
