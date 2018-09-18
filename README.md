# Telegram Personal Notifications
Mini-project to send notifications to my telegram when any configured event happens on my raspberry-pi

The project send the messages that were received from a RabbitMQ queue. The queue used is managed by a RabbitMQ server. This mini-script will be just listening for new messages to income into the queue, and send it to my telegram when a new message is received at the Queue.

# Steps to put it up&running

In order to test it, you just need to follow the below steps:
* Create a docker network in order to get all containers on that network be able to see it each others:

    docker network create notify_net

* Start a RabbitMQ server in a docker container and connected to the previously created network. Once the container is started you will be able to connect it using a browser and surf to the `http://localhost:8080` and use the credentials set by params `guest/guest` feel free to configure that by yourself.

    docker run -d --hostname rabbit --name rabbit -p 5672:5672 -p 8080:15672 -e RABBITMQ_DEFAULT_USER=guest -e RABBITMQ_DEFAULT_PASS=guest --net notify_net rabbitmq:management-alpine

* With the rabbit up&running you can run the service for sending the telegram messages:

    docker run -d --name telegram --net notify_net --rm notify_telegram

# Test

Now if you go to the RabbitMQ web interface and log in, you will be able to add messages to the already existent queue `telegram`. For every message added to the queue, you will get it into your telegram.

# Normal use

The idea is to generate notifications from any process or program. In order to achieve this, you have the script `rabbit_producer_basic.py`, that script will send messages to the configured exchange. You can call it:

    ./rabbit_producer_basic.py --host HOST --exchange EXCHANGE_NAME --message "Message test"

If you are running the containers locally, your host will be `localhost`. Otherwise if you are calling this script from a service on a container, you must remmember to start that container connected to the same network than the Rabbit one. And use then as a host the name you give to the container, if you followed the previous commmand then is `rabbit`.

Because of the internal design of RabbitMQ, the messages sent to an exchange not binded to a queue are discarded. So the last step to make the messages reach your telegram account is to bind into RabbitMQ web interface the `telegram` queue with the `EXCHANGE_NAME` exchange.