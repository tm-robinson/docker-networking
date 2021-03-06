FROM python:3.8-slim-buster

WORKDIR /app

RUN pip install requests

COPY . .

CMD [ "bash", "run-client.sh" ]
