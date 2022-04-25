# Apache Pulsar
Apache Pulsar is a cloud-native, distributed messaging and streaming platform.

---

https://pulsar.apache.org/

https://pulsar.apache.org/en/download/

---

## For this demo, we will use ` Apache Pulsar version 2.8.2 `.

```
### we will install and configure Apache Pulsar to run on this server as a standalone :

192.168.1.124 crysis4 crysis4.OracleByExample.com
```

```
cd ~/software

wget https://archive.apache.org/dist/pulsar/pulsar-2.8.2/apache-pulsar-2.8.2-bin.tar.gz


$ ls -lh ~/software
-rw-r--r-- 1 cassandra cassgrp 320M Dec 20 00:34 apache-pulsar-2.8.2-bin.tar.gz
$


cd ~
tar -xzvf ~/software/apache-pulsar-2.8.2-bin.tar.gz
ln -s ~/apache-pulsar-2.8.2 ~/pulsar-current


mkdir ~/pulsar-current/statusFiles
mkdir ~/pulsar-current/logs

```

---

## Apache Pulsar Configuration Files

### vi ~/pulsar-current/conf/standalone.conf

```
### customize the clusterName
# clusterName=standalone
clusterName=MyPulsarCluster


### configure statusFiles to custom path
# statusFilePath=/usr/local/apache/htdocs
statusFilePath=/apps/opt/cassandra/pulsar-current/statusFiles

```

<br>

### vi ~/pulsar-current/conf/pulsar_env.sh

```
### configure PID file to custom path
PULSAR_PID_DIR=/apps/opt/cassandra/pulsar-current/logs
```

---

### Other important configuration values - no changes are required

```
$ cat ~/pulsar-current/conf/standalone.conf | egrep "brokerServicePort|webServicePort"

brokerServicePort=6650
webServicePort=8080
```

```
$ cat ~/pulsar-current/conf/pulsar_env.sh | egrep "PULSAR_LOG_DIR|PULSAR_MEM"

# PULSAR_LOG_DIR=
PULSAR_MEM=${PULSAR_MEM:-"-Xms2g -Xmx2g -XX:MaxDirectMemorySize=4g"}
```

---

## Start & Stop Pulsar in Standalone mode

```
# start :
~/pulsar-current/bin/pulsar-daemon start standalone


# stop :
~/pulsar-current/bin/pulsar-daemon stop  standalone


# find pulsar process
ps -ef | grep `cat ~/pulsar-current/logs/pulsar-standalone.pid`
ps -ef | grep -i pulsar


# pulsar log
tail -f ~/pulsar-current/logs/pulsar-standalone-`hostname`.log
```

---

## During initial startup of Pulsar, it will create following folders :

```
~/pulsar-current/data
~/pulsar-current/instances
~/pulsar-current/logs
```

---

## Pulsar URLs :

```

Pulsar webServiceUrl    : http://192.168.1.124:8080/

Pulsar brokerServiceUrl : pulsar://192.168.1.124:6650/

Prometheus Metrics URL  : http://192.168.1.124:8080/metrics/

```

---

