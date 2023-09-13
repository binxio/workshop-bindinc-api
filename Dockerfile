# Use the official Python image as the base image
FROM python:3.10-slim

# Set the working directory in Docker
WORKDIR /app

# Copy the poetry lock and pyproject files
COPY flaskapi/pyproject.toml flaskapi/poetry.lock ./

# Install poetry
RUN pip install poetry

# Use poetry to install dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Copy the rest of the application
COPY flaskapi .

# Command to run the application using gunicorn
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app
