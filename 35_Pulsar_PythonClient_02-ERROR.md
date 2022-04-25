### output of 
### python 34_Pulsar_PythonClient_02.py

```
Traceback (most recent call last):
  File "two.py", line 7, in <module>
    consumer = client.subscribe( topic='persistent://sales_tenant/sales_ns/data-sales.sales_orders', subscription_name='pyClient_Subscription', schema=AvroSchema('data-sales.sales_orders') )
TypeError: __init__() missing 1 required positional argument: '_schema_definition'
```

# I HAVE NO CLUE ON HOW TO READ THE AVRO SCHEMA FROM PULSAR SCHEMA REGISTRY

