FROM python:3.6-alpine

RUN apk --no-cache add --virtual build-dependencies \
                build-base \
                python3-dev \
        && pip3 install \
                jupyter \
                pandas

WORKDIR /notebooks
