FROM python:3.11.5-slim

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

# os-level installs
RUN apt-get update && \
    apt-get install -y \
    build-essential \
    python3-dev \
    python3-setuptools \
    libpq-dev \
    gcc \
    make

RUN pip install --upgrade pip
ADD ./src/requirements.txt /app/
RUN pip install -r requirements.txt

ADD ./src /app/src
ADD ./docker /app/docker

# purge unused
RUN apt-get remove -y --purge make gcc build-essential \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*
RUN apt-get update

RUN chmod +x /app/docker/backend/server-entrypoint.sh
RUN chmod +x /app/docker/backend/celery-entrypoint.sh
