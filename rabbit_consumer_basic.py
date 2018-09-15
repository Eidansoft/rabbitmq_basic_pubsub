#!/usr/bin/env python
import sys, getopt
import pika

class Rabbit_consumer_basic():
    rabbit_host = ''
    rabbit_queue = ''
    connection = None
    channel = None

    def connect_to_rabbit(self):

        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.rabbit_host))

        self.channel = self.connection.channel()

        self.channel.queue_declare(queue=self.rabbit_queue)

        print(' [*] Created connection to RabbitMQ server on %s' % self.rabbit_host)


    def callback(self, channel, method, properties, body):
        print(" [x] Received %r" % body)


    def start_service(self):
        self.channel.basic_consume(self.callback,
                              queue=self.rabbit_queue,
                              no_ack=True)
        print(' [*] Waiting for messages. To exit press CTRL+C')
        self.channel.start_consuming()


    def show_usage(self):
        print ('notify_by_telegram.py --host HOST_NAME --queue QUEUE_NAME')


    def main(self, argv):
        try:
            opts, args = getopt.getopt(argv,"",["host=","queue="])
            pass
        except getopt.GetoptError:
            print('[ERROR] Params received not correct.')
            self.show_usage()
            sys.exit(2)
        for opt, arg in opts:
            if opt == "--host":
               self.rabbit_host = arg
            elif opt == "--queue":
               self.rabbit_queue = arg
        if (self.rabbit_host == '' or self.rabbit_queue == ''):
            print('[ERROR] Mandatory param empty.\nHOST: %s\nQUEUE: %s\n' % (self.rabbit_host, self.rabbit_queue))
            self.show_usage()
            sys.exit(2)

        channel = self.connect_to_rabbit()
        self.start_service()


if __name__ == "__main__":
    app = Rabbit_consumer_basic()
    params = sys.argv[1:]
    app.main(params)
