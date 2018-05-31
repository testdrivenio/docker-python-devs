FROM python:3.6 as base
COPY requirements.txt /
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /wheels -r requirements.txt

FROM python:3.6-alpine
COPY --from=base /wheels /wheels
COPY --from=base requirements.txt .
RUN pip install --no-cache /wheels/* # flask, gunicorn, pycrypto
WORKDIR /app
COPY . /app
