# ISSUES : NEED-YOUR-HELP

---

### 1. columns OPTION FOR Pulsar-Cassandra-Source

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
  columns: "user_email_id,user_state_code,order_grand_total"
  # columns: NOT WORKING : Pulsar-Cassandra-Source gets created but with bunch of JAVA errors it will never go into RUNNING mode
  # errors are so cryptic - I have no clue what is wrong with this
#########
```

---

### 2. Python client : How to fetch and use AVRO schema

```
we know that : Cassandra CDC Agent & Source Connector will publish the schema in AVRO format to Pulsar Schema Registry.


for :
https://github.com/sarma1807/Cassandra_CDC-to-Pulsar/blob/main/34_Pulsar_PythonClient_02.py


client.subscribe( topic='', subscription_name='', schema???=AvroSchema???('data-sales.sales_orders') )

I HAVE NO CLUE ON HOW TO READ & USE THE AVRO SCHEMA FROM PULSAR SCHEMA REGISTRY

VERY LITTLE TO NONE DOCUMENTATION/EXAMPLES EXIST BOTH FROM DATASTAX AND PULSAR PROJECTS
```

---

### 3. Prometheus Grafana

```
ACCORDING TO :
https://github.com/datastax/cdc-apache-cassandra#monitoring


looks like it is possible to publish and build dashboards for CDC metrics
but ZERO DOCUMENTATION on who publishes these metrics and how ?
how to extract ? from where ?

Team DataStax ???

```
---

