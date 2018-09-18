# Pi-Personal Notifications
Mini-project to be used in other projects to easely send notifications. For example a message to telegram, or by mail, or by tweet, or any other idea.

I use the RabbitMQ in order to centralise the messages easely and route to the different consumers. The consumers work to deliver the messages to the destination. And the producer can be any other project that I want to notify me when any event happens.

# Steps to put it up&running
To start, you just need to follow the below steps:
* Create a docker network in order to get all containers on that network be able to see it each others:

      docker network create notify_net

* Start a RabbitMQ server in a docker container and connected to the previously created network. Once the container is started you will be able to connect it using a browser and surf to the `http://localhost:8080` and use the credentials set by params `guest/guest` feel free to configure that by yourself.

      docker run -d --hostname rabbit --name rabbit -p 5672:5672 -p 8080:15672 -e RABBITMQ_DEFAULT_USER=guest -e RABBITMQ_DEFAULT_PASS=guest --net notify_net rabbitmq:management-alpine

* Once you have the rabbit up&running you can run one of the services, currently developed services are:

  * Telegram: For sending telegram messages

# Configure and start Telegram service:
The telegram service needs to be configured. To configure it you just need a telegram client and a normal account. Then you can run the configuration script with command below and follow the screen instructions:

    docker run -it --rm --name configure_telegram -v $PWD:/mnt notify_telegram telegram-send --configure --config /mnt/telegram-send.conf

Once the telegram is configured to send you the messages you can just start the service. This service will be listening to a rabbit queue, and any service you want can send messages to that rabbit queue in order the service process them and send it to you by telegram. To start thhe service you just need to run:

    docker run -d --name telegram --net notify_net --rm notify_telegram

# Test

Now if you go to the RabbitMQ web interface and log in, you will be able to add messages to the already existent queue `telegram`. For every message added to the queue, you will get it into your telegram.

# Use as an automatic notification system

The idea is to generate notifications from any process or program. In order to achieve this, you have the script `rabbit_producer_basic.py`, that script will send messages to a configured exchange. You can call it:

    ./rabbit_producer_basic.py --host HOSTNAME --exchange EXCHANGE_NAME --message "Message test"

If you are running the containers locally, your host will be `localhost`. Otherwise if you are calling this script from a service on a container, you must remmember to start that container connected to the same network than the Rabbit and the telegram one. And use then as a HOSTNAME the name you give to the container, if you followed the previous commmand then is `rabbit`.

Because of the internal design of RabbitMQ, the messages sent to an exchange not binded to a queue are discarded. So the last step to make the messages reach your telegram account is to bind into RabbitMQ web interface the `telegram` queue with the `EXCHANGE_NAME` exchange.

You can call the `./rabbit_producer_basic.py` script from any part of your code.