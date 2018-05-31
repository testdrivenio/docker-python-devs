# Base
FROM python:3.6-alpine

# Create directory for the app user
RUN mkdir -p /home/app

# Create the app user
RUN addgroup -S app && adduser -S -G app app

# Create the home directory
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

# Install requirements
COPY requirements.txt /
RUN pip install -r /requirements.txt  # flask and gunicorn

# Copy in the Flask code
COPY . $APP_HOME

# Chown all the files to the app user
RUN chown -R app:app $APP_HOME

# Change to the app user
USER app
