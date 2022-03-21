FROM python:3.7

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

RUN mkdir /app

WORKDIR /app

RUN apt-get update

RUN apt-get -y install python-pip

RUN apt-get update

RUN pip install --upgrade pip

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY . /app/

CMD ["python", "manage.py"]
