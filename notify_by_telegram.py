#!/usr/bin/env python
import sys, getopt
import pika


def connect_to_rabbit(rabbit_host, rabbit_queue):

    connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbit_host))

    channel = connection.channel()

    channel.queue_declare(queue=rabbit_queue)

    print(' [*] Created connection to RabbitMQ server on %s' % rabbit_host)
    return channel


def callback(channel, method, properties, body):
    print(" [x] Received %r" % body)


def start_service(channel, callback_function, rabbit_queue):
    channel.basic_consume(callback_function,
                          queue=rabbit_queue,
                          no_ack=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


def show_usage():
    print ('notify_by_telegram.py --host HOST_NAME --queue QUEUE_NAME')

def main(argv):
    rabbit_host = ''
    rabbit_queue = ''
    try:
        opts, args = getopt.getopt(argv,"",["host=","queue="])
    except getopt.GetoptError:
        show_usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt == "--host":
           rabbit_host = arg
        elif opt == "--queue":
           rabbit_queue = arg

    if (rabbit_host == '' or rabbit_queue == ''):
        show_usage()
        sys.exit(2)

    channel = connect_to_rabbit(rabbit_host, rabbit_queue)
    start_service(channel, callback, rabbit_queue)


if __name__ == "__main__":
   main(sys.argv[1:])
