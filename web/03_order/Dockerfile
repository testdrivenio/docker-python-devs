FROM python:3.6-alpine

WORKDIR /app
# What happens when a change is made to sample.py?
COPY sample.py /app

COPY requirements.txt /
RUN pip install -r /requirements.txt  # flask and gunicorn
