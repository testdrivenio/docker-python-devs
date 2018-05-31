###########
# BUILDER #
###########

# Base Image
FROM python:3.6 as builder

# Install Requirements
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /wheels jupyter pandas


#########
# FINAL #
#########

# Base Image
FROM python:3.6-slim

# Create directory for the app user
RUN mkdir -p /home/app

# Create the app user
RUN groupadd app && useradd -g app app

# Create the home directory
ENV HOME=/home/app
ENV APP_HOME=/home/app/notebooks
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

# Install Requirements
COPY --from=builder /wheels /wheels
RUN pip install --no-cache /wheels/*

# Chown all the files to the app user
RUN chown -R app:app $HOME

# Change to the app user
USER app

# run server
CMD jupyter notebook --no-browser --port=8888 --ip=0.0.0.0
