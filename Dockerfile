FROM python:3.6-buster

ENV PROJECT_DIR=/app/src/botai

RUN mkdir -p ${PROJECT_DIR}

COPY . ${PROJECT_DIR}/

WORKDIR ${PROJECT_DIR}

RUN python3 setup.py install

RUN rm -fr ${PROJECT_DIR}

CMD ["python3", "-m", "botai"]
