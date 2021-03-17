FROM python:3.8-slim

ENV PYTHONUNBUFFERED 1
WORKDIR /Blog_API


RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install -y apt-utils
RUN apt-get install gcc -y
RUN apt-get clean
RUN apt-get install -y python-setuptools
#RUN apt-get install -y postgresql postgresql-contrib
RUN apt-get install -y libpq-dev python3-dev
RUN apt-get install -y systemd

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . /BlogAPI


EXPOSE 8080
CMD ["python3", "blog/manage.py", "runserver", "0.0.0.0:8080"]
