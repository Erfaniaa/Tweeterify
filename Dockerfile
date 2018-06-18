FROM ubuntu:xenial

MAINTAINER Erfan Alimohammadi "<erfan.aa@gmail.com>"

ADD ./requirements.txt /app/
WORKDIR /app

RUN apt-get update -yq && apt-get install -y python3-pip
RUN pip3 install -U -r requirements.txt

ADD . /app

ENTRYPOINT ["./entrypoint.sh"]
