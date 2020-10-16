FROM python:3.8-slim

ENV PYTHONUNBUFFERED 1
MAINTAINER Blog_API


RUN apt-get update \
&& apt-get install gcc -y \
&& apt-get clean


COPY ./requirements.txt /requirements.txt

RUN pip3 install -r requirements.txt


RUN mkdir /BlogAPI
WORKDIR /BlogAPI
COPY ./blog ./BlogAPI
