FROM python:3.8.3-slim-buster

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1

COPY requirements.txt .

RUN set -ex && \
    apt-get update && \
    apt-get install libpq-dev -y && \
    apt-get autoremove && apt-get autoclean && apt-get clean && \
    pip install -U pip setuptools wheel && \
    pip install -r /usr/src/app/requirements.txt && \
    rm -rf /root/.cache/pip

COPY . .