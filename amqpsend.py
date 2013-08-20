#!/usr/bin/env python
# This code is based on the code with the same name in iRODS 3.3.

import sys
import pika

host = sys.argv[1]
port = sys.argv[2]
key = sys.argv[3]
body = sys.argv[4]

exchange='irods'

connection = pika.BlockingConnection(
	pika.ConnectionParameters(
			host=host,
			port=int(port)
	)
)

channel = connection.channel()

channel.exchange_declare(exchange=exchange,
                         type='topic')

channel.basic_publish(exchange=exchange,
                      routing_key=key,
                      body=body)
connection.close()
