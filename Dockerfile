FROM python:3

ENV PYTHONUNBUFFERED 1
RUN mkdir /BlogAPI
WORKDIR /BlogAPI
COPY . /blog
RUN pip3 install -r requirements.txt
