<h3 align="center">Rest Graphql Benchmark</h3>

<div align="center">
  <img src="https://img.shields.io/badge/status-active-success.svg" />
  <img src="https://img.shields.io/badge/python-3.13-blue" />
</div>

---

<p align="center">Rest Graphql Benchmark
    <br> 
</p>

## 📝 Table of Contents
- [About](#about)
- [Getting Started](#getting-started)
- [Built Using](#built-using)

## 🧐 About <a name = "about"></a>
TODO

## 🏁 Getting Started <a name = "getting_started"></a>
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

 - [Docker](https://docs.docker.com/)
 - [Docker Compose](https://docs.docker.com/compose/)

### Installing

```bash
docker compose up
docker exec -it patient_info_dev /bin/bash   # spawns a shell within the docker container
pipenv shell  # spawns a shell within the virtualenv 
```


### ▶️ Running the webapp
```bash
source ./config/.env    # add the environment variables to the running terminal
python3 manage.py collectstatic --noinput && python3 manage.py runserver 0.0.0.0:8000
```

### 🧪 Running the tests <a name = "tests"></a>
[pytest](https://docs.pytest.org/) is used for testing.

```bash
$ pytest tests/             # run all tests
$ pytest tests/unit         # run only the unit tests
$ pytest tests/integration  # run only the integration tests
```

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
```

## ⛏️ Built Using <a name = "built_using"></a>
- [Django](https://www.djangoproject.com/) - Web Framework.
- [PostgreSQL](https://www.postgresql.org/) - Database.