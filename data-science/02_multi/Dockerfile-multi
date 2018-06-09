FROM python:3.6 as base
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /wheels jupyter pandas

FROM python:3.6-slim
COPY --from=base /wheels /wheels
RUN pip install --no-cache /wheels/*
WORKDIR /notebooks
