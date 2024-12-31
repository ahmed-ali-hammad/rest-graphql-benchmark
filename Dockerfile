FROM python:3.11

RUN apt update && apt install -y postgresql 

# install graphviz to be able to generate models graph
# see https://django-extensions.readthedocs.io/en/latest/graph_models.html
RUN apt -y install graphviz

WORKDIR /home

# for serving the static files
ENV APP_HOME=patient_info
RUN mkdir -p $APP_HOME/staticfiles
RUN mkdir -p $APP_HOME/mediafiles

RUN pip install --upgrade pip && pip install pipenv
ENV PIPENV_CUSTOM_VENV_NAME="rest-graphql-benchmark"

COPY Pipfile ./
COPY Pipfile.lock ./

RUN pipenv install --dev