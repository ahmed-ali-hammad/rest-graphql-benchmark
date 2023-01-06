FROM ubuntu:23.04

# updating the base image package manager
RUN apt update

# installing python3 and pip
RUN apt install -y python3.11
RUN apt install -y python3-pip

# install graphviz to be able to generate models graph
# see https://django-extensions.readthedocs.io/en/latest/graph_models.html
RUN apt -y install graphviz

# avoid writting byte code
ENV PYTHONDONTWRITEBYTECODE 1

# ensures that the python output streams are sent straight to terminal, without being first buffered
ENV PYTHONUNBUFFERED 1

WORKDIR /home

# copying the application files to the server
COPY ./patient_info ./patient_info

# for serving the static files
ENV APP_HOME=patient_info
RUN mkdir -p $APP_HOME/staticfiles
RUN mkdir -p $APP_HOME/mediafiles

COPY ./requirements.txt .
RUN pip3 install -r requirements.txt

# CMD [ "python3", "patient_info/manage.py", "runserver", "0.0.0.0:8000"]