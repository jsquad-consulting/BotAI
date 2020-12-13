# BotAI

Create sample Python modules to demonstrate machine learning with help of TensorFlow.

Pipfile has all the dependencies and package configurations needed to package and deploy the application locally or
with Docker.

## Install dependencies

python3 -m pip install pipenv

## Development

```bash
python3 -m pipenv run python botai to test it out without setup.py installation
python3 -m pipenv check # Check for vulnerabilities and PEP 508 requirements
python3 -m pipenv run pytest # run unit, system and integration tests
```

## Install

```bash
python3 -m pipenv install -e . # Compile and package application  
python3 setup.py install # Install the compiled and packaged application, dealt with by the Docker Compose file
```

## Start the packaged application in docker

```bash
docker-compoe -f docker-compose.yaml up --build --force-recreate
```

## Sync setup.py installation file with Pipfile requirements file

```bash
python3 -m pipenv run
pipenv-setup sync # generate/sync Pipfile with setup.py file
```