FROM python:3.12-slim-bullseye

RUN pip install -U pip

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /app

CMD ["python", "main.py"]