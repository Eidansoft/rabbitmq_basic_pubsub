# Telegram Personal Notifications
Mini-project to send notifications to my telegram when any configured event happens on my raspberry-pi

The project send the messages that were received from a queue. The queue used is managed by a RabbitMQ server. This mini-script will be just listening for new messages to income into the queue, and send it to my telegram when a new messagen is received at the Queue.

# Test
In order to test it, I start a RabbitMQ server with docker container. To do it so I just run:

    docker run -d --hostname rabbit --name rabbit -p 5672:5672 -p 8080:15672 -e RABBITMQ_DEFAULT_USER=guest -e RABBITMQ_DEFAULT_PASS=guest rabbitmq:management-alpine

Once the container is started I am able to connect it using a browser and connecting to the http://localhost:8080 and use the given credentials guest/guest.

With the rabbit up&running I can run the service for sending the telegram messages