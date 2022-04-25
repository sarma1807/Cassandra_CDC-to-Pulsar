# Pulsar-Cassandra-Source
This package is developed by DataStax as an open-source project. <br>
This source will use the event info to fetch the actual data from Cassandra and publish it to Apache Pulsar as an ` Data Topic `.

https://github.com/datastax/cdc-apache-cassandra

---

For this demo, we will use ` Release v1.0.5 `

---

## Download Pulsar-Cassandra-Source-<version>.nar (yes nar - not a typo)
## on Apache Pulsar server :

```
mkdir ~/pulsar-current/connectors
cd    ~/pulsar-current/connectors

wget https://github.com/datastax/cdc-apache-cassandra/releases/download/v1.0.5/pulsar-cassandra-source-1.0.5.nar

$ ls -lh
-rw-r--r-- 1 cassandra cassgrp 81M Apr 11 10:35 pulsar-cassandra-source-1.0.5.nar
$


# reload new sources
~/pulsar-current/bin/pulsar-admin sources reload

# verify available sources
~/pulsar-current/bin/pulsar-admin sources available-sources

$
cassandra-source
Read data from Cassandra
$

```

---

# pulsar-io-cassandra-<version>.nar WILL NOT WORK

## NOTE THAT ` Apache Cassandra Source and Sink ` available under ` Pulsar IO connectors ` on following webpage : https://pulsar.apache.org/en/download/

# WILL NOT WORK

---

## Let us now create a new Pulsar-Cassandra-Source for our CDC data

#### first create a YAML config file

` $ vi ~/pulsar-current/conf/cass-source.yaml `

```
#########
configs:
  keyspace: "sales"
  table: "sales_orders"
  events.topic: "persistent://sales_tenant/sales_ns/events-sales.sales_orders"
  events.subscription.name: "cass_cdc_events_sub"
  contactPoints: "192.168.1.122,192.168.1.123"
  loadBalancing.localDc: "east_dc"
  port: "9042"
  auth.provider: "PLAIN"
  auth.username: "sales_user"
  auth.password: "PassCode"
#########
```


#### create Pulsar-Cassandra-Source

```
# create source
~/pulsar-current/bin/pulsar-admin sources create --name cassandra-source-sales-sales_orders --source-type cassandra-source --tenant public --namespace default --destination-topic-name persistent://sales_tenant/sales_ns/data-sales.sales_orders --parallelism 1 --source-config-file ~/pulsar-current/conf/cass-source.yaml

"Created successfully"

# NOTE : tenant set to public and namespace to default : any other values will cause problems and source will not work
# --tenant public
# --namespace default
# --destination-topic-name persistent://sales_tenant/sales_ns/data-sales.sales_orders

```


#### verify Pulsar-Cassandra-Source

```
# list sources
~/pulsar-current/bin/pulsar-admin sources list

$
[
  "cassandra-source-sales-sales_orders"
]
$


# source status
~/pulsar-current/bin/pulsar-admin sources status --name cassandra-source-sales-sales_orders

{
  "numInstances" : 1,
  "numRunning" : 1,
  "instances" : [ {
    "instanceId" : 0,
    "status" : {
      "running" : true,
      "error" : "",
      "numRestarts" : 0,
      "numReceivedFromSource" : 203,
      "numSystemExceptions" : 0,
      "latestSystemExceptions" : [ ],
      "numSourceExceptions" : 0,
      "latestSourceExceptions" : [ ],
      "numWritten" : 203,
      "lastReceivedTime" : 1650923045856,
      "workerId" : "c-MyPulsarCluster-fw-localhost-8080"
    }
  } ]
}


# get source config
~/pulsar-current/bin/pulsar-admin sources get --name cassandra-source-sales-sales_orders

{
  "tenant": "public",
  "namespace": "default",
  "name": "cassandra-source-sales-sales_orders",
  "className": "com.datastax.oss.pulsar.source.CassandraSource",
  "topicName": "persistent://sales_tenant/sales_ns/data-sales.sales_orders",
  "producerConfig": {
    "useThreadLocalProducers": false,
    "batchBuilder": ""
  },
  "configs": {
    "loadBalancing.localDc": "east_dc",
    "keyspace": "sales",
    "auth.password": "PassCode",
    "port": "9042",
    "events.topic": "persistent://sales_tenant/sales_ns/events-sales.sales_orders",
    "contactPoints": "192.168.1.122,192.168.1.123",
    "events.subscription.name": "cass_cdc_events_sub",
    "auth.provider": "PLAIN",
    "table": "sales_orders",
    "auth.username": "sales_user"
  },
  "parallelism": 1,
  "processingGuarantees": "ATLEAST_ONCE",
  "resources": {
    "cpu": 1.0,
    "ram": 1073741824,
    "disk": 10737418240
  },
  "archive": "builtin://cassandra-source"
}


# if source needs a restart
~/pulsar-current/bin/pulsar-admin sources restart --name cassandra-source-sales-sales_orders

```


#### list Pulsar topics

```
~/pulsar-current/bin/pulsar-admin topics list "sales_tenant/sales_ns"

$
"persistent://sales_tenant/sales_ns/events-sales.sales_orders"
"persistent://sales_tenant/sales_ns/data-sales.sales_orders"
$


#### now we have both events and data :
#### events published by CDC Agent from Cassandra Nodes
#### data   published by Pulsar-Cassandra-Source

```


#### check stats for Pulsar topics

```

# see how many events are produced and who produced them

~/pulsar-current/bin/pulsar-admin topics stats "persistent://sales_tenant/sales_ns/events-sales.sales_orders" | egrep "msgInCounter|address|consumerName"

$
  "msgInCounter" : 2010,
    "address" : "/192.168.1.121:52206",
    "address" : "/192.168.1.123:37820",
    "address" : "/192.168.1.122:37044",
        "consumerName" : "CDC Consumer",
        "address" : "/127.0.0.1:33642",
$



~/pulsar-current/bin/pulsar-admin topics stats "persistent://sales_tenant/sales_ns/data-sales.sales_orders" | egrep "msgInCounter|address|consumerName"

$
  "msgInCounter" : 593,
    "address" : "/127.0.0.1:33642",
$

```


#### check Pulsar Data topic

```

# verify the incoming DATA messages using pulsar client :
~/pulsar-current/bin/pulsar-client --url pulsar://192.168.1.124:6650/ consume "persistent://sales_tenant/sales_ns/data-sales.sales_orders" --subscription-name "mySub" --num-messages 3


----- got message -----
key:[xqoCIgLA2u2djGACSDNkM2VlMDU5LTM5MjYtNDQ1Yy05Njc5LTIwOGY1NTNjOWNhMQ==], properties:[writetime=1650923761909700], content:~K2ecaa37c21cb4@fastmail.comGecaa37c21cb4874-847-6038ChromeBookVA
----- got message -----
key:[xqoCIgL02+2djGACSGIzY2EyODU2LTZhMTItNDFhYi05NWI1LWI4YmI4YjMyOWJkZQ==], properties:[writetime=1650923761985345], content:){]2a8272c54ccc4@hushmail.com(a8272c54ccc4766-715-9373iPhoneSD
----- got message -----
key:[xqoCIgKK3e2djGACSDg2OTJiOTQ5LWMxNDctNGJmNC1hMmUzLWU1MjBkOWM4ZjViNA==], properties:[writetime=1650923762082706], content:rBrB,d335d5e92784@email.netVd335d5e92784878-198-2203LinuxUT
-----------------------
```


#### Pulsar-Cassandra-Source logs

```
ls -lh ~/pulsar-current/logs/functions/public/default/cassandra-source-sales-sales_orders/

$
-rw-r--r-- 1 cassandra cassgrp 5.3K Apr 25 12:33 cassandra-source-sales-sales_orders-0-04-24-2022-1.log.gz
-rw-r--r-- 1 cassandra cassgrp    0 Apr 24 21:58 cassandra-source-sales-sales_orders-0.bk
-rw-r--r-- 1 cassandra cassgrp 174K Apr 25 17:58 cassandra-source-sales-sales_orders-0.log
$

```

---

#### DELETE Pulsar-Cassandra-Source

```
# if you ever need to delete the cassandra-source-sales-sales_orders
# ~/pulsar-current/bin/pulsar-admin sources delete --name cassandra-source-sales-sales_orders

```

