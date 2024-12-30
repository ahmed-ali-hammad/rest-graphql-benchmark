FROM python:3.11

RUN apt update && apt install -y postgresql 

# install graphviz to be able to generate models graph
# see https://django-extensions.readthedocs.io/en/latest/graph_models.html
RUN apt -y install graphviz

WORKDIR /home

COPY ./requirements.txt .
RUN pip3 install -r requirements.txt

COPY ./patient_info ./patient_info

# for serving the static files
ENV APP_HOME=patient_info
RUN mkdir -p $APP_HOME/staticfiles
RUN mkdir -p $APP_HOME/mediafiles

# CMD [ "python3", "patient_info/manage.py", "runserver", "0.0.0.0:8000"]