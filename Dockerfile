FROM ubuntu:18.10

ENV REFRESEHED_AT 2019-04-26

MAINTAINER Eduardo Ferro Aldama <eduardo.ferro.aldama@gmail.com>

RUN apt-get update && apt-get install -y software-properties-common ffmpeg rtmpdump python3 python3-dev python3-pip libpython3-dev python3-dev python3-virtualenv
RUN rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade youtube_dl && mkdir /download

ADD simplevideodownload.py /usr/bin/simplevideodownload
RUN chmod 755 /usr/bin/simplevideodownload
WORKDIR /download

ENTRYPOINT ["simplevideodownload"]
