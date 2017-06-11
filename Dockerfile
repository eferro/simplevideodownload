FROM ubuntu:15.04

ENV REFRESEHED_AT 2017-06-11

MAINTAINER Eduardo Ferro Aldama <eduardo.ferro.aldama@gmail.com>

RUN apt-get update
RUN apt-get install -y software-properties-common
RUN apt-get update
RUN apt-get install -y ffmpeg rtmpdump
# Install Python
RUN \
  apt-get update && \
  apt-get install -y python python-dev python-pip libpython-dev python2.7-dev python-virtualenv && \
  rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade youtube_dl && mkdir /download

ADD simplevideodownload.py /usr/bin/simplevideodownload
RUN chmod 755 /usr/bin/simplevideodownload
WORKDIR /download

ENTRYPOINT ["simplevideodownload"]
