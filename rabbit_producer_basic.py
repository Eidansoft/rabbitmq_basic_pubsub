#!/usr/bin/env python
import sys, getopt
import pika

class Rabbit_producer_basic():
    host = None
    exchange = None
    connection = None
    channel = None
    message = None

    def connect_to_rabbit(self):

        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.host))

        self.channel = self.connection.channel()

        self.channel.exchange_declare(exchange=self.exchange, exchange_type='fanout')


    def disconnect_rabbit(self):
        self.connection.close()


    def show_usage(self):
        print ('notify_by_telegram.py --host HOST_NAME --exchange EXCHANGE_NAME --message MESSAGE')


    def main(self, argv):
        try:
            opts, args = getopt.getopt(argv,"",["host=","exchange=","message="])
            pass
        except getopt.GetoptError:
            print('[ERROR] Params received not correct.')
            self.show_usage()
            sys.exit(2)
        for opt, arg in opts:
            if opt == "--host":
               self.host = arg
            elif opt == "--exchange":
               self.exchange = arg
            elif opt == "--message":
                self.message = arg

        if (not self.host or not self.exchange or not self.message):
            print('[ERROR] Mandatory param empty.\nHOST: %s\nEXCHANGE: %s\nMESSAGE: %s\n' % (self.host, self.exchange, self.message))
            self.show_usage()
            sys.exit(2)

        self.connect_to_rabbit()
        self.channel.basic_publish(exchange=self.exchange,
                                   routing_key='',
                                   body=self.message)
        self.disconnect_rabbit()
        print(' [*] Connected to RabbitMQ on %s and try to sent message "%s"' % (self.host, self.message))


if __name__ == "__main__":
    app = Rabbit_producer_basic()
    params = sys.argv[1:]
    app.main(params)
