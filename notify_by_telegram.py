#!/usr/bin/env python
from rabbit_consumer_basic import Rabbit_consumer_basic
import sys

class Notify_telegram(Rabbit_consumer_basic):

    def callback(self, channel, method, properties, body):
        print(" [x] Received and this will be send to telegram %r" % body)


if __name__ == "__main__":
    app = Notify_telegram()
    params = sys.argv[1:]
    app.main(params)
