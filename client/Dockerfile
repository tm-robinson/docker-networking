FROM python:3.8-slim-buster

WORKDIR /app

RUN pip install requests flask

COPY . .

CMD [ "bash", "run-flaskapp.sh" ]
