#!/usr/bin/env python
import sys, getopt
import pika

class Rabbit_consumer_basic():
    user = None
    passwd = None
    host = None
    queue = None
    connection = None
    channel = None

    def connect_to_rabbit(self):

        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.host, credentials=pika.PlainCredentials(self.user, self.passwd)))

        self.channel = self.connection.channel()

        self.channel.queue_declare(queue=self.queue)

        print(' [*] Created connection to RabbitMQ server on %s' % self.host)


    def callback(self, channel, method, properties, body):
        print(" [x] Received %r" % body)


    def start_service(self):
        self.channel.basic_consume(self.callback,
                              queue=self.queue,
                              no_ack=True)
        print(' [*] Waiting for messages. To exit press CTRL+C')
        self.channel.start_consuming()


    def show_usage(self):
        print ('rabbit_consumer_basic.py --host HOST_NAME --user USER --pw PASSWORD --queue QUEUE_NAME')


    def main(self, argv):
        try:
            opts, args = getopt.getopt(argv,"",["host=","queue=","user=","pw="])
            pass
        except getopt.GetoptError:
            print('[ERROR] Params received not correct.')
            self.show_usage()
            sys.exit(2)
        for opt, arg in opts:
            if opt == "--host":
               self.host = arg
            elif opt == "--queue":
               self.queue = arg
            elif opt == "--user":
               self.user = arg
            elif opt == "--pw":
               self.passwd = arg
        if (self.host == '' or self.queue == '' or self.user == ''):
            print('[ERROR] Mandatory param empty.\nHOST: %s\nQUEUE: %s\nUSER: %s\n' % (self.host, self.queue, self.user))
            self.show_usage()
            sys.exit(2)

        channel = self.connect_to_rabbit()
        self.start_service()


if __name__ == "__main__":
    app = Rabbit_consumer_basic()
    params = sys.argv[1:]
    app.main(params)
