########
import pulsar

client = pulsar.Client('pulsar://192.168.1.124:6650')

consumer = client.subscribe('persistent://sales_tenant/sales_ns/data-sales.sales_orders', 'pyClient_Subscription')

while True:
    msg = consumer.receive()
    try:
        # print("Received message '{}' id='{}'".format(msg.data(), msg.message_id()))
        print("Received message id='{}'".format(msg.message_id()))

	# Acknowledge successful processing of the message
        consumer.acknowledge(msg)
    except:
        # Message failed to be processed
        consumer.negative_acknowledge(msg)

client.close()
########

