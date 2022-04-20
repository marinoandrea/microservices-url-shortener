# syntax=docker/dockerfile:1

FROM python:3.9-slim-bullseye

ENV APP_DIR /usr/local/src/auth-service

COPY . ${APP_DIR}/

WORKDIR ${APP_DIR}

RUN apt-get update && apt-get install -y pipenv

RUN pipenv install --system --deploy

EXPOSE 5000

ENV FLASK_APP ${APP_DIR}/app.py

CMD [ "flask", "run", "--host", "0.0.0.0" ]