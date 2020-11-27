FROM ubuntu:20.04
MAINTAINER Gian Pio Domiziani

RUN apt-get update -y
RUN apt install -y python3-pip

WORKDIR /app
# add all flask's contents in workdir
ADD . /app
RUN pip3 install uwsgi
RUN pip3 install -r requirements.txt
# try to install uwsgi directly inside docker container
CMD ["uwsgi", "app.ini"]