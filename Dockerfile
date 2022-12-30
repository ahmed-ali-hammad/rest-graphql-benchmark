FROM python:3.12.0a3-buster

RUN apt update
RUN apt -y install graphviz

WORKDIR /home

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt .

RUN pip3 install -r requirements.txt

COPY ./patient_info_graphql ./patient_info_graphql

# for serving the static files
ENV APP_HOME=patient_info_graphql
RUN mkdir -p $APP_HOME/staticfiles
RUN mkdir -p $APP_HOME/mediafiles

# CMD [ "python", "patient_info_graphql/manage.py", "runserver", "0.0.0.0:8000"]