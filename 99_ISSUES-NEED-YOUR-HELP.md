# ISSUES : NEED-YOUR-HELP

---

## RESOLVED : 1. columns OPTION FOR Pulsar-Cassandra-Source

```
~/pulsar-current/conf/cass-source.yaml IN :
https://github.com/sarma1807/Cassandra_CDC-to-Pulsar/blob/main/22_Pulsar-Cassandra-Source.md



ACCORDING TO :
https://github.com/datastax/cdc-apache-cassandra/blob/master/connector/src/main/java/com/datastax/oss/cdc/CassandraSourceConnectorConfig.java



vi ~/pulsar-current/conf/cass-source.yaml
#########
configs:
  keyspace: "sales"
  table: "sales_orders"
  # WRONG SYNTAX : columns: "user_email_id,user_state_code,order_grand_total"
  columns: "user_email_id|user_state_code|order_grand_total"
  # columns: column separator is NOT COMMA - it is PIPE
#########
```

---

## 2. Python client : How to fetch and use AVRO schema

```
we know that : Cassandra CDC Agent & Source Connector will publish the schema in AVRO format to Pulsar Schema Registry.


for :
https://github.com/sarma1807/Cassandra_CDC-to-Pulsar/blob/main/34_Pulsar_PythonClient_02.py


client.subscribe( topic='', subscription_name='', schema???=AvroSchema???('data-sales.sales_orders') )

I HAVE NO CLUE ON HOW TO READ & USE THE AVRO SCHEMA FROM PULSAR SCHEMA REGISTRY

VERY LITTLE TO NONE DOCUMENTATION/EXAMPLES EXIST BOTH FROM DATASTAX AND PULSAR PROJECTS
```

---

## RESOLVED : 3. Prometheus Grafana (needs JMX/Metric Collector for Apache Cassandra (MCAC))

```
ACCORDING TO :
https://github.com/datastax/cdc-apache-cassandra#monitoring


Basically the CDC agent exposes JMX metrics (as part of DSE metrics).
We can use DSE Metrics Collector to expose the CDC metrics like other DSE metrics - this 
is a capability related to monitoring DSE and is not specific to Pulsar.

MCAC : https://github.com/datastax/metric-collector-for-apache-cassandra

```
---

