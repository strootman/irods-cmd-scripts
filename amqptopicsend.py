#!/usr/bin/env python2.6
import sys
import pika

host = sys.argv[1]
port = sys.argv[2]
user = sys.argv[3]
password = sys.argv[4]
key = sys.argv[5]
body = sys.argv[6]
ephemeral = sys.argv[7]  # Indicates if the exchange is only temporary (for testing)

exchange='irods'
credentials = pika.PlainCredentials(user, password)

connection = pika.BlockingConnection(
	pika.ConnectionParameters(
			host=host,
			port=int(port),
			credentials=credentials
	)
)

channel = connection.channel()

channel.exchange_declare(exchange=exchange,
                         type='topic',
                         durable=(not ephemeral),
                         auto_delete=ephemeral)

channel.basic_publish(exchange=exchange,
                      routing_key=key,
                      body=body)

connection.close()
