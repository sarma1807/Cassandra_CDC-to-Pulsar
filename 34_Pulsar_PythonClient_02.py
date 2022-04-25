########
import pulsar
from pulsar.schema import *

client = pulsar.Client('pulsar://192.168.1.124:6650')

consumer = client.subscribe( topic='persistent://sales_tenant/sales_ns/data-sales.sales_orders', subscription_name='pyClient_Subscription', schema=AvroSchema('data-sales.sales_orders') )

while True:
    msg = consumer.receive()
    rec = msg.value()
    try:
        print("Received message order_date={} order_grand_total={}".format( rec.order_date, rec.order_grand_total ))

	# Acknowledge successful processing of the message
        consumer.acknowledge(msg)
    except:
        # Message failed to be processed
        consumer.negative_acknowledge(msg)

client.close()
########

