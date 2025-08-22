FROM python:3.12

WORKDIR /app

COPY pyproject.toml .
COPY uv.lock .

RUN pip install uv==0.6.1 --no-cache-dir
RUN uv pip install -e . --system


COPY src ./src
COPY migrations ./migrations
COPY settings.json .
COPY entrypoint.sh .

