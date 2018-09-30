FROM rabbit/pubsub:latest

LABEL maintainer="http://alejandro.lorente.info"

COPY notify_by_telegram.py /usr/bin
COPY telegram-send.conf /etc/telegram-send.conf

WORKDIR /mnt

ENV RABBIT_QUEUE telegram

CMD rabbit_producer_basic.py --host $RABBIT_HOSTNAME --queue $RABBIT_QUEUE --user $RABBIT_USER --pw $RABBIT_PW --message 'Telegram notifier has started.' && \
    notify_by_telegram.py --host $RABBIT_HOSTNAME --user $RABBIT_USER --pw $RABBIT_PW --queue $RABBIT_QUEUE