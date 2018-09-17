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