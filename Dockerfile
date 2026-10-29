FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    POETRY_VERSION=1.8.3 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=1

WORKDIR /app

RUN pip install --no-cache-dir "poetry==$POETRY_VERSION"

COPY pyproject.toml poetry.lock ./
RUN poetry install --only main --no-root

COPY src ./src
COPY migrations ./migrations
COPY alembic.ini ./alembic.ini

RUN useradd -m appuser && chown -R appuser /app
USER appuser

CMD ["sh", "-c", "alembic upgrade head"]
