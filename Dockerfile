# docs: https://hub.docker.com/_/python
FROM python:3

WORKDIR /4-containerized-app-exercise-speedy

COPY . .

WORKDIR web_app

COPY web_app/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "pytest" ]
