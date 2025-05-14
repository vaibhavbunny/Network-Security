FROM python:3.10-slim-buster

WORKDIR /app

COPY . ./app
COPY requirements.txt ./

RUN apt update -y && apt install -y awscli
RUN pip install -r requirements.txt

CMD ["python3", "app.py"]
