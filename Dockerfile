FROM python:3.11

WORKDIR /code

COPY pyproject.toml poetry.lock* README.md ./
RUN pip install poetry && poetry config virtualenvs.create false && poetry install --no-root --no-interaction --no-ansi

COPY . .

CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
