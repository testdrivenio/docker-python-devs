FROM python:3.6-alpine

WORKDIR /app

COPY requirements.txt /
RUN pip install -r /requirements.txt  # flask and gunicorn

COPY . /app
