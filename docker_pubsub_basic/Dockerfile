FROM python:3.6-alpine

LABEL maintainer="http://alejandro.lorente.info"

COPY rabbit_consumer_basic.py /usr/bin
COPY rabbit_producer_basic.py /usr/bin

RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing/" >> /etc/apk/repositories && \
    apk add --update bash build-base openssl-dev libffi-dev && \
    pip install pika telegram-send && \
    rm -rf /tmp/* /var/tmp/* /var/cache/apk/* /var/cache/distfiles/* /root/.cache/*

WORKDIR /mnt

ENV RABBIT_HOSTNAME rabbit
ENV RABBIT_USER guest
ENV RABBIT_PW guest
