FROM python:3.9.7-slim

RUN pip install -U pip
RUN pip install pipenv

WORKDIR /app

COPY ["Pipefile", "Pipfile.lock", "./"]

RUN pipenv install --setting --deploy

COPY ["predict.py", "web-service/lin_reg.bin", "./"]
EXPOSE 8080
ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:8080", "predict:app"]