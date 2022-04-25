# CDC Agent for Apache Cassandra
This Agent is developed by DataStax as an open-source project.
This agent will read the CDC data and publish it to Apache Pulsar as an ` Event Topic `.

https://github.com/datastax/cdc-apache-cassandra

---

For this demo, we will use ` Release v1.0.5 `

---

## Download Agent-Cass-Pulsar-<version>.jar
## on all Cassandra nodes :

```
cd <CASSANDRA_HOME>/lib/

wget https://github.com/datastax/cdc-apache-cassandra/releases/download/v1.0.5/agent-c4-pulsar-1.0.5-all.jar



ls -lh agent-c4-pulsar-1.0.5-all.jar

$
-rw-r--r-- 1 cassandra cassgrp 40M Apr 12 20:19 agent-c4-pulsar-1.0.5-all.jar
$

```


## Configure Agent-Cass-Pulsar-<version>.jar
## on all Cassandra nodes :

## vi <CASSANDRA_HOME>/conf/cassandra-env.sh

```
## add following settings 1 line above : JVM_OPTS="$JVM_OPTS $JVM_EXTRA_OPTS"

#### needed when Pulsar JWT Authentication is ENABLED
# export CDC_PULSAR_AUTH_PLUGIN_CLASS_NAME="org.apache.pulsar.client.impl.auth.AuthenticationToken"
# export CDC_PULSAR_AUTH_PARAMS="file://</path/to/token/file>"
#### needed when Pulsar TLS Encryption is ENABLED
# export CDC_TLS_TRUST_CERTS_FILE_PATH="</path/to/trusted/cert/file>"

# agent temp files
export CDC_WORKING_DIR="/apps/opt/cassandra/data/cdc_raw"

# pre-create tenant/namespace on Pulsar
export CDC_TOPIC_PREFIX="sales_tenant/sales_ns/events-"

# Pulsar Service URL
export CDC_PULSAR_SERVICE_URL="pulsar://192.168.1.124:6650/"

# include agent jar
JVM_OPTS="$JVM_OPTS -javaagent:$CASSANDRA_HOME/lib/agent-c4-pulsar-1.0.5-all.jar"

```

### Restart all nodes in the Cassandra cluster to Enable CDC Agent


```
# log messages for Pulsar/CDC_Agent
cat <CASSANDRA_LOGS>/system.log | egrep -i "cdc|pulsar"


# config settings for Pulsar/CDC_Agent
cat <CASSANDRA_LOGS>/system.log | egrep "AgentConfig.java"
```

---

# DataStax CDC Agent will start pushing CDC changes from Cassandra to Pulsar

### if CDC_TOPIC_PREFIX is NOT pre-configured in cassandra-env.sh : on Pulsar, cdc_agent will by default publish messages to a topic in "public" tenant with "default" namespace.

### if CDC_TOPIC_PREFIX is pre-configured in cassandra-env.sh : on Pulsar, cdc_agent will publish messages to a topic in pre-configured "tenant/namespace".

### Topic Name : events-<cassandra_keyspace>.<cassandra_table>

---

## on Pulsar server :

```
~/pulsar-current/bin/pulsar-admin topics list "public/default"

~/pulsar-current/bin/pulsar-admin topics list "sales_tenant/sales_ns"

$
"persistent://sales_tenant/sales_ns/events-sales.sales_orders"
$


# check how many events are produced and who produced them
~/pulsar-current/bin/pulsar-admin topics stats "persistent://sales_tenant/sales_ns/events-sales.sales_orders" | egrep "msgInCounter|address|consumerName"

$
  "msgInCounter" : 42264,
    "address" : "/192.168.1.121:52206",
    "address" : "/192.168.1.123:37820",
    "address" : "/192.168.1.122:37044",
        "consumerName" : "CDC Consumer",
        "address" : "/127.0.0.1:59670",
$



# verify the incoming messages using pulsar client :
~/pulsar-current/bin/pulsar-client --url pulsar://192.168.1.124:6650/ consume "persistent://sales_tenant/sales_ns/events-sales.sales_orders" --subscription-name "mySub" --num-messages 3


----- got message -----
key:[xqoCIgLgq/GajGACSDNhZDE0Nzg0LTJjZDQtNDQ4ZS1hZjQwLWFkODY1MWU1OGNiZQ==], properties:[segpos=1650895445487:17106851, writetime=1650920646031841, token=1926680084403078048], content:@54e0f9aea50aba5c225c5bda13ff52c2H59b24ea3-4ce6-4656-9327-1316bb4ad028
----- got message -----
key:[xqoCIgKorvGajGACSDg1NGVlY2VlLTg0ZGQtNDBiOC05MDY4LTkxZjRlODllMTcyOA==], properties:[segpos=1650895445487:17110689, writetime=1650920646133922, token=1926680084403078048], content:@0f0ca7a2fc0479b5d0b6918b7ef5fd2bH59b24ea3-4ce6-4656-9327-1316bb4ad028
----- got message -----
key:[xqoCIgL0r/GajGACSGY4YTE1MjFiLTQxOWEtNDgwZS04ZjNhLWVjZDRjZGM4ZjJkNg==], properties:[segpos=1650895445487:17113407, writetime=1650920646203421, token=1926680084403078048], content:@35aec2a9b7366da8b16aa02fa3aaf8feH59b24ea3-4ce6-4656-9327-1316bb4ad028
-----------------------

```

### These are just CDC events which inform Pulsar about which segments on Cassandra have changed.

### Now we have to configure the Pulsar-Cassandra-Source to have Pulsar pull the required changes (actual changed data) from Cassandra.

---

```
# cassandra log after CDC Agent publishes events to Pulsar
$ tail -f <CASSANDRA_LOGS>/system.log | egrep -i --line-buffered "PULSAR"


INFO  [pulsar-timer-5-1] 2022-04-23 22:14:09,400 ProducerStatsRecorderImpl.java:145 - [sales_tenant/sales_ns/events-sales.sales_orders] [cdc-producer-603bcabc-5d54-4abf-a49b-cfd1713d1d49-sales.sales_orders] Pending messages: 0 --- Publish throughput: 0.55 msg/s --- 0.00 Mbit/s --- Latency: med: 27.000 ms - 95pct: 40.000 ms - 99pct: 40.000 ms - 99.9pct: 40.000 ms - max: 40.000 ms --- Ack received rate: 0.55 ack/s --- Failed messages: 0
```

