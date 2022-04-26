# Apache Cassandra CDC to Apache Pulsar
Apache Cassandra Change-Data-Capture to Apache Pulsar

---

![CassCDCPulsarArch.jpg](https://github.com/sarma1807/Cassandra_CDC-to-Pulsar/blob/main/CassCDCPulsarArch.jpg)

---

### Environment

##### Following servers are running with ` CentOS Stream release 8 ` & ` Apache Cassandra 4.0.3 ` :
```
192.168.1.121 crysis1 crysis1.OracleByExample.com
192.168.1.122 crysis2 crysis2.OracleByExample.com
192.168.1.123 crysis3 crysis3.OracleByExample.com
```

---

##### Following server is running with ` CentOS Stream release 8 ` :
```
192.168.1.124 crysis4 crysis4.OracleByExample.com
```
##### This server is also running a python app ` SalesApp_AutoSalesGenerator ` which generates Sales data and stores into Apache Cassandra Database. 
Please check : https://github.com/sarma1807/python-cassandra-driver/tree/master/31_SalesApp_AutoSalesGenerator

### We will configure and run Apache Pulsar on this server.

---

##### Following server is running with ` CentOS Stream release 8 ` & ` Prometheus & Grafana ` :
```
192.168.1.125 crysis5 crysis5.OracleByExample.com
```

---

![91_CDCPromGraf_00.jpg](https://github.com/sarma1807/Cassandra_CDC-to-Pulsar/blob/main/91_CDCPromGraf_00.jpg)

<br><br>
