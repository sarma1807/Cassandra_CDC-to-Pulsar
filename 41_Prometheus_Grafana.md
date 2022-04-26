# Prometheus & Grafana

### Apache Pulsar by default out-of-the-box will publish metrics in the Prometheus format

```
Prometheus Metrics URL  : http://192.168.1.124:8080/metrics/
```

check :

https://github.com/sarma1807/Cassandra_CDC-to-Pulsar/blob/main/42_Pulsar_Prometheus_Metrics.md

---

## configure Prometheus to scrape for Pulsar metrics

` $ vi ~/prometheus-current/prometheus.yml `

```
# YAML files are sensitive about spaces/tabs - extra spaces/tabs can result in errors
# add following entries at the end of file
  # my pulsar metrics
  - job_name: 'pulsar_metrics'
    scrape_interval: 180s
    metrics_path: '/metrics'
    scheme: 'http'
    static_configs:
    # - targets: ['<SERVER1_IP_OR_HOSTNAME>:<PORT>', '<SERVER2_IP_OR_HOSTNAME>:<PORT>', ...]
    - targets: ['192.168.1.124:8080']
# add your pulsar servers to this targets list
```

---

## Grafana Dashboard

```
http://<GRAFANA_IP_OR_HOSTNAME>:3000/dashboard/import

Click on "Upload JSON file" button.

Download and select "43_GrafanaDashboard_20220425_01.json" from following URL :
https://github.com/sarma1807/Cassandra_CDC-to-Pulsar/blob/main/43_GrafanaDashboard_20220425_01.json


Under "Options" - select "Prometheus" as your data source.

Click on "Import" button.
```


## Enjoy the Cassandra CDC to Pulsar Dashboard by ORAMAD

![91_CDCPromGraf_00.jpg](https://github.com/sarma1807/Cassandra_CDC-to-Pulsar/blob/main/91_CDCPromGraf_00.jpg)

---

