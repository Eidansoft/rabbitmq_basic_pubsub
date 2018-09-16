FROM python:3.6-alpine

LABEL maintainer="http://alejandro.lorente.info"

COPY rabbit_consumer_basic.py /usr/bin
COPY notify_by_telegram.py /usr/bin

RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing/" >> /etc/apk/repositories && \
    apk add --update bash build-base openssl-dev libffi-dev && \
    rm -rf /tmp/* /var/tmp/* /var/cache/apk/* /var/cache/distfiles/* && \
    pip install pika telegram-send

WORKDIR /mnt

ENV QUEUE_HOST rabbit
ENV QUEUE_NAME telegram

CMD notify_by_telegram.py --host $QUEUE_HOST --queue $QUEUE_NAME