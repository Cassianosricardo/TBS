FROM python:3
 ENV PYTHONUNBUFFERED 1
 RUN mkdir /code
 WORKDIR /code
 RUN apt update && apt install -y \
    python-dev \
    default-libmysqlclient-dev
 ADD requirements.txt /code/
 RUN pip install -r requirements.txt
 ADD . /code/