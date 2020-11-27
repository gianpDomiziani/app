FROM python:3.8-slim-buster
MAINTAINER Gian Pio Domiziani

WORKDIR /app
# add all flask's contents in workdir
ADD . /app
RUN pip3 install -r requirements.txt
# try to install uwsgi directly inside docker container
RUN pip3 install uwsgi
CMD ['uwsgi', 'app.ini']