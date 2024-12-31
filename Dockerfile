FROM python:3.11

# Install PostgreSQL client for shell access inside the container
RUN apt update && apt install -y postgresql 

WORKDIR /home

# For static files
ENV APP_HOME=patient_info
RUN mkdir -p $APP_HOME/staticfiles
RUN mkdir -p $APP_HOME/mediafiles

RUN pip install --upgrade pip && pip install pipenv
ENV PIPENV_CUSTOM_VENV_NAME="rest-graphql-benchmark"

COPY Pipfile ./
COPY Pipfile.lock ./
RUN pipenv install --dev