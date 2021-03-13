FROM python:3.6-buster

ENV PROJECT_DIR=/app/src/botai

RUN mkdir -p ${PROJECT_DIR}

COPY . ${PROJECT_DIR}/

WORKDIR ${PROJECT_DIR}

RUN python3 -m pip install pipenv
RUN python3 -m pipenv install -e .
RUN python3 -m pipenv run python -m unittest

# RUN rm -fr ${PROJECT_DIR}

CMD ["python3", "-m", "pipenv run python -m unittest"]
