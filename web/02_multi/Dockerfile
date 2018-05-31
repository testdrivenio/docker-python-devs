FROM python:3.6

WORKDIR /app

COPY requirements.txt /
RUN pip install -r /requirements.txt  # flask, gunicorn, pycrypto

COPY . /app
