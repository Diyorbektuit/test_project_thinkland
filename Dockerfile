FROM python:3.12-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt clean && apt update && apt install curl netcat vim -y

WORKDIR /app

COPY requirements /app/requirements
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r /app/requirements/develop.txt \
    && pip cache purge

COPY . /app