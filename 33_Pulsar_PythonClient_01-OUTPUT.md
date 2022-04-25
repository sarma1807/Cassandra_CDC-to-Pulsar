### output of 
### python 32_Pulsar_PythonClient_01.py

```
2022-04-25 18:26:19.869 INFO  [140021667613568] Client:88 | Subscribing on Topic :persistent://sales_tenant/sales_ns/data-sales.sales_orders
2022-04-25 18:26:19.869 INFO  [140021667613568] ClientConnection:189 | [<none> -> pulsar://192.168.1.124:6650] Create ClientConnection, timeout=10000
2022-04-25 18:26:19.870 INFO  [140021667613568] ConnectionPool:96 | Created connection for pulsar://192.168.1.124:6650
2022-04-25 18:26:19.870 INFO  [140021607356160] ClientConnection:375 | [192.168.1.124:49826 -> 192.168.1.124:6650] Connected to broker
2022-04-25 18:26:19.875 INFO  [140021607356160] HandlerBase:64 | [persistent://sales_tenant/sales_ns/data-sales.sales_orders, pyClient_Subscription, 0] Getting connection from pool
2022-04-25 18:26:19.876 INFO  [140021607356160] ClientConnection:189 | [<none> -> pulsar://192.168.1.124:6650] Create ClientConnection, timeout=10000
2022-04-25 18:26:19.876 INFO  [140021607356160] ConnectionPool:96 | Created connection for pulsar://localhost:6650
2022-04-25 18:26:19.876 INFO  [140021607356160] ClientConnection:377 | [192.168.1.124:49828 -> 192.168.1.124:6650] Connected to broker through proxy. Logical broker: pulsar://localhost:6650
2022-04-25 18:26:19.878 INFO  [140021607356160] ConsumerImpl:224 | [persistent://sales_tenant/sales_ns/data-sales.sales_orders, pyClient_Subscription, 0] Created consumer on broker [192.168.1.124:49828 -> 192.168.1.124:6650]
Received message id='(524,66,-1,0)'
Received message id='(524,66,-1,1)'
Received message id='(524,66,-1,2)'
Received message id='(524,66,-1,3)'
Received message id='(524,66,-1,4)'
Received message id='(524,66,-1,5)'
Received message id='(524,66,-1,6)'
Received message id='(524,66,-1,7)'
Received message id='(524,66,-1,8)'
Received message id='(524,66,-1,9)'
Received message id='(524,66,-1,10)'
Received message id='(524,66,-1,11)'
Received message id='(524,66,-1,12)'
Received message id='(524,66,-1,13)'
Received message id='(524,66,-1,14)'
Received message id='(524,66,-1,15)'
Received message id='(524,66,-1,16)'
Received message id='(524,66,-1,17)'
^C^C^C^C^C^C^CTraceback (most recent call last):
  File "first.py", line 9, in <module>
    msg = consumer.receive()
  File "/usr/local/lib64/python3.6/site-packages/pulsar/__init__.py", line 1130, in receive
    msg = self._consumer.receive()
KeyboardInterrupt
2022-04-25 18:28:05.877 INFO  [140021667613568] ClientConnection:1559 | [192.168.1.124:49826 -> 192.168.1.124:6650] Connection closed
2022-04-25 18:28:05.877 INFO  [140021667613568] ClientConnection:1559 | [192.168.1.124:49828 -> 192.168.1.124:6650] Connection closed
```

