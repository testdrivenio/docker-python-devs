FROM python:3.6-alpine

RUN apk --no-cache add --virtual build-dependencies \
                build-base \
                python3-dev

# Create directory for the app user
RUN mkdir -p /home/app

# Create the app user
RUN addgroup -S app && adduser -S -G app app

# Create the home directory
ENV HOME=/home/app
ENV APP_HOME=/home/app/notebooks
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

# Install requirements
RUN pip install jupyter pandas

# Chown all the files to the app user
RUN chown -R app:app $APP_HOME

# Change to the app user
USER app
