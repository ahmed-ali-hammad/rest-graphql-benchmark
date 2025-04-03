<h3 align="center">Rest Graphql Benchmark</h3>

<div align="center">
  <img src="https://img.shields.io/badge/python-3.11-blue" />
</div>

---

## 📝 Table of Contents
- [About](#about)
- [Getting Started](#getting-started)
- [Built Using](#built-using)

## 🧐 About <a name = "about"></a>
A performance comparison of REST API (resource-driven) and GraphQL (query-driven). Key features:

- Dual API Design: Same functionality built with REST (HTTP verbs) and GraphQL (single endpoint)
- Healthcare Data Model: Full CRUD for patients, medical records, care teams, and contacts
- Metrics: Benchmarked via Apache JMeter 

## 🏁 Getting Started <a name = "getting_started"></a>
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

 - [Docker](https://docs.docker.com/)
 - [Docker Compose](https://docs.docker.com/compose/)

### Installing
If you're opening this project using [devcontainers](https://containers.dev/) then your docker container should be ready to go!

Otherwise you will need to start the docker compose environment `docker compose up` and open a shell into the container `patient_info_dev`.

```bash
docker compose up
docker exec -it patient_info_dev /bin/bash   # spawns a shell within the docker container
pipenv shell  # spawns a shell within the virtualenv 
```

### ▶️ Running the webapp
```bash
source ./config/.env    # add the environment variables to the running terminal
python3 patient_info/manage.py collectstatic --noinput && python3 patient_info/manage.py runserver 0.0.0.0:8000
```

- API Docs [http://0.0.0.0:8888/api/schema/swagger-ui/]
- Django Admin [http://0.0.0.0:8888/admin/login/?next=/admin/]
- GraphQL [http://0.0.0.0:8888/patient_info_graphql/patient/]


### Code Style & Linting
The following tools are run during pipelines to enforce code style and quality.

 - [flake8](https://flake8.pycqa.org/en/latest/) for linting
 - [isort](https://pycqa.github.io/isort/) for import sorting
 - [black](https://black.readthedocs.io/en/stable/) for code style

### Python Package Management
[pipenv](https://pipenv.pypa.io/en/latest/) is used to manage Python packages. 

```bash
$ pipenv shell  # spawns a shell within the virtualenv
$ pipenv install  # installs all packages from Pipfile
$ pipenv install --dev # installs all packages from Pipfile, including dev dependencies
$ pipenv install <package1> <package2>  # installs provided packages and adds them to Pipfile
$ pipenv update  # update package versions in Pipfile.lock, this should be run frequently to keep packages up to date
$ pipenv uninstall package # uninstall a package 
$ pipenv uninstall package  --categories dev-packages # uninstall a dev package
```

## ⛏️ Built Using <a name = "built_using"></a>
- [Django](https://www.djangoproject.com/) - Web Framework.
- [PostgreSQL](https://www.postgresql.org/) - Database.