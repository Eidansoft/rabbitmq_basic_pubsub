#!/usr/bin/env python
from rabbit_consumer_basic import Rabbit_consumer_basic
import sys
import telegram_send

class Notify_telegram(Rabbit_consumer_basic):

    def callback(self, channel, method, properties, body):
        telegram_send.send(messages=[body.decode("utf-8")], parse_mode='text', conf='/etc/telegram-send.conf')
        print(" [x] Received and sent to telegram %r" % body)


if __name__ == "__main__":
    app = Notify_telegram()
    params = sys.argv[1:]
    app.main(params)
