.PHONY: install migrate load lint format typecheck test clean

install:
	poetry install
	poetry run pre-commit install

migrate:
	poetry run alembic upgrade head

load:
	poetry run python -m logistics_model.cli

lint:
	poetry run ruff check .

format:
	poetry run ruff format .

typecheck:
	poetry run mypy src

test:
	poetry run pytest

clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type f -name "*.pyc" -delete
	rm -f logistics.db
