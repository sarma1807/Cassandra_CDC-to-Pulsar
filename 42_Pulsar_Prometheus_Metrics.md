# Pulsar Prometheus Metrics

```
# TYPE pulsar_broker_lookup_answers counter
pulsar_broker_lookup_answers{cluster="MyPulsarCluster"} 12.0
# TYPE pulsar_broker_lookup summary
pulsar_broker_lookup{cluster="MyPulsarCluster",quantile="0.5"} NaN
pulsar_broker_lookup{cluster="MyPulsarCluster",quantile="0.99"} NaN
pulsar_broker_lookup{cluster="MyPulsarCluster",quantile="0.999"} NaN
pulsar_broker_lookup{cluster="MyPulsarCluster",quantile="1.0"} -Inf
pulsar_broker_lookup_count{cluster="MyPulsarCluster"} 12.0
pulsar_broker_lookup_sum{cluster="MyPulsarCluster"} 64.0
# TYPE zk_write_latency summary
zk_write_latency{cluster="MyPulsarCluster",quantile="0.5"} NaN
zk_write_latency{cluster="MyPulsarCluster",quantile="0.75"} NaN
zk_write_latency{cluster="MyPulsarCluster",quantile="0.95"} NaN
zk_write_latency{cluster="MyPulsarCluster",quantile="0.99"} NaN
zk_write_latency{cluster="MyPulsarCluster",quantile="0.999"} NaN
zk_write_latency{cluster="MyPulsarCluster",quantile="0.9999"} NaN
zk_write_latency_count{cluster="MyPulsarCluster"} 0.0
zk_write_latency_sum{cluster="MyPulsarCluster"} 0.0
# TYPE jvm_threads_current gauge
jvm_threads_current{cluster="MyPulsarCluster"} 233.0
# TYPE jvm_threads_daemon gauge
jvm_threads_daemon{cluster="MyPulsarCluster"} 50.0
# TYPE jvm_threads_peak gauge
jvm_threads_peak{cluster="MyPulsarCluster"} 233.0
# TYPE jvm_threads_started_total counter
jvm_threads_started_total{cluster="MyPulsarCluster"} 334.0
# TYPE jvm_threads_deadlocked gauge
jvm_threads_deadlocked{cluster="MyPulsarCluster"} 0.0
# TYPE jvm_threads_deadlocked_monitor gauge
jvm_threads_deadlocked_monitor{cluster="MyPulsarCluster"} 0.0
# TYPE log4j2_appender_total counter
log4j2_appender_total{cluster="MyPulsarCluster",level="debug"} 0.0
log4j2_appender_total{cluster="MyPulsarCluster",level="warn"} 707.0
log4j2_appender_total{cluster="MyPulsarCluster",level="trace"} 0.0
log4j2_appender_total{cluster="MyPulsarCluster",level="error"} 4.0
log4j2_appender_total{cluster="MyPulsarCluster",level="fatal"} 0.0
log4j2_appender_total{cluster="MyPulsarCluster",level="info"} 1062.0
# TYPE pulsar_broker_lookup_pending_requests gauge
pulsar_broker_lookup_pending_requests{cluster="MyPulsarCluster"} 0.0
# TYPE jvm_info gauge
jvm_info{cluster="MyPulsarCluster",version="1.8.0_322-b06",vendor="Red Hat, Inc.",runtime="OpenJDK Runtime Environment"} 1.0
# TYPE jvm_classes_loaded gauge
jvm_classes_loaded{cluster="MyPulsarCluster"} 15857.0
# TYPE jvm_classes_loaded_total counter
jvm_classes_loaded_total{cluster="MyPulsarCluster"} 15857.0
# TYPE jvm_classes_unloaded_total counter
jvm_classes_unloaded_total{cluster="MyPulsarCluster"} 0.0
# TYPE pulsar_broker_topic_load_pending_requests gauge
pulsar_broker_topic_load_pending_requests{cluster="MyPulsarCluster"} 0.0
# TYPE jvm_memory_bytes_used gauge
jvm_memory_bytes_used{cluster="MyPulsarCluster",area="heap"} 1.11512424E9
jvm_memory_bytes_used{cluster="MyPulsarCluster",area="nonheap"} 1.3169116E8
# TYPE jvm_memory_bytes_committed gauge
jvm_memory_bytes_committed{cluster="MyPulsarCluster",area="heap"} 2.147483648E9
jvm_memory_bytes_committed{cluster="MyPulsarCluster",area="nonheap"} 1.39419648E8
# TYPE jvm_memory_bytes_max gauge
jvm_memory_bytes_max{cluster="MyPulsarCluster",area="heap"} 2.147483648E9
jvm_memory_bytes_max{cluster="MyPulsarCluster",area="nonheap"} -1.0
# TYPE jvm_memory_bytes_init gauge
jvm_memory_bytes_init{cluster="MyPulsarCluster",area="heap"} 2.147483648E9
jvm_memory_bytes_init{cluster="MyPulsarCluster",area="nonheap"} 2555904.0
# TYPE jvm_memory_pool_bytes_used gauge
jvm_memory_pool_bytes_used{cluster="MyPulsarCluster",pool="Code Cache"} 2.8832896E7
jvm_memory_pool_bytes_used{cluster="MyPulsarCluster",pool="Metaspace"} 9.1725792E7
jvm_memory_pool_bytes_used{cluster="MyPulsarCluster",pool="Compressed Class Space"} 1.1132472E7
jvm_memory_pool_bytes_used{cluster="MyPulsarCluster",pool="G1 Eden Space"} 1.030750208E9
jvm_memory_pool_bytes_used{cluster="MyPulsarCluster",pool="G1 Survivor Space"} 4.194304E7
jvm_memory_pool_bytes_used{cluster="MyPulsarCluster",pool="G1 Old Gen"} 4.2430992E7
# TYPE jvm_memory_pool_bytes_committed gauge
jvm_memory_pool_bytes_committed{cluster="MyPulsarCluster",pool="Code Cache"} 2.9425664E7
jvm_memory_pool_bytes_committed{cluster="MyPulsarCluster",pool="Metaspace"} 9.7726464E7
jvm_memory_pool_bytes_committed{cluster="MyPulsarCluster",pool="Compressed Class Space"} 1.226752E7
jvm_memory_pool_bytes_committed{cluster="MyPulsarCluster",pool="G1 Eden Space"} 1.086324736E9
jvm_memory_pool_bytes_committed{cluster="MyPulsarCluster",pool="G1 Survivor Space"} 4.194304E7
jvm_memory_pool_bytes_committed{cluster="MyPulsarCluster",pool="G1 Old Gen"} 1.019215872E9
# TYPE jvm_memory_pool_bytes_max gauge
jvm_memory_pool_bytes_max{cluster="MyPulsarCluster",pool="Code Cache"} 2.5165824E8
jvm_memory_pool_bytes_max{cluster="MyPulsarCluster",pool="Metaspace"} -1.0
jvm_memory_pool_bytes_max{cluster="MyPulsarCluster",pool="Compressed Class Space"} 1.073741824E9
jvm_memory_pool_bytes_max{cluster="MyPulsarCluster",pool="G1 Eden Space"} -1.0
jvm_memory_pool_bytes_max{cluster="MyPulsarCluster",pool="G1 Survivor Space"} -1.0
jvm_memory_pool_bytes_max{cluster="MyPulsarCluster",pool="G1 Old Gen"} 2.147483648E9
# TYPE jvm_memory_pool_bytes_init gauge
jvm_memory_pool_bytes_init{cluster="MyPulsarCluster",pool="Code Cache"} 2555904.0
jvm_memory_pool_bytes_init{cluster="MyPulsarCluster",pool="Metaspace"} 0.0
jvm_memory_pool_bytes_init{cluster="MyPulsarCluster",pool="Compressed Class Space"} 0.0
jvm_memory_pool_bytes_init{cluster="MyPulsarCluster",pool="G1 Eden Space"} 1.128267776E9
jvm_memory_pool_bytes_init{cluster="MyPulsarCluster",pool="G1 Survivor Space"} 0.0
jvm_memory_pool_bytes_init{cluster="MyPulsarCluster",pool="G1 Old Gen"} 1.019215872E9
# TYPE process_cpu_seconds_total counter
process_cpu_seconds_total{cluster="MyPulsarCluster"} 71.38
# TYPE process_start_time_seconds gauge
process_start_time_seconds{cluster="MyPulsarCluster"} 1.650931190017E9
# TYPE process_open_fds gauge
process_open_fds{cluster="MyPulsarCluster"} 604.0
# TYPE process_max_fds gauge
process_max_fds{cluster="MyPulsarCluster"} 100000.0
# TYPE process_virtual_memory_bytes gauge
process_virtual_memory_bytes{cluster="MyPulsarCluster"} 7.093997568E9
# TYPE process_resident_memory_bytes gauge
process_resident_memory_bytes{cluster="MyPulsarCluster"} 1.546543104E9
# TYPE pulsar_broker_throttled_connections_global_limit gauge
pulsar_broker_throttled_connections_global_limit{cluster="MyPulsarCluster"} 0.0
# TYPE jvm_buffer_pool_used_bytes gauge
jvm_buffer_pool_used_bytes{cluster="MyPulsarCluster",pool="direct"} 921913.0
jvm_buffer_pool_used_bytes{cluster="MyPulsarCluster",pool="mapped"} 0.0
# TYPE jvm_buffer_pool_capacity_bytes gauge
jvm_buffer_pool_capacity_bytes{cluster="MyPulsarCluster",pool="direct"} 921911.0
jvm_buffer_pool_capacity_bytes{cluster="MyPulsarCluster",pool="mapped"} 0.0
# TYPE jvm_buffer_pool_used_buffers gauge
jvm_buffer_pool_used_buffers{cluster="MyPulsarCluster",pool="direct"} 77.0
jvm_buffer_pool_used_buffers{cluster="MyPulsarCluster",pool="mapped"} 0.0
# TYPE jvm_memory_direct_bytes_max gauge
jvm_memory_direct_bytes_max{cluster="MyPulsarCluster"} 4.294967296E9
# TYPE pulsar_broker_lookup_failures counter
pulsar_broker_lookup_failures{cluster="MyPulsarCluster"} 0.0
# TYPE pulsar_broker_lookup_redirects counter
pulsar_broker_lookup_redirects{cluster="MyPulsarCluster"} 0.0
# TYPE pulsar_version_info gauge
pulsar_version_info{cluster="MyPulsarCluster",version="2.8.2",commit="4b9cadcd57e41bc8eb95cc9b9917f938365b1cca"} 1.0
# TYPE jetty_requests_total counter
jetty_requests_total{cluster="MyPulsarCluster"} 115.0
# TYPE jetty_requests_active gauge
jetty_requests_active{cluster="MyPulsarCluster"} 1.0
# TYPE jetty_requests_active_max gauge
jetty_requests_active_max{cluster="MyPulsarCluster"} 5.0
# TYPE jetty_request_time_max_seconds gauge
jetty_request_time_max_seconds{cluster="MyPulsarCluster"} 0.633
# TYPE jetty_request_time_seconds_total counter
jetty_request_time_seconds_total{cluster="MyPulsarCluster"} 4.914
# TYPE jetty_dispatched_total counter
jetty_dispatched_total{cluster="MyPulsarCluster"} 115.0
# TYPE jetty_dispatched_active gauge
jetty_dispatched_active{cluster="MyPulsarCluster"} 0.0
# TYPE jetty_dispatched_active_max gauge
jetty_dispatched_active_max{cluster="MyPulsarCluster"} 4.0
# TYPE jetty_dispatched_time_max gauge
jetty_dispatched_time_max{cluster="MyPulsarCluster"} 507.0
# TYPE jetty_dispatched_time_seconds_total counter
jetty_dispatched_time_seconds_total{cluster="MyPulsarCluster"} 2.827
# TYPE jetty_async_requests_total counter
jetty_async_requests_total{cluster="MyPulsarCluster"} 25.0
# TYPE jetty_async_requests_waiting gauge
jetty_async_requests_waiting{cluster="MyPulsarCluster"} 1.0
# TYPE jetty_async_requests_waiting_max gauge
jetty_async_requests_waiting_max{cluster="MyPulsarCluster"} 4.0
# TYPE jetty_async_dispatches_total counter
jetty_async_dispatches_total{cluster="MyPulsarCluster"} 0.0
# TYPE jetty_expires_total counter
jetty_expires_total{cluster="MyPulsarCluster"} 0.0
# TYPE jetty_responses_total counter
jetty_responses_total{cluster="MyPulsarCluster",code="1xx"} 0.0
jetty_responses_total{cluster="MyPulsarCluster",code="2xx"} 109.0
jetty_responses_total{cluster="MyPulsarCluster",code="3xx"} 4.0
jetty_responses_total{cluster="MyPulsarCluster",code="4xx"} 1.0
jetty_responses_total{cluster="MyPulsarCluster",code="5xx"} 0.0
# TYPE jetty_stats_seconds gauge
jetty_stats_seconds{cluster="MyPulsarCluster"} 760.971
# TYPE jetty_responses_bytes_total counter
jetty_responses_bytes_total{cluster="MyPulsarCluster"} 1230597.0
# TYPE caffeine_cache_hit_total counter
caffeine_cache_hit_total{cluster="MyPulsarCluster",cache="owned-bundles"} 181.0
caffeine_cache_hit_total{cluster="MyPulsarCluster",cache="bookies-racks-exists"} 0.0
caffeine_cache_hit_total{cluster="MyPulsarCluster",cache="global-zk-children"} 0.0
caffeine_cache_hit_total{cluster="MyPulsarCluster",cache="bookies-racks-children"} 0.0
caffeine_cache_hit_total{cluster="MyPulsarCluster",cache="local-zk-exists"} 7.0
caffeine_cache_hit_total{cluster="MyPulsarCluster",cache="local-zk-children"} 0.0
caffeine_cache_hit_total{cluster="MyPulsarCluster",cache="bundles"} 188.0
caffeine_cache_hit_total{cluster="MyPulsarCluster",cache="global-zk-data"} 946.0
caffeine_cache_hit_total{cluster="MyPulsarCluster",cache="local-zk-data"} 12.0
caffeine_cache_hit_total{cluster="MyPulsarCluster",cache="bookies-racks-data"} 0.0
caffeine_cache_hit_total{cluster="MyPulsarCluster",cache="global-zk-exists"} 0.0
# TYPE caffeine_cache_miss_total counter
caffeine_cache_miss_total{cluster="MyPulsarCluster",cache="owned-bundles"} 10.0
caffeine_cache_miss_total{cluster="MyPulsarCluster",cache="bookies-racks-exists"} 0.0
caffeine_cache_miss_total{cluster="MyPulsarCluster",cache="global-zk-children"} 0.0
caffeine_cache_miss_total{cluster="MyPulsarCluster",cache="bookies-racks-children"} 0.0
caffeine_cache_miss_total{cluster="MyPulsarCluster",cache="local-zk-exists"} 11.0
caffeine_cache_miss_total{cluster="MyPulsarCluster",cache="local-zk-children"} 3.0
caffeine_cache_miss_total{cluster="MyPulsarCluster",cache="bundles"} 5.0
caffeine_cache_miss_total{cluster="MyPulsarCluster",cache="global-zk-data"} 698.0
caffeine_cache_miss_total{cluster="MyPulsarCluster",cache="local-zk-data"} 20.0
caffeine_cache_miss_total{cluster="MyPulsarCluster",cache="bookies-racks-data"} 0.0
caffeine_cache_miss_total{cluster="MyPulsarCluster",cache="global-zk-exists"} 0.0
# TYPE caffeine_cache_requests_total counter
caffeine_cache_requests_total{cluster="MyPulsarCluster",cache="owned-bundles"} 191.0
caffeine_cache_requests_total{cluster="MyPulsarCluster",cache="bookies-racks-exists"} 0.0
caffeine_cache_requests_total{cluster="MyPulsarCluster",cache="global-zk-children"} 0.0
caffeine_cache_requests_total{cluster="MyPulsarCluster",cache="bookies-racks-children"} 0.0
caffeine_cache_requests_total{cluster="MyPulsarCluster",cache="local-zk-exists"} 18.0
caffeine_cache_requests_total{cluster="MyPulsarCluster",cache="local-zk-children"} 3.0
caffeine_cache_requests_total{cluster="MyPulsarCluster",cache="bundles"} 193.0
caffeine_cache_requests_total{cluster="MyPulsarCluster",cache="global-zk-data"} 1644.0
caffeine_cache_requests_total{cluster="MyPulsarCluster",cache="local-zk-data"} 32.0
caffeine_cache_requests_total{cluster="MyPulsarCluster",cache="bookies-racks-data"} 0.0
caffeine_cache_requests_total{cluster="MyPulsarCluster",cache="global-zk-exists"} 0.0
# TYPE caffeine_cache_eviction_total counter
caffeine_cache_eviction_total{cluster="MyPulsarCluster",cache="owned-bundles"} 0.0
caffeine_cache_eviction_total{cluster="MyPulsarCluster",cache="bookies-racks-exists"} 0.0
caffeine_cache_eviction_total{cluster="MyPulsarCluster",cache="global-zk-children"} 0.0
caffeine_cache_eviction_total{cluster="MyPulsarCluster",cache="bookies-racks-children"} 0.0
caffeine_cache_eviction_total{cluster="MyPulsarCluster",cache="local-zk-exists"} 2.0
caffeine_cache_eviction_total{cluster="MyPulsarCluster",cache="local-zk-children"} 1.0
caffeine_cache_eviction_total{cluster="MyPulsarCluster",cache="bundles"} 0.0
caffeine_cache_eviction_total{cluster="MyPulsarCluster",cache="global-zk-data"} 0.0
caffeine_cache_eviction_total{cluster="MyPulsarCluster",cache="local-zk-data"} 0.0
caffeine_cache_eviction_total{cluster="MyPulsarCluster",cache="bookies-racks-data"} 0.0
caffeine_cache_eviction_total{cluster="MyPulsarCluster",cache="global-zk-exists"} 0.0
# TYPE caffeine_cache_eviction_weight gauge
caffeine_cache_eviction_weight{cluster="MyPulsarCluster",cache="owned-bundles"} 0.0
caffeine_cache_eviction_weight{cluster="MyPulsarCluster",cache="bookies-racks-exists"} 0.0
caffeine_cache_eviction_weight{cluster="MyPulsarCluster",cache="global-zk-children"} 0.0
caffeine_cache_eviction_weight{cluster="MyPulsarCluster",cache="bookies-racks-children"} 0.0
caffeine_cache_eviction_weight{cluster="MyPulsarCluster",cache="local-zk-exists"} 2.0
caffeine_cache_eviction_weight{cluster="MyPulsarCluster",cache="local-zk-children"} 1.0
caffeine_cache_eviction_weight{cluster="MyPulsarCluster",cache="bundles"} 0.0
caffeine_cache_eviction_weight{cluster="MyPulsarCluster",cache="global-zk-data"} 0.0
caffeine_cache_eviction_weight{cluster="MyPulsarCluster",cache="local-zk-data"} 0.0
caffeine_cache_eviction_weight{cluster="MyPulsarCluster",cache="bookies-racks-data"} 0.0
caffeine_cache_eviction_weight{cluster="MyPulsarCluster",cache="global-zk-exists"} 0.0
# TYPE caffeine_cache_load_failure_total counter
caffeine_cache_load_failure_total{cluster="MyPulsarCluster",cache="owned-bundles"} 0.0
caffeine_cache_load_failure_total{cluster="MyPulsarCluster",cache="bookies-racks-exists"} 0.0
caffeine_cache_load_failure_total{cluster="MyPulsarCluster",cache="global-zk-children"} 0.0
caffeine_cache_load_failure_total{cluster="MyPulsarCluster",cache="bookies-racks-children"} 0.0
caffeine_cache_load_failure_total{cluster="MyPulsarCluster",cache="local-zk-exists"} 0.0
caffeine_cache_load_failure_total{cluster="MyPulsarCluster",cache="local-zk-children"} 0.0
caffeine_cache_load_failure_total{cluster="MyPulsarCluster",cache="bundles"} 0.0
caffeine_cache_load_failure_total{cluster="MyPulsarCluster",cache="global-zk-data"} 344.0
caffeine_cache_load_failure_total{cluster="MyPulsarCluster",cache="local-zk-data"} 7.0
caffeine_cache_load_failure_total{cluster="MyPulsarCluster",cache="bookies-racks-data"} 0.0
caffeine_cache_load_failure_total{cluster="MyPulsarCluster",cache="global-zk-exists"} 0.0
# TYPE caffeine_cache_loads_total counter
caffeine_cache_loads_total{cluster="MyPulsarCluster",cache="owned-bundles"} 4.0
caffeine_cache_loads_total{cluster="MyPulsarCluster",cache="bookies-racks-exists"} 0.0
caffeine_cache_loads_total{cluster="MyPulsarCluster",cache="global-zk-children"} 0.0
caffeine_cache_loads_total{cluster="MyPulsarCluster",cache="bookies-racks-children"} 0.0
caffeine_cache_loads_total{cluster="MyPulsarCluster",cache="local-zk-exists"} 11.0
caffeine_cache_loads_total{cluster="MyPulsarCluster",cache="local-zk-children"} 3.0
caffeine_cache_loads_total{cluster="MyPulsarCluster",cache="bundles"} 5.0
caffeine_cache_loads_total{cluster="MyPulsarCluster",cache="global-zk-data"} 355.0
caffeine_cache_loads_total{cluster="MyPulsarCluster",cache="local-zk-data"} 10.0
caffeine_cache_loads_total{cluster="MyPulsarCluster",cache="bookies-racks-data"} 0.0
caffeine_cache_loads_total{cluster="MyPulsarCluster",cache="global-zk-exists"} 0.0
# TYPE caffeine_cache_estimated_size gauge
caffeine_cache_estimated_size{cluster="MyPulsarCluster",cache="owned-bundles"} 4.0
caffeine_cache_estimated_size{cluster="MyPulsarCluster",cache="bookies-racks-exists"} 0.0
caffeine_cache_estimated_size{cluster="MyPulsarCluster",cache="global-zk-children"} 0.0
caffeine_cache_estimated_size{cluster="MyPulsarCluster",cache="bookies-racks-children"} 0.0
caffeine_cache_estimated_size{cluster="MyPulsarCluster",cache="local-zk-exists"} 1.0
caffeine_cache_estimated_size{cluster="MyPulsarCluster",cache="local-zk-children"} 0.0
caffeine_cache_estimated_size{cluster="MyPulsarCluster",cache="bundles"} 3.0
caffeine_cache_estimated_size{cluster="MyPulsarCluster",cache="global-zk-data"} 2.0
caffeine_cache_estimated_size{cluster="MyPulsarCluster",cache="local-zk-data"} 3.0
caffeine_cache_estimated_size{cluster="MyPulsarCluster",cache="bookies-racks-data"} 0.0
caffeine_cache_estimated_size{cluster="MyPulsarCluster",cache="global-zk-exists"} 0.0
# TYPE caffeine_cache_load_duration_seconds summary
caffeine_cache_load_duration_seconds_count{cluster="MyPulsarCluster",cache="owned-bundles"} 4.0
caffeine_cache_load_duration_seconds_sum{cluster="MyPulsarCluster",cache="owned-bundles"} 0.101213046
caffeine_cache_load_duration_seconds_count{cluster="MyPulsarCluster",cache="bookies-racks-exists"} 0.0
caffeine_cache_load_duration_seconds_sum{cluster="MyPulsarCluster",cache="bookies-racks-exists"} 0.0
caffeine_cache_load_duration_seconds_count{cluster="MyPulsarCluster",cache="global-zk-children"} 0.0
caffeine_cache_load_duration_seconds_sum{cluster="MyPulsarCluster",cache="global-zk-children"} 0.0
caffeine_cache_load_duration_seconds_count{cluster="MyPulsarCluster",cache="bookies-racks-children"} 0.0
caffeine_cache_load_duration_seconds_sum{cluster="MyPulsarCluster",cache="bookies-racks-children"} 0.0
caffeine_cache_load_duration_seconds_count{cluster="MyPulsarCluster",cache="local-zk-exists"} 11.0
caffeine_cache_load_duration_seconds_sum{cluster="MyPulsarCluster",cache="local-zk-exists"} 0.150348264
caffeine_cache_load_duration_seconds_count{cluster="MyPulsarCluster",cache="local-zk-children"} 3.0
caffeine_cache_load_duration_seconds_sum{cluster="MyPulsarCluster",cache="local-zk-children"} 0.019665745
caffeine_cache_load_duration_seconds_count{cluster="MyPulsarCluster",cache="bundles"} 5.0
caffeine_cache_load_duration_seconds_sum{cluster="MyPulsarCluster",cache="bundles"} 0.10803908
caffeine_cache_load_duration_seconds_count{cluster="MyPulsarCluster",cache="global-zk-data"} 355.0
caffeine_cache_load_duration_seconds_sum{cluster="MyPulsarCluster",cache="global-zk-data"} 1.345026869
caffeine_cache_load_duration_seconds_count{cluster="MyPulsarCluster",cache="local-zk-data"} 10.0
caffeine_cache_load_duration_seconds_sum{cluster="MyPulsarCluster",cache="local-zk-data"} 0.100599775
caffeine_cache_load_duration_seconds_count{cluster="MyPulsarCluster",cache="bookies-racks-data"} 0.0
caffeine_cache_load_duration_seconds_sum{cluster="MyPulsarCluster",cache="bookies-racks-data"} 0.0
caffeine_cache_load_duration_seconds_count{cluster="MyPulsarCluster",cache="global-zk-exists"} 0.0
caffeine_cache_load_duration_seconds_sum{cluster="MyPulsarCluster",cache="global-zk-exists"} 0.0
# TYPE jvm_gc_collection_seconds summary
jvm_gc_collection_seconds_count{cluster="MyPulsarCluster",gc="G1 Young Generation"} 3.0
jvm_gc_collection_seconds_sum{cluster="MyPulsarCluster",gc="G1 Young Generation"} 1.241
jvm_gc_collection_seconds_count{cluster="MyPulsarCluster",gc="G1 Old Generation"} 0.0
jvm_gc_collection_seconds_sum{cluster="MyPulsarCluster",gc="G1 Old Generation"} 0.0
# TYPE zk_read_latency summary
zk_read_latency{cluster="MyPulsarCluster",quantile="0.5"} NaN
zk_read_latency{cluster="MyPulsarCluster",quantile="0.75"} NaN
zk_read_latency{cluster="MyPulsarCluster",quantile="0.95"} NaN
zk_read_latency{cluster="MyPulsarCluster",quantile="0.99"} NaN
zk_read_latency{cluster="MyPulsarCluster",quantile="0.999"} NaN
zk_read_latency{cluster="MyPulsarCluster",quantile="0.9999"} NaN
zk_read_latency_count{cluster="MyPulsarCluster"} 0.0
zk_read_latency_sum{cluster="MyPulsarCluster"} 0.0
# TYPE jvm_memory_direct_bytes_used gauge
jvm_memory_direct_bytes_used{cluster="MyPulsarCluster"} 2.181234695E9
# TYPE pulsar_broker_throttled_connections gauge
pulsar_broker_throttled_connections{cluster="MyPulsarCluster"} 0.0
# TYPE topic_load_times summary
topic_load_times{cluster="MyPulsarCluster",quantile="0.5"} NaN
topic_load_times{cluster="MyPulsarCluster",quantile="0.75"} NaN
topic_load_times{cluster="MyPulsarCluster",quantile="0.95"} NaN
topic_load_times{cluster="MyPulsarCluster",quantile="0.99"} NaN
topic_load_times{cluster="MyPulsarCluster",quantile="0.999"} NaN
topic_load_times{cluster="MyPulsarCluster",quantile="0.9999"} NaN
topic_load_times_count{cluster="MyPulsarCluster"} 0.0
topic_load_times_sum{cluster="MyPulsarCluster"} 0.0
# TYPE pulsar_broker_publish_latency summary
pulsar_broker_publish_latency{cluster="MyPulsarCluster",quantile="0.0"} +Inf
pulsar_broker_publish_latency{cluster="MyPulsarCluster",quantile="0.5"} NaN
pulsar_broker_publish_latency{cluster="MyPulsarCluster",quantile="0.95"} NaN
pulsar_broker_publish_latency{cluster="MyPulsarCluster",quantile="0.99"} NaN
pulsar_broker_publish_latency{cluster="MyPulsarCluster",quantile="0.999"} NaN
pulsar_broker_publish_latency{cluster="MyPulsarCluster",quantile="0.9999"} NaN
pulsar_broker_publish_latency{cluster="MyPulsarCluster",quantile="1.0"} -Inf
pulsar_broker_publish_latency_count{cluster="MyPulsarCluster"} 40706.0
pulsar_broker_publish_latency_sum{cluster="MyPulsarCluster"} 1.1180417E7
# TYPE pulsar_topics_count gauge
pulsar_topics_count{cluster="MyPulsarCluster"} 0 1650931968254
# TYPE pulsar_subscriptions_count gauge
pulsar_subscriptions_count{cluster="MyPulsarCluster"} 0 1650931968254
# TYPE pulsar_producers_count gauge
pulsar_producers_count{cluster="MyPulsarCluster"} 0 1650931968254
# TYPE pulsar_consumers_count gauge
pulsar_consumers_count{cluster="MyPulsarCluster"} 0 1650931968254
# TYPE pulsar_rate_in gauge
pulsar_rate_in{cluster="MyPulsarCluster"} 0 1650931968254
# TYPE pulsar_rate_out gauge
pulsar_rate_out{cluster="MyPulsarCluster"} 0 1650931968254
# TYPE pulsar_throughput_in gauge
pulsar_throughput_in{cluster="MyPulsarCluster"} 0 1650931968254
# TYPE pulsar_throughput_out gauge
pulsar_throughput_out{cluster="MyPulsarCluster"} 0 1650931968254
# TYPE pulsar_storage_size gauge
pulsar_storage_size{cluster="MyPulsarCluster"} 0 1650931968254
# TYPE pulsar_storage_logical_size gauge
pulsar_storage_logical_size{cluster="MyPulsarCluster"} 0 1650931968254
# TYPE pulsar_storage_write_rate gauge
pulsar_storage_write_rate{cluster="MyPulsarCluster"} 0 1650931968254
# TYPE pulsar_storage_read_rate gauge
pulsar_storage_read_rate{cluster="MyPulsarCluster"} 0 1650931968254
# TYPE pulsar_msg_backlog gauge
pulsar_msg_backlog{cluster="MyPulsarCluster"} 0 1650931968254
pulsar_subscriptions_count{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/events-sales.sales_orders"} 1.0 1650931968255
pulsar_producers_count{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/events-sales.sales_orders"} 3.0 1650931968255
pulsar_consumers_count{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/events-sales.sales_orders"} 1.0 1650931968255
pulsar_rate_in{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/events-sales.sales_orders"} 0.0 1650931968255
pulsar_rate_out{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/events-sales.sales_orders"} 0.0 1650931968255
pulsar_throughput_in{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/events-sales.sales_orders"} 0.0 1650931968255
pulsar_throughput_out{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/events-sales.sales_orders"} 0.0 1650931968255
# TYPE pulsar_average_msg_size gauge
pulsar_average_msg_size{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/events-sales.sales_orders"} 0.0 1650931968255
pulsar_storage_size{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/events-sales.sales_orders"} 13920641.0 1650931968255
pulsar_storage_logical_size{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/events-sales.sales_orders"} 13920641.0 1650931968255
pulsar_msg_backlog{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/events-sales.sales_orders"} 0.0 1650931968255
# TYPE pulsar_storage_backlog_size gauge
pulsar_storage_backlog_size{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/events-sales.sales_orders"} 0.0 1650931968255
# TYPE pulsar_storage_offloaded_size gauge
pulsar_storage_offloaded_size{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/events-sales.sales_orders"} 0.0 1650931968255
# TYPE pulsar_storage_backlog_quota_limit gauge
pulsar_storage_backlog_quota_limit{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/events-sales.sales_orders"} 10737418240.0 1650931968255
# TYPE pulsar_storage_backlog_quota_limit_time gauge
pulsar_storage_backlog_quota_limit_time{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/events-sales.sales_orders"} -1.0 1650931968255
# TYPE pulsar_storage_write_latency_le_0_5 gauge
pulsar_storage_write_latency_le_0_5{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/events-sales.sales_orders"} 0.0 1650931968255
# TYPE pulsar_storage_write_latency_le_1 gauge
pulsar_storage_write_latency_le_1{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/events-sales.sales_orders"} 0.0 1650931968255
# TYPE pulsar_storage_write_latency_le_5 gauge
pulsar_storage_write_latency_le_5{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/events-sales.sales_orders"} 0.0 1650931968255
# TYPE pulsar_storage_write_latency_le_10 gauge
pulsar_storage_write_latency_le_10{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/events-sales.sales_orders"} 0.0 1650931968255
# TYPE pulsar_storage_write_latency_le_20 gauge
pulsar_storage_write_latency_le_20{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/events-sales.sales_orders"} 0.0 1650931968255
# TYPE pulsar_storage_write_latency_le_50 gauge
pulsar_storage_write_latency_le_50{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/events-sales.sales_orders"} 0.0 1650931968255
# TYPE pulsar_storage_write_latency_le_100 gauge
pulsar_storage_write_latency_le_100{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/events-sales.sales_orders"} 0.0 1650931968255
# TYPE pulsar_storage_write_latency_le_200 gauge
pulsar_storage_write_latency_le_200{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/events-sales.sales_orders"} 0.0 1650931968255
# TYPE pulsar_storage_write_latency_le_1000 gauge
pulsar_storage_write_latency_le_1000{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/events-sales.sales_orders"} 0.0 1650931968255
# TYPE pulsar_storage_write_latency_overflow gauge
pulsar_storage_write_latency_overflow{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/events-sales.sales_orders"} 0.0 1650931968255
# TYPE pulsar_storage_write_latency_count gauge
pulsar_storage_write_latency_count{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/events-sales.sales_orders"} 0.0 1650931968255
# TYPE pulsar_storage_write_latency_sum gauge
pulsar_storage_write_latency_sum{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/events-sales.sales_orders"} 0.0 1650931968255
# TYPE pulsar_storage_ledger_write_latency_le_0_5 gauge
pulsar_storage_ledger_write_latency_le_0_5{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/events-sales.sales_orders"} 0.0 1650931968255
# TYPE pulsar_storage_ledger_write_latency_le_1 gauge
pulsar_storage_ledger_write_latency_le_1{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/events-sales.sales_orders"} 0.0 1650931968255
# TYPE pulsar_storage_ledger_write_latency_le_5 gauge
pulsar_storage_ledger_write_latency_le_5{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/events-sales.sales_orders"} 0.0 1650931968255
# TYPE pulsar_storage_ledger_write_latency_le_10 gauge
pulsar_storage_ledger_write_latency_le_10{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/events-sales.sales_orders"} 0.0 1650931968255
# TYPE pulsar_storage_ledger_write_latency_le_20 gauge
pulsar_storage_ledger_write_latency_le_20{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/events-sales.sales_orders"} 0.0 1650931968255
# TYPE pulsar_storage_ledger_write_latency_le_50 gauge
pulsar_storage_ledger_write_latency_le_50{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/events-sales.sales_orders"} 0.0 1650931968255
# TYPE pulsar_storage_ledger_write_latency_le_100 gauge
pulsar_storage_ledger_write_latency_le_100{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/events-sales.sales_orders"} 0.0 1650931968255
# TYPE pulsar_storage_ledger_write_latency_le_200 gauge
pulsar_storage_ledger_write_latency_le_200{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/events-sales.sales_orders"} 0.0 1650931968255
# TYPE pulsar_storage_ledger_write_latency_le_1000 gauge
pulsar_storage_ledger_write_latency_le_1000{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/events-sales.sales_orders"} 0.0 1650931968255
# TYPE pulsar_storage_ledger_write_latency_overflow gauge
pulsar_storage_ledger_write_latency_overflow{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/events-sales.sales_orders"} 0.0 1650931968255
# TYPE pulsar_storage_ledger_write_latency_count gauge
pulsar_storage_ledger_write_latency_count{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/events-sales.sales_orders"} 0.0 1650931968255
# TYPE pulsar_storage_ledger_write_latency_sum gauge
pulsar_storage_ledger_write_latency_sum{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/events-sales.sales_orders"} 0.0 1650931968255
# TYPE pulsar_entry_size_le_128 gauge
pulsar_entry_size_le_128{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/events-sales.sales_orders"} 0.0 1650931968255
# TYPE pulsar_entry_size_le_512 gauge
pulsar_entry_size_le_512{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/events-sales.sales_orders"} 0.0 1650931968255
# TYPE pulsar_entry_size_le_1_kb gauge
pulsar_entry_size_le_1_kb{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/events-sales.sales_orders"} 0.0 1650931968255
# TYPE pulsar_entry_size_le_2_kb gauge
pulsar_entry_size_le_2_kb{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/events-sales.sales_orders"} 0.0 1650931968255
# TYPE pulsar_entry_size_le_4_kb gauge
pulsar_entry_size_le_4_kb{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/events-sales.sales_orders"} 0.0 1650931968255
# TYPE pulsar_entry_size_le_16_kb gauge
pulsar_entry_size_le_16_kb{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/events-sales.sales_orders"} 0.0 1650931968255
# TYPE pulsar_entry_size_le_100_kb gauge
pulsar_entry_size_le_100_kb{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/events-sales.sales_orders"} 0.0 1650931968255
# TYPE pulsar_entry_size_le_1_mb gauge
pulsar_entry_size_le_1_mb{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/events-sales.sales_orders"} 0.0 1650931968255
# TYPE pulsar_entry_size_le_overflow gauge
pulsar_entry_size_le_overflow{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/events-sales.sales_orders"} 0.0 1650931968255
# TYPE pulsar_entry_size_count gauge
pulsar_entry_size_count{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/events-sales.sales_orders"} 0.0 1650931968255
# TYPE pulsar_entry_size_sum gauge
pulsar_entry_size_sum{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/events-sales.sales_orders"} 0.0 1650931968255
# TYPE pulsar_subscription_back_log gauge
pulsar_subscription_back_log{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/events-sales.sales_orders",subscription="cass_cdc_events_sub"} 0 1650931968255
# TYPE pulsar_subscription_back_log_no_delayed gauge
pulsar_subscription_back_log_no_delayed{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/events-sales.sales_orders",subscription="cass_cdc_events_sub"} 0 1650931968255
# TYPE pulsar_subscription_delayed gauge
pulsar_subscription_delayed{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/events-sales.sales_orders",subscription="cass_cdc_events_sub"} 0 1650931968255
# TYPE pulsar_subscription_msg_rate_redeliver gauge
pulsar_subscription_msg_rate_redeliver{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/events-sales.sales_orders",subscription="cass_cdc_events_sub"} 0.0 1650931968255
# TYPE pulsar_subscription_unacked_messages gauge
pulsar_subscription_unacked_messages{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/events-sales.sales_orders",subscription="cass_cdc_events_sub"} 0 1650931968255
# TYPE pulsar_subscription_blocked_on_unacked_messages gauge
pulsar_subscription_blocked_on_unacked_messages{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/events-sales.sales_orders",subscription="cass_cdc_events_sub"} 0 1650931968255
# TYPE pulsar_subscription_msg_rate_out gauge
pulsar_subscription_msg_rate_out{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/events-sales.sales_orders",subscription="cass_cdc_events_sub"} 0.0 1650931968255
# TYPE pulsar_subscription_msg_throughput_out gauge
pulsar_subscription_msg_throughput_out{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/events-sales.sales_orders",subscription="cass_cdc_events_sub"} 0.0 1650931968255
# TYPE pulsar_out_bytes_total gauge
pulsar_out_bytes_total{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/events-sales.sales_orders",subscription="cass_cdc_events_sub"} 13920641 1650931968255
# TYPE pulsar_out_messages_total gauge
pulsar_out_messages_total{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/events-sales.sales_orders",subscription="cass_cdc_events_sub"} 40485 1650931968255
# TYPE pulsar_subscription_last_expire_timestamp gauge
pulsar_subscription_last_expire_timestamp{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/events-sales.sales_orders",subscription="cass_cdc_events_sub"} 0 1650931968255
# TYPE pulsar_subscription_last_acked_timestamp gauge
pulsar_subscription_last_acked_timestamp{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/events-sales.sales_orders",subscription="cass_cdc_events_sub"} 1650931928120 1650931968255
# TYPE pulsar_subscription_last_consumed_flow_timestamp gauge
pulsar_subscription_last_consumed_flow_timestamp{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/events-sales.sales_orders",subscription="cass_cdc_events_sub"} 1650931714995 1650931968255
# TYPE pulsar_subscription_last_consumed_timestamp gauge
pulsar_subscription_last_consumed_timestamp{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/events-sales.sales_orders",subscription="cass_cdc_events_sub"} 1650931928079 1650931968255
# TYPE pulsar_subscription_last_mark_delete_advanced_timestamp gauge
pulsar_subscription_last_mark_delete_advanced_timestamp{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/events-sales.sales_orders",subscription="cass_cdc_events_sub"} 1650931928120 1650931968255
# TYPE pulsar_subscription_msg_rate_expired gauge
pulsar_subscription_msg_rate_expired{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/events-sales.sales_orders",subscription="cass_cdc_events_sub"} 0.0 1650931968255
# TYPE pulsar_subscription_total_msg_expired gauge
pulsar_subscription_total_msg_expired{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/events-sales.sales_orders",subscription="cass_cdc_events_sub"} 0 1650931968255
# TYPE pulsar_in_bytes_total gauge
pulsar_in_bytes_total{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/events-sales.sales_orders"} 13920641.0 1650931968255
# TYPE pulsar_in_messages_total gauge
pulsar_in_messages_total{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/events-sales.sales_orders"} 40485.0 1650931968255
pulsar_subscriptions_count{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/data-sales.sales_orders"} 0.0 1650931968255
pulsar_producers_count{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/data-sales.sales_orders"} 1.0 1650931968255
pulsar_consumers_count{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/data-sales.sales_orders"} 0.0 1650931968255
pulsar_rate_in{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/data-sales.sales_orders"} 0.0 1650931968255
pulsar_rate_out{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/data-sales.sales_orders"} 0.0 1650931968255
pulsar_throughput_in{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/data-sales.sales_orders"} 0.0 1650931968255
pulsar_throughput_out{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/data-sales.sales_orders"} 0.0 1650931968255
pulsar_average_msg_size{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/data-sales.sales_orders"} 0.0 1650931968255
pulsar_storage_size{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/data-sales.sales_orders"} 3093037.0 1650931968255
pulsar_storage_logical_size{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/data-sales.sales_orders"} 3093037.0 1650931968255
pulsar_msg_backlog{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/data-sales.sales_orders"} 0.0 1650931968255
pulsar_storage_backlog_size{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/data-sales.sales_orders"} 0.0 1650931968255
pulsar_storage_offloaded_size{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/data-sales.sales_orders"} 0.0 1650931968255
pulsar_storage_backlog_quota_limit{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/data-sales.sales_orders"} 10737418240.0 1650931968255
pulsar_storage_backlog_quota_limit_time{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/data-sales.sales_orders"} -1.0 1650931968255
pulsar_storage_write_latency_le_0_5{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/data-sales.sales_orders"} 0.0 1650931968255
pulsar_storage_write_latency_le_1{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/data-sales.sales_orders"} 0.0 1650931968255
pulsar_storage_write_latency_le_5{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/data-sales.sales_orders"} 0.0 1650931968255
pulsar_storage_write_latency_le_10{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/data-sales.sales_orders"} 0.0 1650931968255
pulsar_storage_write_latency_le_20{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/data-sales.sales_orders"} 0.0 1650931968255
pulsar_storage_write_latency_le_50{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/data-sales.sales_orders"} 0.0 1650931968255
pulsar_storage_write_latency_le_100{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/data-sales.sales_orders"} 0.0 1650931968255
pulsar_storage_write_latency_le_200{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/data-sales.sales_orders"} 0.0 1650931968255
pulsar_storage_write_latency_le_1000{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/data-sales.sales_orders"} 0.0 1650931968255
pulsar_storage_write_latency_overflow{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/data-sales.sales_orders"} 0.0 1650931968255
pulsar_storage_write_latency_count{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/data-sales.sales_orders"} 0.0 1650931968255
pulsar_storage_write_latency_sum{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/data-sales.sales_orders"} 0.0 1650931968255
pulsar_storage_ledger_write_latency_le_0_5{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/data-sales.sales_orders"} 0.0 1650931968255
pulsar_storage_ledger_write_latency_le_1{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/data-sales.sales_orders"} 0.0 1650931968255
pulsar_storage_ledger_write_latency_le_5{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/data-sales.sales_orders"} 0.0 1650931968255
pulsar_storage_ledger_write_latency_le_10{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/data-sales.sales_orders"} 0.0 1650931968255
pulsar_storage_ledger_write_latency_le_20{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/data-sales.sales_orders"} 0.0 1650931968255
pulsar_storage_ledger_write_latency_le_50{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/data-sales.sales_orders"} 0.0 1650931968255
pulsar_storage_ledger_write_latency_le_100{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/data-sales.sales_orders"} 0.0 1650931968255
pulsar_storage_ledger_write_latency_le_200{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/data-sales.sales_orders"} 0.0 1650931968255
pulsar_storage_ledger_write_latency_le_1000{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/data-sales.sales_orders"} 0.0 1650931968255
pulsar_storage_ledger_write_latency_overflow{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/data-sales.sales_orders"} 0.0 1650931968255
pulsar_storage_ledger_write_latency_count{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/data-sales.sales_orders"} 0.0 1650931968255
pulsar_storage_ledger_write_latency_sum{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/data-sales.sales_orders"} 0.0 1650931968255
pulsar_entry_size_le_128{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/data-sales.sales_orders"} 0.0 1650931968255
pulsar_entry_size_le_512{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/data-sales.sales_orders"} 0.0 1650931968255
pulsar_entry_size_le_1_kb{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/data-sales.sales_orders"} 0.0 1650931968255
pulsar_entry_size_le_2_kb{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/data-sales.sales_orders"} 0.0 1650931968255
pulsar_entry_size_le_4_kb{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/data-sales.sales_orders"} 0.0 1650931968255
pulsar_entry_size_le_16_kb{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/data-sales.sales_orders"} 0.0 1650931968255
pulsar_entry_size_le_100_kb{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/data-sales.sales_orders"} 0.0 1650931968255
pulsar_entry_size_le_1_mb{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/data-sales.sales_orders"} 0.0 1650931968255
pulsar_entry_size_le_overflow{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/data-sales.sales_orders"} 0.0 1650931968255
pulsar_entry_size_count{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/data-sales.sales_orders"} 0.0 1650931968255
pulsar_entry_size_sum{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/data-sales.sales_orders"} 0.0 1650931968255
pulsar_in_bytes_total{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/data-sales.sales_orders"} 3093037.0 1650931968255
pulsar_in_messages_total{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns",topic="persistent://sales_tenant/sales_ns/data-sales.sales_orders"} 22881.0 1650931968255
pulsar_topics_count{cluster="MyPulsarCluster",namespace="sales_tenant/sales_ns"} 2 1650931968255
pulsar_subscriptions_count{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/metadata"} 0.0 1650931968256
pulsar_producers_count{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/metadata"} 1.0 1650931968256
pulsar_consumers_count{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/metadata"} 0.0 1650931968256
pulsar_rate_in{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/metadata"} 0.0 1650931968256
pulsar_rate_out{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/metadata"} 0.0 1650931968256
pulsar_throughput_in{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/metadata"} 0.0 1650931968256
pulsar_throughput_out{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/metadata"} 0.0 1650931968256
pulsar_average_msg_size{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/metadata"} 0.0 1650931968256
pulsar_storage_size{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/metadata"} 707.0 1650931968256
pulsar_storage_logical_size{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/metadata"} 707.0 1650931968256
pulsar_msg_backlog{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/metadata"} 0.0 1650931968256
pulsar_storage_backlog_size{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/metadata"} 0.0 1650931968256
pulsar_storage_offloaded_size{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/metadata"} 0.0 1650931968256
pulsar_storage_backlog_quota_limit{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/metadata"} 10737418240.0 1650931968256
pulsar_storage_backlog_quota_limit_time{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/metadata"} -1.0 1650931968256
pulsar_storage_write_latency_le_0_5{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/metadata"} 0.0 1650931968256
pulsar_storage_write_latency_le_1{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/metadata"} 0.0 1650931968256
pulsar_storage_write_latency_le_5{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/metadata"} 0.0 1650931968256
pulsar_storage_write_latency_le_10{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/metadata"} 0.0 1650931968256
pulsar_storage_write_latency_le_20{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/metadata"} 0.0 1650931968256
pulsar_storage_write_latency_le_50{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/metadata"} 0.0 1650931968256
pulsar_storage_write_latency_le_100{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/metadata"} 0.0 1650931968256
pulsar_storage_write_latency_le_200{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/metadata"} 0.0 1650931968256
pulsar_storage_write_latency_le_1000{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/metadata"} 0.0 1650931968256
pulsar_storage_write_latency_overflow{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/metadata"} 0.0 1650931968256
pulsar_storage_write_latency_count{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/metadata"} 0.0 1650931968256
pulsar_storage_write_latency_sum{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/metadata"} 0.0 1650931968256
pulsar_storage_ledger_write_latency_le_0_5{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/metadata"} 0.0 1650931968256
pulsar_storage_ledger_write_latency_le_1{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/metadata"} 0.0 1650931968256
pulsar_storage_ledger_write_latency_le_5{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/metadata"} 0.0 1650931968256
pulsar_storage_ledger_write_latency_le_10{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/metadata"} 0.0 1650931968256
pulsar_storage_ledger_write_latency_le_20{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/metadata"} 0.0 1650931968256
pulsar_storage_ledger_write_latency_le_50{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/metadata"} 0.0 1650931968256
pulsar_storage_ledger_write_latency_le_100{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/metadata"} 0.0 1650931968256
pulsar_storage_ledger_write_latency_le_200{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/metadata"} 0.0 1650931968256
pulsar_storage_ledger_write_latency_le_1000{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/metadata"} 0.0 1650931968256
pulsar_storage_ledger_write_latency_overflow{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/metadata"} 0.0 1650931968256
pulsar_storage_ledger_write_latency_count{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/metadata"} 0.0 1650931968256
pulsar_storage_ledger_write_latency_sum{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/metadata"} 0.0 1650931968256
pulsar_entry_size_le_128{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/metadata"} 0.0 1650931968256
pulsar_entry_size_le_512{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/metadata"} 0.0 1650931968256
pulsar_entry_size_le_1_kb{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/metadata"} 0.0 1650931968256
pulsar_entry_size_le_2_kb{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/metadata"} 0.0 1650931968256
pulsar_entry_size_le_4_kb{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/metadata"} 0.0 1650931968256
pulsar_entry_size_le_16_kb{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/metadata"} 0.0 1650931968256
pulsar_entry_size_le_100_kb{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/metadata"} 0.0 1650931968256
pulsar_entry_size_le_1_mb{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/metadata"} 0.0 1650931968256
pulsar_entry_size_le_overflow{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/metadata"} 0.0 1650931968256
pulsar_entry_size_count{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/metadata"} 0.0 1650931968256
pulsar_entry_size_sum{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/metadata"} 0.0 1650931968256
pulsar_in_bytes_total{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/metadata"} 707.0 1650931968256
pulsar_in_messages_total{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/metadata"} 1.0 1650931968256
pulsar_subscriptions_count{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/coordinate"} 1.0 1650931968256
pulsar_producers_count{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/coordinate"} 0.0 1650931968256
pulsar_consumers_count{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/coordinate"} 1.0 1650931968256
pulsar_rate_in{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/coordinate"} 0.0 1650931968256
pulsar_rate_out{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/coordinate"} 0.0 1650931968256
pulsar_throughput_in{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/coordinate"} 0.0 1650931968256
pulsar_throughput_out{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/coordinate"} 0.0 1650931968256
pulsar_average_msg_size{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/coordinate"} 0.0 1650931968256
pulsar_storage_size{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/coordinate"} 0.0 1650931968256
pulsar_storage_logical_size{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/coordinate"} 0.0 1650931968256
pulsar_msg_backlog{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/coordinate"} 0.0 1650931968256
pulsar_storage_backlog_size{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/coordinate"} 0.0 1650931968256
pulsar_storage_offloaded_size{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/coordinate"} 0.0 1650931968256
pulsar_storage_backlog_quota_limit{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/coordinate"} 10737418240.0 1650931968256
pulsar_storage_backlog_quota_limit_time{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/coordinate"} -1.0 1650931968256
pulsar_storage_write_latency_le_0_5{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/coordinate"} 0.0 1650931968256
pulsar_storage_write_latency_le_1{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/coordinate"} 0.0 1650931968256
pulsar_storage_write_latency_le_5{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/coordinate"} 0.0 1650931968256
pulsar_storage_write_latency_le_10{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/coordinate"} 0.0 1650931968256
pulsar_storage_write_latency_le_20{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/coordinate"} 0.0 1650931968256
pulsar_storage_write_latency_le_50{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/coordinate"} 0.0 1650931968256
pulsar_storage_write_latency_le_100{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/coordinate"} 0.0 1650931968256
pulsar_storage_write_latency_le_200{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/coordinate"} 0.0 1650931968256
pulsar_storage_write_latency_le_1000{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/coordinate"} 0.0 1650931968256
pulsar_storage_write_latency_overflow{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/coordinate"} 0.0 1650931968256
pulsar_storage_write_latency_count{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/coordinate"} 0.0 1650931968256
pulsar_storage_write_latency_sum{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/coordinate"} 0.0 1650931968256
pulsar_storage_ledger_write_latency_le_0_5{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/coordinate"} 0.0 1650931968256
pulsar_storage_ledger_write_latency_le_1{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/coordinate"} 0.0 1650931968256
pulsar_storage_ledger_write_latency_le_5{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/coordinate"} 0.0 1650931968256
pulsar_storage_ledger_write_latency_le_10{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/coordinate"} 0.0 1650931968256
pulsar_storage_ledger_write_latency_le_20{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/coordinate"} 0.0 1650931968256
pulsar_storage_ledger_write_latency_le_50{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/coordinate"} 0.0 1650931968256
pulsar_storage_ledger_write_latency_le_100{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/coordinate"} 0.0 1650931968256
pulsar_storage_ledger_write_latency_le_200{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/coordinate"} 0.0 1650931968256
pulsar_storage_ledger_write_latency_le_1000{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/coordinate"} 0.0 1650931968256
pulsar_storage_ledger_write_latency_overflow{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/coordinate"} 0.0 1650931968256
pulsar_storage_ledger_write_latency_count{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/coordinate"} 0.0 1650931968256
pulsar_storage_ledger_write_latency_sum{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/coordinate"} 0.0 1650931968256
pulsar_entry_size_le_128{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/coordinate"} 0.0 1650931968256
pulsar_entry_size_le_512{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/coordinate"} 0.0 1650931968256
pulsar_entry_size_le_1_kb{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/coordinate"} 0.0 1650931968256
pulsar_entry_size_le_2_kb{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/coordinate"} 0.0 1650931968256
pulsar_entry_size_le_4_kb{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/coordinate"} 0.0 1650931968256
pulsar_entry_size_le_16_kb{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/coordinate"} 0.0 1650931968256
pulsar_entry_size_le_100_kb{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/coordinate"} 0.0 1650931968256
pulsar_entry_size_le_1_mb{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/coordinate"} 0.0 1650931968256
pulsar_entry_size_le_overflow{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/coordinate"} 0.0 1650931968256
pulsar_entry_size_count{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/coordinate"} 0.0 1650931968256
pulsar_entry_size_sum{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/coordinate"} 0.0 1650931968256
pulsar_subscription_back_log{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/coordinate",subscription="participants"} 0 1650931968256
pulsar_subscription_back_log_no_delayed{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/coordinate",subscription="participants"} 0 1650931968256
pulsar_subscription_delayed{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/coordinate",subscription="participants"} 0 1650931968256
pulsar_subscription_msg_rate_redeliver{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/coordinate",subscription="participants"} 0.0 1650931968256
pulsar_subscription_unacked_messages{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/coordinate",subscription="participants"} 0 1650931968256
pulsar_subscription_blocked_on_unacked_messages{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/coordinate",subscription="participants"} 0 1650931968256
pulsar_subscription_msg_rate_out{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/coordinate",subscription="participants"} 0.0 1650931968256
pulsar_subscription_msg_throughput_out{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/coordinate",subscription="participants"} 0.0 1650931968256
pulsar_out_bytes_total{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/coordinate",subscription="participants"} 0 1650931968256
pulsar_out_messages_total{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/coordinate",subscription="participants"} 0 1650931968256
pulsar_subscription_last_expire_timestamp{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/coordinate",subscription="participants"} 0 1650931968256
pulsar_subscription_last_acked_timestamp{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/coordinate",subscription="participants"} 0 1650931968256
pulsar_subscription_last_consumed_flow_timestamp{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/coordinate",subscription="participants"} 1650931212037 1650931968256
pulsar_subscription_last_consumed_timestamp{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/coordinate",subscription="participants"} 0 1650931968256
pulsar_subscription_last_mark_delete_advanced_timestamp{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/coordinate",subscription="participants"} 0 1650931968256
pulsar_subscription_msg_rate_expired{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/coordinate",subscription="participants"} 0.0 1650931968256
pulsar_subscription_total_msg_expired{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/coordinate",subscription="participants"} 0 1650931968256
pulsar_in_bytes_total{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/coordinate"} 0.0 1650931968256
pulsar_in_messages_total{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/coordinate"} 0.0 1650931968256
pulsar_subscriptions_count{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/assignments"} 0.0 1650931968256
pulsar_producers_count{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/assignments"} 1.0 1650931968256
pulsar_consumers_count{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/assignments"} 0.0 1650931968256
pulsar_rate_in{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/assignments"} 0.0 1650931968256
pulsar_rate_out{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/assignments"} 0.0 1650931968256
pulsar_throughput_in{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/assignments"} 0.0 1650931968256
pulsar_throughput_out{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/assignments"} 0.0 1650931968256
pulsar_average_msg_size{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/assignments"} 0.0 1650931968256
pulsar_storage_size{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/assignments"} 723.0 1650931968256
pulsar_storage_logical_size{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/assignments"} 723.0 1650931968256
pulsar_msg_backlog{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/assignments"} 0.0 1650931968256
pulsar_storage_backlog_size{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/assignments"} 0.0 1650931968256
pulsar_storage_offloaded_size{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/assignments"} 0.0 1650931968256
pulsar_storage_backlog_quota_limit{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/assignments"} 10737418240.0 1650931968256
pulsar_storage_backlog_quota_limit_time{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/assignments"} -1.0 1650931968256
pulsar_storage_write_latency_le_0_5{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/assignments"} 0.0 1650931968256
pulsar_storage_write_latency_le_1{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/assignments"} 0.0 1650931968256
pulsar_storage_write_latency_le_5{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/assignments"} 0.0 1650931968256
pulsar_storage_write_latency_le_10{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/assignments"} 0.0 1650931968256
pulsar_storage_write_latency_le_20{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/assignments"} 0.0 1650931968256
pulsar_storage_write_latency_le_50{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/assignments"} 0.0 1650931968256
pulsar_storage_write_latency_le_100{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/assignments"} 0.0 1650931968256
pulsar_storage_write_latency_le_200{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/assignments"} 0.0 1650931968256
pulsar_storage_write_latency_le_1000{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/assignments"} 0.0 1650931968256
pulsar_storage_write_latency_overflow{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/assignments"} 0.0 1650931968256
pulsar_storage_write_latency_count{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/assignments"} 0.0 1650931968256
pulsar_storage_write_latency_sum{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/assignments"} 0.0 1650931968256
pulsar_storage_ledger_write_latency_le_0_5{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/assignments"} 0.0 1650931968256
pulsar_storage_ledger_write_latency_le_1{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/assignments"} 0.0 1650931968256
pulsar_storage_ledger_write_latency_le_5{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/assignments"} 0.0 1650931968256
pulsar_storage_ledger_write_latency_le_10{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/assignments"} 0.0 1650931968256
pulsar_storage_ledger_write_latency_le_20{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/assignments"} 0.0 1650931968256
pulsar_storage_ledger_write_latency_le_50{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/assignments"} 0.0 1650931968256
pulsar_storage_ledger_write_latency_le_100{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/assignments"} 0.0 1650931968256
pulsar_storage_ledger_write_latency_le_200{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/assignments"} 0.0 1650931968256
pulsar_storage_ledger_write_latency_le_1000{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/assignments"} 0.0 1650931968256
pulsar_storage_ledger_write_latency_overflow{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/assignments"} 0.0 1650931968256
pulsar_storage_ledger_write_latency_count{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/assignments"} 0.0 1650931968256
pulsar_storage_ledger_write_latency_sum{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/assignments"} 0.0 1650931968256
pulsar_entry_size_le_128{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/assignments"} 0.0 1650931968256
pulsar_entry_size_le_512{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/assignments"} 0.0 1650931968256
pulsar_entry_size_le_1_kb{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/assignments"} 0.0 1650931968256
pulsar_entry_size_le_2_kb{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/assignments"} 0.0 1650931968256
pulsar_entry_size_le_4_kb{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/assignments"} 0.0 1650931968256
pulsar_entry_size_le_16_kb{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/assignments"} 0.0 1650931968256
pulsar_entry_size_le_100_kb{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/assignments"} 0.0 1650931968256
pulsar_entry_size_le_1_mb{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/assignments"} 0.0 1650931968256
pulsar_entry_size_le_overflow{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/assignments"} 0.0 1650931968256
pulsar_entry_size_count{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/assignments"} 0.0 1650931968256
pulsar_entry_size_sum{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/assignments"} 0.0 1650931968256
pulsar_in_bytes_total{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/assignments"} 723.0 1650931968256
pulsar_in_messages_total{cluster="MyPulsarCluster",namespace="public/functions",topic="persistent://public/functions/assignments"} 1.0 1650931968256
pulsar_topics_count{cluster="MyPulsarCluster",namespace="public/functions"} 3 1650931968256
pulsar_function_worker_start_up_time_ms_count{cluster="MyPulsarCluster",} 1.0
pulsar_function_worker_start_up_time_ms_sum{cluster="MyPulsarCluster",} 4348.020203
pulsar_function_worker_start_instance_process_time_ms{cluster="MyPulsarCluster",quantile="0.5",} 99.204134
pulsar_function_worker_start_instance_process_time_ms{cluster="MyPulsarCluster",quantile="0.9",} 99.204134
pulsar_function_worker_start_instance_process_time_ms{cluster="MyPulsarCluster",quantile="1.0",} 99.204134
pulsar_function_worker_start_instance_process_time_ms_count{cluster="MyPulsarCluster",} 1.0
pulsar_function_worker_start_instance_process_time_ms_sum{cluster="MyPulsarCluster",} 99.204134
pulsar_function_worker_instance_count{cluster="MyPulsarCluster",} 1.0
pulsar_function_worker_stop_instance_process_time_ms{cluster="MyPulsarCluster",quantile="0.5",} NaN
pulsar_function_worker_stop_instance_process_time_ms{cluster="MyPulsarCluster",quantile="0.9",} NaN
pulsar_function_worker_stop_instance_process_time_ms{cluster="MyPulsarCluster",quantile="1.0",} NaN
pulsar_function_worker_stop_instance_process_time_ms_count{cluster="MyPulsarCluster",} 0.0
pulsar_function_worker_stop_instance_process_time_ms_sum{cluster="MyPulsarCluster",} 0.0
pulsar_function_worker_schedule_execution_time_total_ms{cluster="MyPulsarCluster",quantile="0.5",} 168.015375
pulsar_function_worker_schedule_execution_time_total_ms{cluster="MyPulsarCluster",quantile="0.9",} 168.015375
pulsar_function_worker_schedule_execution_time_total_ms{cluster="MyPulsarCluster",quantile="1.0",} 168.015375
pulsar_function_worker_schedule_execution_time_total_ms_count{cluster="MyPulsarCluster",} 2.0
pulsar_function_worker_schedule_execution_time_total_ms_sum{cluster="MyPulsarCluster",} 315.61794199999997
pulsar_function_worker_schedule_strategy_execution_time_ms{cluster="MyPulsarCluster",quantile="0.5",} 2.350581
pulsar_function_worker_schedule_strategy_execution_time_ms{cluster="MyPulsarCluster",quantile="0.9",} 2.350581
pulsar_function_worker_schedule_strategy_execution_time_ms{cluster="MyPulsarCluster",quantile="1.0",} 2.350581
pulsar_function_worker_schedule_strategy_execution_time_ms_count{cluster="MyPulsarCluster",} 2.0
pulsar_function_worker_schedule_strategy_execution_time_ms_sum{cluster="MyPulsarCluster",} 2.4336510000000002
pulsar_function_worker_rebalance_execution_time_total_ms{cluster="MyPulsarCluster",quantile="0.5",} NaN
pulsar_function_worker_rebalance_execution_time_total_ms{cluster="MyPulsarCluster",quantile="0.9",} NaN
pulsar_function_worker_rebalance_execution_time_total_ms{cluster="MyPulsarCluster",quantile="1.0",} NaN
pulsar_function_worker_rebalance_execution_time_total_ms_count{cluster="MyPulsarCluster",} 0.0
pulsar_function_worker_rebalance_execution_time_total_ms_sum{cluster="MyPulsarCluster",} 0.0
pulsar_function_worker_rebalance_strategy_execution_time_ms{cluster="MyPulsarCluster",quantile="0.5",} NaN
pulsar_function_worker_rebalance_strategy_execution_time_ms{cluster="MyPulsarCluster",quantile="0.9",} NaN
pulsar_function_worker_rebalance_strategy_execution_time_ms{cluster="MyPulsarCluster",quantile="1.0",} NaN
pulsar_function_worker_rebalance_strategy_execution_time_ms_count{cluster="MyPulsarCluster",} 0.0
pulsar_function_worker_rebalance_strategy_execution_time_ms_sum{cluster="MyPulsarCluster",} 0.0
pulsar_function_worker_total_function_count{cluster="MyPulsarCluster",} 1
pulsar_function_worker_total_expected_instance_count{cluster="MyPulsarCluster",} 1
pulsar_function_worker_is_leader{cluster="MyPulsarCluster",} 1
# HELP pulsar_source_system_exception Exception from system code.
# TYPE pulsar_source_system_exception gauge
# HELP pulsar_source_user_metric_ User defined metric.
# TYPE pulsar_source_user_metric_ summary
pulsar_source_user_metric_{tenant="public",namespace="public/default",name="cassandra-source-sales-sales_orders",instance_id="0",cluster="MyPulsarCluster",fqfn="public/default/cassandra-source-sales-sales_orders",metric="query_latency",quantile="0.5",} 8.0
pulsar_source_user_metric_{tenant="public",namespace="public/default",name="cassandra-source-sales-sales_orders",instance_id="0",cluster="MyPulsarCluster",fqfn="public/default/cassandra-source-sales-sales_orders",metric="query_latency",quantile="0.9",} 24.0
pulsar_source_user_metric_{tenant="public",namespace="public/default",name="cassandra-source-sales-sales_orders",instance_id="0",cluster="MyPulsarCluster",fqfn="public/default/cassandra-source-sales-sales_orders",metric="query_latency",quantile="0.99",} 121.0
pulsar_source_user_metric_{tenant="public",namespace="public/default",name="cassandra-source-sales-sales_orders",instance_id="0",cluster="MyPulsarCluster",fqfn="public/default/cassandra-source-sales-sales_orders",metric="query_latency",quantile="0.999",} 316.0
pulsar_source_user_metric__count{tenant="public",namespace="public/default",name="cassandra-source-sales-sales_orders",instance_id="0",cluster="MyPulsarCluster",fqfn="public/default/cassandra-source-sales-sales_orders",metric="query_latency",} 40485.0
pulsar_source_user_metric__sum{tenant="public",namespace="public/default",name="cassandra-source-sales-sales_orders",instance_id="0",cluster="MyPulsarCluster",fqfn="public/default/cassandra-source-sales-sales_orders",metric="query_latency",} 384561.0
pulsar_source_user_metric_{tenant="public",namespace="public/default",name="cassandra-source-sales-sales_orders",instance_id="0",cluster="MyPulsarCluster",fqfn="public/default/cassandra-source-sales-sales_orders",metric="query_executors",quantile="0.5",} 10.0
pulsar_source_user_metric_{tenant="public",namespace="public/default",name="cassandra-source-sales-sales_orders",instance_id="0",cluster="MyPulsarCluster",fqfn="public/default/cassandra-source-sales-sales_orders",metric="query_executors",quantile="0.9",} 10.0
pulsar_source_user_metric_{tenant="public",namespace="public/default",name="cassandra-source-sales-sales_orders",instance_id="0",cluster="MyPulsarCluster",fqfn="public/default/cassandra-source-sales-sales_orders",metric="query_executors",quantile="0.99",} 10.0
pulsar_source_user_metric_{tenant="public",namespace="public/default",name="cassandra-source-sales-sales_orders",instance_id="0",cluster="MyPulsarCluster",fqfn="public/default/cassandra-source-sales-sales_orders",metric="query_executors",quantile="0.999",} 10.0
pulsar_source_user_metric__count{tenant="public",namespace="public/default",name="cassandra-source-sales-sales_orders",instance_id="0",cluster="MyPulsarCluster",fqfn="public/default/cassandra-source-sales-sales_orders",metric="query_executors",} 40485.0
pulsar_source_user_metric__sum{tenant="public",namespace="public/default",name="cassandra-source-sales-sales_orders",instance_id="0",cluster="MyPulsarCluster",fqfn="public/default/cassandra-source-sales-sales_orders",metric="query_executors",} 404850.0
pulsar_source_user_metric_{tenant="public",namespace="public/default",name="cassandra-source-sales-sales_orders",instance_id="0",cluster="MyPulsarCluster",fqfn="public/default/cassandra-source-sales-sales_orders",metric="replication_latency",quantile="0.5",} 1.9798112E7
pulsar_source_user_metric_{tenant="public",namespace="public/default",name="cassandra-source-sales-sales_orders",instance_id="0",cluster="MyPulsarCluster",fqfn="public/default/cassandra-source-sales-sales_orders",metric="replication_latency",quantile="0.9",} 3.3006283E7
pulsar_source_user_metric_{tenant="public",namespace="public/default",name="cassandra-source-sales-sales_orders",instance_id="0",cluster="MyPulsarCluster",fqfn="public/default/cassandra-source-sales-sales_orders",metric="replication_latency",quantile="0.99",} 3.5961757E7
pulsar_source_user_metric_{tenant="public",namespace="public/default",name="cassandra-source-sales-sales_orders",instance_id="0",cluster="MyPulsarCluster",fqfn="public/default/cassandra-source-sales-sales_orders",metric="replication_latency",quantile="0.999",} 3.5989704E7
pulsar_source_user_metric__count{tenant="public",namespace="public/default",name="cassandra-source-sales-sales_orders",instance_id="0",cluster="MyPulsarCluster",fqfn="public/default/cassandra-source-sales-sales_orders",metric="replication_latency",} 40485.0
pulsar_source_user_metric__sum{tenant="public",namespace="public/default",name="cassandra-source-sales-sales_orders",instance_id="0",cluster="MyPulsarCluster",fqfn="public/default/cassandra-source-sales-sales_orders",metric="replication_latency",} 7.61221819767E11
pulsar_source_user_metric_{tenant="public",namespace="public/default",name="cassandra-source-sales-sales_orders",instance_id="0",cluster="MyPulsarCluster",fqfn="public/default/cassandra-source-sales-sales_orders",metric="cache_hits",quantile="0.5",} 3943.0
pulsar_source_user_metric_{tenant="public",namespace="public/default",name="cassandra-source-sales-sales_orders",instance_id="0",cluster="MyPulsarCluster",fqfn="public/default/cassandra-source-sales-sales_orders",metric="cache_hits",quantile="0.9",} 14245.0
pulsar_source_user_metric_{tenant="public",namespace="public/default",name="cassandra-source-sales-sales_orders",instance_id="0",cluster="MyPulsarCluster",fqfn="public/default/cassandra-source-sales-sales_orders",metric="cache_hits",quantile="0.99",} 17617.0
pulsar_source_user_metric_{tenant="public",namespace="public/default",name="cassandra-source-sales-sales_orders",instance_id="0",cluster="MyPulsarCluster",fqfn="public/default/cassandra-source-sales-sales_orders",metric="cache_hits",quantile="0.999",} 17628.0
pulsar_source_user_metric__count{tenant="public",namespace="public/default",name="cassandra-source-sales-sales_orders",instance_id="0",cluster="MyPulsarCluster",fqfn="public/default/cassandra-source-sales-sales_orders",metric="cache_hits",} 40485.0
pulsar_source_user_metric__sum{tenant="public",namespace="public/default",name="cassandra-source-sales-sales_orders",instance_id="0",cluster="MyPulsarCluster",fqfn="public/default/cassandra-source-sales-sales_orders",metric="cache_hits",} 2.09973692E8
pulsar_source_user_metric_{tenant="public",namespace="public/default",name="cassandra-source-sales-sales_orders",instance_id="0",cluster="MyPulsarCluster",fqfn="public/default/cassandra-source-sales-sales_orders",metric="cache_evictions",quantile="0.5",} 0.0
pulsar_source_user_metric_{tenant="public",namespace="public/default",name="cassandra-source-sales-sales_orders",instance_id="0",cluster="MyPulsarCluster",fqfn="public/default/cassandra-source-sales-sales_orders",metric="cache_evictions",quantile="0.9",} 0.0
pulsar_source_user_metric_{tenant="public",namespace="public/default",name="cassandra-source-sales-sales_orders",instance_id="0",cluster="MyPulsarCluster",fqfn="public/default/cassandra-source-sales-sales_orders",metric="cache_evictions",quantile="0.99",} 22836.0
pulsar_source_user_metric_{tenant="public",namespace="public/default",name="cassandra-source-sales-sales_orders",instance_id="0",cluster="MyPulsarCluster",fqfn="public/default/cassandra-source-sales-sales_orders",metric="cache_evictions",quantile="0.999",} 22836.0
pulsar_source_user_metric__count{tenant="public",namespace="public/default",name="cassandra-source-sales-sales_orders",instance_id="0",cluster="MyPulsarCluster",fqfn="public/default/cassandra-source-sales-sales_orders",metric="cache_evictions",} 40485.0
pulsar_source_user_metric__sum{tenant="public",namespace="public/default",name="cassandra-source-sales-sales_orders",instance_id="0",cluster="MyPulsarCluster",fqfn="public/default/cassandra-source-sales-sales_orders",metric="cache_evictions",} 6864850.0
pulsar_source_user_metric_{tenant="public",namespace="public/default",name="cassandra-source-sales-sales_orders",instance_id="0",cluster="MyPulsarCluster",fqfn="public/default/cassandra-source-sales-sales_orders",metric="cache_size",quantile="0.5",} 16354.0
pulsar_source_user_metric_{tenant="public",namespace="public/default",name="cassandra-source-sales-sales_orders",instance_id="0",cluster="MyPulsarCluster",fqfn="public/default/cassandra-source-sales-sales_orders",metric="cache_size",quantile="0.9",} 22527.0
pulsar_source_user_metric_{tenant="public",namespace="public/default",name="cassandra-source-sales-sales_orders",instance_id="0",cluster="MyPulsarCluster",fqfn="public/default/cassandra-source-sales-sales_orders",metric="cache_size",quantile="0.99",} 22712.0
pulsar_source_user_metric_{tenant="public",namespace="public/default",name="cassandra-source-sales-sales_orders",instance_id="0",cluster="MyPulsarCluster",fqfn="public/default/cassandra-source-sales-sales_orders",metric="cache_size",quantile="0.999",} 22718.0
pulsar_source_user_metric__count{tenant="public",namespace="public/default",name="cassandra-source-sales-sales_orders",instance_id="0",cluster="MyPulsarCluster",fqfn="public/default/cassandra-source-sales-sales_orders",metric="cache_size",} 40485.0
pulsar_source_user_metric__sum{tenant="public",namespace="public/default",name="cassandra-source-sales-sales_orders",instance_id="0",cluster="MyPulsarCluster",fqfn="public/default/cassandra-source-sales-sales_orders",metric="cache_size",} 6.02680903E8
pulsar_source_user_metric_{tenant="public",namespace="public/default",name="cassandra-source-sales-sales_orders",instance_id="0",cluster="MyPulsarCluster",fqfn="public/default/cassandra-source-sales-sales_orders",metric="cache_misses",quantile="0.5",} 32964.0
pulsar_source_user_metric_{tenant="public",namespace="public/default",name="cassandra-source-sales-sales_orders",instance_id="0",cluster="MyPulsarCluster",fqfn="public/default/cassandra-source-sales-sales_orders",metric="cache_misses",quantile="0.9",} 45054.0
pulsar_source_user_metric_{tenant="public",namespace="public/default",name="cassandra-source-sales-sales_orders",instance_id="0",cluster="MyPulsarCluster",fqfn="public/default/cassandra-source-sales-sales_orders",metric="cache_misses",quantile="0.99",} 45738.0
pulsar_source_user_metric_{tenant="public",namespace="public/default",name="cassandra-source-sales-sales_orders",instance_id="0",cluster="MyPulsarCluster",fqfn="public/default/cassandra-source-sales-sales_orders",metric="cache_misses",quantile="0.999",} 45738.0
pulsar_source_user_metric__count{tenant="public",namespace="public/default",name="cassandra-source-sales-sales_orders",instance_id="0",cluster="MyPulsarCluster",fqfn="public/default/cassandra-source-sales-sales_orders",metric="cache_misses",} 40485.0
pulsar_source_user_metric__sum{tenant="public",namespace="public/default",name="cassandra-source-sales-sales_orders",instance_id="0",cluster="MyPulsarCluster",fqfn="public/default/cassandra-source-sales-sales_orders",metric="cache_misses",} 1.219323207E9
# HELP jvm_threads_current Current thread count of a JVM
# TYPE jvm_threads_current gauge
jvm_threads_current 43.0
# HELP jvm_threads_daemon Daemon thread count of a JVM
# TYPE jvm_threads_daemon gauge
jvm_threads_daemon 20.0
# HELP jvm_threads_peak Peak thread count of a JVM
# TYPE jvm_threads_peak gauge
jvm_threads_peak 44.0
# HELP jvm_threads_started_total Started thread count of a JVM
# TYPE jvm_threads_started_total counter
jvm_threads_started_total 57.0
# HELP jvm_threads_deadlocked Cycles of JVM-threads that are in deadlock waiting to acquire object monitors or ownable synchronizers
# TYPE jvm_threads_deadlocked gauge
jvm_threads_deadlocked 0.0
# HELP jvm_threads_deadlocked_monitor Cycles of JVM-threads that are in deadlock waiting to acquire object monitors
# TYPE jvm_threads_deadlocked_monitor gauge
jvm_threads_deadlocked_monitor 0.0
# HELP jvm_gc_collection_seconds Time spent in a given JVM garbage collector in seconds.
# TYPE jvm_gc_collection_seconds summary
jvm_gc_collection_seconds_count{gc="Copy",} 123.0
jvm_gc_collection_seconds_sum{gc="Copy",} 0.72
jvm_gc_collection_seconds_count{gc="MarkSweepCompact",} 6.0
jvm_gc_collection_seconds_sum{gc="MarkSweepCompact",} 0.829
# HELP pulsar_source_system_exceptions_total_1min Total number of system exceptions in the last 1 minute.
# TYPE pulsar_source_system_exceptions_total_1min counter
pulsar_source_system_exceptions_total_1min{tenant="public",namespace="public/default",name="cassandra-source-sales-sales_orders",instance_id="0",cluster="MyPulsarCluster",fqfn="public/default/cassandra-source-sales-sales_orders",} 0.0
# HELP jvm_buffer_pool_used_bytes Used bytes of a given JVM buffer pool.
# TYPE jvm_buffer_pool_used_bytes gauge
jvm_buffer_pool_used_bytes{pool="direct",} 521037.0
jvm_buffer_pool_used_bytes{pool="mapped",} 0.0
# HELP jvm_buffer_pool_capacity_bytes Bytes capacity of a given JVM buffer pool.
# TYPE jvm_buffer_pool_capacity_bytes gauge
jvm_buffer_pool_capacity_bytes{pool="direct",} 521034.0
jvm_buffer_pool_capacity_bytes{pool="mapped",} 0.0
# HELP jvm_buffer_pool_used_buffers Used buffers of a given JVM buffer pool.
# TYPE jvm_buffer_pool_used_buffers gauge
jvm_buffer_pool_used_buffers{pool="direct",} 15.0
jvm_buffer_pool_used_buffers{pool="mapped",} 0.0
# HELP pulsar_source_received_total Total number of records received from source.
# TYPE pulsar_source_received_total counter
pulsar_source_received_total{tenant="public",namespace="public/default",name="cassandra-source-sales-sales_orders",instance_id="0",cluster="MyPulsarCluster",fqfn="public/default/cassandra-source-sales-sales_orders",} 22881.0
# HELP pulsar_source_received_total_1min Total number of records received from source in the last 1 minute.
# TYPE pulsar_source_received_total_1min counter
pulsar_source_received_total_1min{tenant="public",namespace="public/default",name="cassandra-source-sales-sales_orders",instance_id="0",cluster="MyPulsarCluster",fqfn="public/default/cassandra-source-sales-sales_orders",} 0.0
# HELP org_apache_logging_log4j2_5c647e05_Additive Attribute exposed for management (org.apache.logging.log4j2<type=5c647e05, component=Loggers, name=org.apache.pulsar.functions.runtime.shaded.org.apache.bookkeeper><>Additive)
# TYPE org_apache_logging_log4j2_5c647e05_Additive untyped
org_apache_logging_log4j2_5c647e05_Additive{component="Loggers",name="org.apache.pulsar.functions.runtime.shaded.org.apache.bookkeeper",} 0.0
org_apache_logging_log4j2_5c647e05_Additive{component="Loggers",name="",} 1.0
# HELP java_lang_GarbageCollector_LastGcInfo_memoryUsageAfterGc_used java.lang.management.MemoryUsage (java.lang<type=GarbageCollector, name=Copy, key=Survivor Space><LastGcInfo, memoryUsageAfterGc>used)
# TYPE java_lang_GarbageCollector_LastGcInfo_memoryUsageAfterGc_used untyped
java_lang_GarbageCollector_LastGcInfo_memoryUsageAfterGc_used{name="Copy",key="Survivor Space",} 1687192.0
java_lang_GarbageCollector_LastGcInfo_memoryUsageAfterGc_used{name="Copy",key="Compressed Class Space",} 7808464.0
java_lang_GarbageCollector_LastGcInfo_memoryUsageAfterGc_used{name="Copy",key="Eden Space",} 0.0
java_lang_GarbageCollector_LastGcInfo_memoryUsageAfterGc_used{name="Copy",key="Metaspace",} 6.53534E7
java_lang_GarbageCollector_LastGcInfo_memoryUsageAfterGc_used{name="Copy",key="Code Cache",} 1.9117056E7
java_lang_GarbageCollector_LastGcInfo_memoryUsageAfterGc_used{name="Copy",key="Tenured Gen",} 4.898048E7
java_lang_GarbageCollector_LastGcInfo_memoryUsageAfterGc_used{name="MarkSweepCompact",key="Survivor Space",} 0.0
java_lang_GarbageCollector_LastGcInfo_memoryUsageAfterGc_used{name="MarkSweepCompact",key="Compressed Class Space",} 7605216.0
java_lang_GarbageCollector_LastGcInfo_memoryUsageAfterGc_used{name="MarkSweepCompact",key="Eden Space",} 0.0
java_lang_GarbageCollector_LastGcInfo_memoryUsageAfterGc_used{name="MarkSweepCompact",key="Metaspace",} 6.349404E7
java_lang_GarbageCollector_LastGcInfo_memoryUsageAfterGc_used{name="MarkSweepCompact",key="Code Cache",} 1.8809664E7
java_lang_GarbageCollector_LastGcInfo_memoryUsageAfterGc_used{name="MarkSweepCompact",key="Tenured Gen",} 3.6623248E7
# HELP java_lang_OperatingSystem_TotalSwapSpaceSize TotalSwapSpaceSize (java.lang<type=OperatingSystem><>TotalSwapSpaceSize)
# TYPE java_lang_OperatingSystem_TotalSwapSpaceSize untyped
java_lang_OperatingSystem_TotalSwapSpaceSize 8.585736192E9
# HELP java_lang_Threading_ThreadContentionMonitoringSupported ThreadContentionMonitoringSupported (java.lang<type=Threading><>ThreadContentionMonitoringSupported)
# TYPE java_lang_Threading_ThreadContentionMonitoringSupported untyped
java_lang_Threading_ThreadContentionMonitoringSupported 1.0
# HELP java_lang_Memory_HeapMemoryUsage_committed java.lang.management.MemoryUsage (java.lang<type=Memory><HeapMemoryUsage>committed)
# TYPE java_lang_Memory_HeapMemoryUsage_committed untyped
java_lang_Memory_HeapMemoryUsage_committed 8.869888E7
# HELP java_lang_Runtime_StartTime StartTime (java.lang<type=Runtime><>StartTime)
# TYPE java_lang_Runtime_StartTime untyped
java_lang_Runtime_StartTime 1.650931647403E12
# HELP java_lang_MemoryPool_UsageThreshold UsageThreshold (java.lang<type=MemoryPool, name=Code Cache><>UsageThreshold)
# TYPE java_lang_MemoryPool_UsageThreshold untyped
java_lang_MemoryPool_UsageThreshold{name="Code Cache",} 0.0
java_lang_MemoryPool_UsageThreshold{name="Tenured Gen",} 0.0
java_lang_MemoryPool_UsageThreshold{name="Metaspace",} 0.0
java_lang_MemoryPool_UsageThreshold{name="Compressed Class Space",} 0.0
# HELP java_lang_Memory_NonHeapMemoryUsage_used java.lang.management.MemoryUsage (java.lang<type=Memory><NonHeapMemoryUsage>used)
# TYPE java_lang_Memory_NonHeapMemoryUsage_used untyped
java_lang_Memory_NonHeapMemoryUsage_used 9.2460896E7
# HELP java_lang_Threading_PeakThreadCount PeakThreadCount (java.lang<type=Threading><>PeakThreadCount)
# TYPE java_lang_Threading_PeakThreadCount untyped
java_lang_Threading_PeakThreadCount 44.0
# HELP java_lang_ClassLoading_TotalLoadedClassCount TotalLoadedClassCount (java.lang<type=ClassLoading><>TotalLoadedClassCount)
# TYPE java_lang_ClassLoading_TotalLoadedClassCount untyped
java_lang_ClassLoading_TotalLoadedClassCount 10866.0
# HELP java_lang_ClassLoading_Verbose Verbose (java.lang<type=ClassLoading><>Verbose)
# TYPE java_lang_ClassLoading_Verbose untyped
java_lang_ClassLoading_Verbose 0.0
# HELP java_lang_GarbageCollector_LastGcInfo_id CompositeType for GC info for Copy (java.lang<type=GarbageCollector, name=Copy><LastGcInfo>id)
# TYPE java_lang_GarbageCollector_LastGcInfo_id untyped
java_lang_GarbageCollector_LastGcInfo_id{name="Copy",} 123.0
java_lang_GarbageCollector_LastGcInfo_id{name="MarkSweepCompact",} 6.0
# HELP java_lang_MemoryPool_PeakUsage_committed java.lang.management.MemoryUsage (java.lang<type=MemoryPool, name=Survivor Space><PeakUsage>committed)
# TYPE java_lang_MemoryPool_PeakUsage_committed untyped
java_lang_MemoryPool_PeakUsage_committed{name="Survivor Space",} 3014656.0
java_lang_MemoryPool_PeakUsage_committed{name="Code Cache",} 2.0774912E7
java_lang_MemoryPool_PeakUsage_committed{name="Tenured Gen",} 6.1042688E7
java_lang_MemoryPool_PeakUsage_committed{name="Metaspace",} 6.8026368E7
java_lang_MemoryPool_PeakUsage_committed{name="Eden Space",} 2.4641536E7
java_lang_MemoryPool_PeakUsage_committed{name="Compressed Class Space",} 8257536.0
# HELP java_lang_Runtime_BootClassPathSupported BootClassPathSupported (java.lang<type=Runtime><>BootClassPathSupported)
# TYPE java_lang_Runtime_BootClassPathSupported untyped
java_lang_Runtime_BootClassPathSupported 1.0
# HELP java_nio_BufferPool_Count Count (java.nio<type=BufferPool, name=direct><>Count)
# TYPE java_nio_BufferPool_Count untyped
java_nio_BufferPool_Count{name="direct",} 15.0
java_nio_BufferPool_Count{name="mapped",} 0.0
# HELP java_lang_MemoryPool_CollectionUsage_init java.lang.management.MemoryUsage (java.lang<type=MemoryPool, name=Survivor Space><CollectionUsage>init)
# TYPE java_lang_MemoryPool_CollectionUsage_init untyped
java_lang_MemoryPool_CollectionUsage_init{name="Survivor Space",} 2162688.0
java_lang_MemoryPool_CollectionUsage_init{name="Tenured Gen",} 4.3384832E7
java_lang_MemoryPool_CollectionUsage_init{name="Eden Space",} 1.7301504E7
# HELP org_apache_logging_log4j2_7852e922_IncludeLocation Attribute exposed for management (org.apache.logging.log4j2<type=7852e922, component=Loggers, name=org.apache.pulsar.functions.runtime.shaded.org.apache.bookkeeper><>IncludeLocation)
# TYPE org_apache_logging_log4j2_7852e922_IncludeLocation untyped
org_apache_logging_log4j2_7852e922_IncludeLocation{component="Loggers",name="org.apache.pulsar.functions.runtime.shaded.org.apache.bookkeeper",} 1.0
org_apache_logging_log4j2_7852e922_IncludeLocation{component="Loggers",name="",} 1.0
# HELP java_lang_Threading_ThreadAllocatedMemoryEnabled ThreadAllocatedMemoryEnabled (java.lang<type=Threading><>ThreadAllocatedMemoryEnabled)
# TYPE java_lang_Threading_ThreadAllocatedMemoryEnabled untyped
java_lang_Threading_ThreadAllocatedMemoryEnabled 1.0
# HELP java_lang_OperatingSystem_ProcessCpuLoad ProcessCpuLoad (java.lang<type=OperatingSystem><>ProcessCpuLoad)
# TYPE java_lang_OperatingSystem_ProcessCpuLoad untyped
java_lang_OperatingSystem_ProcessCpuLoad 0.021844660194174755
# HELP java_lang_MemoryPool_CollectionUsage_committed java.lang.management.MemoryUsage (java.lang<type=MemoryPool, name=Survivor Space><CollectionUsage>committed)
# TYPE java_lang_MemoryPool_CollectionUsage_committed untyped
java_lang_MemoryPool_CollectionUsage_committed{name="Survivor Space",} 3014656.0
java_lang_MemoryPool_CollectionUsage_committed{name="Tenured Gen",} 5.4173696E7
java_lang_MemoryPool_CollectionUsage_committed{name="Eden Space",} 2.4641536E7
# HELP java_lang_OperatingSystem_TotalPhysicalMemorySize TotalPhysicalMemorySize (java.lang<type=OperatingSystem><>TotalPhysicalMemorySize)
# TYPE java_lang_OperatingSystem_TotalPhysicalMemorySize untyped
java_lang_OperatingSystem_TotalPhysicalMemorySize 4.114644992E9
# HELP java_lang_Memory_NonHeapMemoryUsage_committed java.lang.management.MemoryUsage (java.lang<type=Memory><NonHeapMemoryUsage>committed)
# TYPE java_lang_Memory_NonHeapMemoryUsage_committed untyped
java_lang_Memory_NonHeapMemoryUsage_committed 9.7058816E7
# HELP java_lang_Threading_CurrentThreadAllocatedBytes CurrentThreadAllocatedBytes (java.lang<type=Threading><>CurrentThreadAllocatedBytes)
# TYPE java_lang_Threading_CurrentThreadAllocatedBytes untyped
java_lang_Threading_CurrentThreadAllocatedBytes 1.327836E7
# HELP java_lang_Memory_Verbose Verbose (java.lang<type=Memory><>Verbose)
# TYPE java_lang_Memory_Verbose untyped
java_lang_Memory_Verbose 0.0
# HELP java_lang_MemoryPool_Valid Valid (java.lang<type=MemoryPool, name=Survivor Space><>Valid)
# TYPE java_lang_MemoryPool_Valid untyped
java_lang_MemoryPool_Valid{name="Survivor Space",} 1.0
java_lang_MemoryPool_Valid{name="Code Cache",} 1.0
java_lang_MemoryPool_Valid{name="Tenured Gen",} 1.0
java_lang_MemoryPool_Valid{name="Metaspace",} 1.0
java_lang_MemoryPool_Valid{name="Eden Space",} 1.0
java_lang_MemoryPool_Valid{name="Compressed Class Space",} 1.0
# HELP java_lang_OperatingSystem_FreeSwapSpaceSize FreeSwapSpaceSize (java.lang<type=OperatingSystem><>FreeSwapSpaceSize)
# TYPE java_lang_OperatingSystem_FreeSwapSpaceSize untyped
java_lang_OperatingSystem_FreeSwapSpaceSize 8.585736192E9
# HELP java_lang_Threading_CurrentThreadCpuTime CurrentThreadCpuTime (java.lang<type=Threading><>CurrentThreadCpuTime)
# TYPE java_lang_Threading_CurrentThreadCpuTime untyped
java_lang_Threading_CurrentThreadCpuTime 4.556559E7
# HELP java_lang_MemoryPool_CollectionUsageThreshold CollectionUsageThreshold (java.lang<type=MemoryPool, name=Survivor Space><>CollectionUsageThreshold)
# TYPE java_lang_MemoryPool_CollectionUsageThreshold untyped
java_lang_MemoryPool_CollectionUsageThreshold{name="Survivor Space",} 0.0
java_lang_MemoryPool_CollectionUsageThreshold{name="Tenured Gen",} 0.0
java_lang_MemoryPool_CollectionUsageThreshold{name="Eden Space",} 0.0
# HELP org_apache_logging_log4j2_517e8000_IgnoreExceptions Attribute exposed for management (org.apache.logging.log4j2<type=517e8000, component=Appenders, name=BkRollingFile><>IgnoreExceptions)
# TYPE org_apache_logging_log4j2_517e8000_IgnoreExceptions untyped
org_apache_logging_log4j2_517e8000_IgnoreExceptions{component="Appenders",name="BkRollingFile",} 1.0
org_apache_logging_log4j2_517e8000_IgnoreExceptions{component="Appenders",name="RollingFile",} 1.0
org_apache_logging_log4j2_517e8000_IgnoreExceptions{component="Appenders",name="Console",} 1.0
# HELP java_lang_GarbageCollector_CollectionTime CollectionTime (java.lang<type=GarbageCollector, name=Copy><>CollectionTime)
# TYPE java_lang_GarbageCollector_CollectionTime untyped
java_lang_GarbageCollector_CollectionTime{name="Copy",} 720.0
java_lang_GarbageCollector_CollectionTime{name="MarkSweepCompact",} 829.0
# HELP java_lang_MemoryPool_Usage_committed java.lang.management.MemoryUsage (java.lang<type=MemoryPool, name=Survivor Space><Usage>committed)
# TYPE java_lang_MemoryPool_Usage_committed untyped
java_lang_MemoryPool_Usage_committed{name="Survivor Space",} 3014656.0
java_lang_MemoryPool_Usage_committed{name="Code Cache",} 2.0774912E7
java_lang_MemoryPool_Usage_committed{name="Tenured Gen",} 6.1042688E7
java_lang_MemoryPool_Usage_committed{name="Metaspace",} 6.8026368E7
java_lang_MemoryPool_Usage_committed{name="Eden Space",} 2.4641536E7
java_lang_MemoryPool_Usage_committed{name="Compressed Class Space",} 8257536.0
# HELP java_lang_Memory_NonHeapMemoryUsage_init java.lang.management.MemoryUsage (java.lang<type=Memory><NonHeapMemoryUsage>init)
# TYPE java_lang_Memory_NonHeapMemoryUsage_init untyped
java_lang_Memory_NonHeapMemoryUsage_init 2555904.0
# HELP java_lang_MemoryPool_PeakUsage_init java.lang.management.MemoryUsage (java.lang<type=MemoryPool, name=Survivor Space><PeakUsage>init)
# TYPE java_lang_MemoryPool_PeakUsage_init untyped
java_lang_MemoryPool_PeakUsage_init{name="Survivor Space",} 2162688.0
java_lang_MemoryPool_PeakUsage_init{name="Code Cache",} 2555904.0
java_lang_MemoryPool_PeakUsage_init{name="Tenured Gen",} 4.3384832E7
java_lang_MemoryPool_PeakUsage_init{name="Metaspace",} 0.0
java_lang_MemoryPool_PeakUsage_init{name="Eden Space",} 1.7301504E7
java_lang_MemoryPool_PeakUsage_init{name="Compressed Class Space",} 0.0
# HELP java_lang_ClassLoading_UnloadedClassCount UnloadedClassCount (java.lang<type=ClassLoading><>UnloadedClassCount)
# TYPE java_lang_ClassLoading_UnloadedClassCount untyped
java_lang_ClassLoading_UnloadedClassCount 0.0
# HELP java_lang_Memory_HeapMemoryUsage_init java.lang.management.MemoryUsage (java.lang<type=Memory><HeapMemoryUsage>init)
# TYPE java_lang_Memory_HeapMemoryUsage_init untyped
java_lang_Memory_HeapMemoryUsage_init 6.5011712E7
# HELP java_lang_GarbageCollector_LastGcInfo_memoryUsageAfterGc_init java.lang.management.MemoryUsage (java.lang<type=GarbageCollector, name=Copy, key=Survivor Space><LastGcInfo, memoryUsageAfterGc>init)
# TYPE java_lang_GarbageCollector_LastGcInfo_memoryUsageAfterGc_init untyped
java_lang_GarbageCollector_LastGcInfo_memoryUsageAfterGc_init{name="Copy",key="Survivor Space",} 2162688.0
java_lang_GarbageCollector_LastGcInfo_memoryUsageAfterGc_init{name="Copy",key="Compressed Class Space",} 0.0
java_lang_GarbageCollector_LastGcInfo_memoryUsageAfterGc_init{name="Copy",key="Eden Space",} 1.7301504E7
java_lang_GarbageCollector_LastGcInfo_memoryUsageAfterGc_init{name="Copy",key="Metaspace",} 0.0
java_lang_GarbageCollector_LastGcInfo_memoryUsageAfterGc_init{name="Copy",key="Code Cache",} 2555904.0
java_lang_GarbageCollector_LastGcInfo_memoryUsageAfterGc_init{name="Copy",key="Tenured Gen",} 4.3384832E7
java_lang_GarbageCollector_LastGcInfo_memoryUsageAfterGc_init{name="MarkSweepCompact",key="Survivor Space",} 2162688.0
java_lang_GarbageCollector_LastGcInfo_memoryUsageAfterGc_init{name="MarkSweepCompact",key="Compressed Class Space",} 0.0
java_lang_GarbageCollector_LastGcInfo_memoryUsageAfterGc_init{name="MarkSweepCompact",key="Eden Space",} 1.7301504E7
java_lang_GarbageCollector_LastGcInfo_memoryUsageAfterGc_init{name="MarkSweepCompact",key="Metaspace",} 0.0
java_lang_GarbageCollector_LastGcInfo_memoryUsageAfterGc_init{name="MarkSweepCompact",key="Code Cache",} 2555904.0
java_lang_GarbageCollector_LastGcInfo_memoryUsageAfterGc_init{name="MarkSweepCompact",key="Tenured Gen",} 4.3384832E7
# HELP java_lang_GarbageCollector_LastGcInfo_memoryUsageBeforeGc_init java.lang.management.MemoryUsage (java.lang<type=GarbageCollector, name=Copy, key=Survivor Space><LastGcInfo, memoryUsageBeforeGc>init)
# TYPE java_lang_GarbageCollector_LastGcInfo_memoryUsageBeforeGc_init untyped
java_lang_GarbageCollector_LastGcInfo_memoryUsageBeforeGc_init{name="Copy",key="Survivor Space",} 2162688.0
java_lang_GarbageCollector_LastGcInfo_memoryUsageBeforeGc_init{name="Copy",key="Compressed Class Space",} 0.0
java_lang_GarbageCollector_LastGcInfo_memoryUsageBeforeGc_init{name="Copy",key="Eden Space",} 1.7301504E7
java_lang_GarbageCollector_LastGcInfo_memoryUsageBeforeGc_init{name="Copy",key="Metaspace",} 0.0
java_lang_GarbageCollector_LastGcInfo_memoryUsageBeforeGc_init{name="Copy",key="Code Cache",} 2555904.0
java_lang_GarbageCollector_LastGcInfo_memoryUsageBeforeGc_init{name="Copy",key="Tenured Gen",} 4.3384832E7
java_lang_GarbageCollector_LastGcInfo_memoryUsageBeforeGc_init{name="MarkSweepCompact",key="Survivor Space",} 2162688.0
java_lang_GarbageCollector_LastGcInfo_memoryUsageBeforeGc_init{name="MarkSweepCompact",key="Compressed Class Space",} 0.0
java_lang_GarbageCollector_LastGcInfo_memoryUsageBeforeGc_init{name="MarkSweepCompact",key="Eden Space",} 1.7301504E7
java_lang_GarbageCollector_LastGcInfo_memoryUsageBeforeGc_init{name="MarkSweepCompact",key="Metaspace",} 0.0
java_lang_GarbageCollector_LastGcInfo_memoryUsageBeforeGc_init{name="MarkSweepCompact",key="Code Cache",} 2555904.0
java_lang_GarbageCollector_LastGcInfo_memoryUsageBeforeGc_init{name="MarkSweepCompact",key="Tenured Gen",} 4.3384832E7
# HELP java_lang_Memory_NonHeapMemoryUsage_max java.lang.management.MemoryUsage (java.lang<type=Memory><NonHeapMemoryUsage>max)
# TYPE java_lang_Memory_NonHeapMemoryUsage_max untyped
java_lang_Memory_NonHeapMemoryUsage_max -1.0
# HELP java_lang_OperatingSystem_ProcessCpuTime ProcessCpuTime (java.lang<type=OperatingSystem><>ProcessCpuTime)
# TYPE java_lang_OperatingSystem_ProcessCpuTime untyped
java_lang_OperatingSystem_ProcessCpuTime 3.874E10
# HELP java_lang_OperatingSystem_FreePhysicalMemorySize FreePhysicalMemorySize (java.lang<type=OperatingSystem><>FreePhysicalMemorySize)
# TYPE java_lang_OperatingSystem_FreePhysicalMemorySize untyped
java_lang_OperatingSystem_FreePhysicalMemorySize 7.52222208E8
# HELP java_lang_Runtime_Uptime Uptime (java.lang<type=Runtime><>Uptime)
# TYPE java_lang_Runtime_Uptime untyped
java_lang_Runtime_Uptime 321943.0
# HELP java_lang_MemoryPool_CollectionUsageThresholdExceeded CollectionUsageThresholdExceeded (java.lang<type=MemoryPool, name=Survivor Space><>CollectionUsageThresholdExceeded)
# TYPE java_lang_MemoryPool_CollectionUsageThresholdExceeded untyped
java_lang_MemoryPool_CollectionUsageThresholdExceeded{name="Survivor Space",} 0.0
java_lang_MemoryPool_CollectionUsageThresholdExceeded{name="Tenured Gen",} 0.0
java_lang_MemoryPool_CollectionUsageThresholdExceeded{name="Eden Space",} 0.0
# HELP org_apache_logging_log4j2_5c647e05_IncludeLocation Attribute exposed for management (org.apache.logging.log4j2<type=5c647e05, component=Loggers, name=org.apache.pulsar.functions.runtime.shaded.org.apache.bookkeeper><>IncludeLocation)
# TYPE org_apache_logging_log4j2_5c647e05_IncludeLocation untyped
org_apache_logging_log4j2_5c647e05_IncludeLocation{component="Loggers",name="org.apache.pulsar.functions.runtime.shaded.org.apache.bookkeeper",} 1.0
org_apache_logging_log4j2_5c647e05_IncludeLocation{component="Loggers",name="",} 1.0
# HELP java_lang_MemoryPool_UsageThresholdCount UsageThresholdCount (java.lang<type=MemoryPool, name=Code Cache><>UsageThresholdCount)
# TYPE java_lang_MemoryPool_UsageThresholdCount untyped
java_lang_MemoryPool_UsageThresholdCount{name="Code Cache",} 0.0
java_lang_MemoryPool_UsageThresholdCount{name="Tenured Gen",} 0.0
java_lang_MemoryPool_UsageThresholdCount{name="Metaspace",} 0.0
java_lang_MemoryPool_UsageThresholdCount{name="Compressed Class Space",} 0.0
# HELP org_apache_logging_log4j2_5c647e05_IgnoreExceptions Attribute exposed for management (org.apache.logging.log4j2<type=5c647e05, component=Appenders, name=Console><>IgnoreExceptions)
# TYPE org_apache_logging_log4j2_5c647e05_IgnoreExceptions untyped
org_apache_logging_log4j2_5c647e05_IgnoreExceptions{component="Appenders",name="Console",} 1.0
org_apache_logging_log4j2_5c647e05_IgnoreExceptions{component="Appenders",name="RollingFile",} 1.0
org_apache_logging_log4j2_5c647e05_IgnoreExceptions{component="Appenders",name="BkRollingFile",} 1.0
# HELP java_lang_MemoryPool_UsageThresholdSupported UsageThresholdSupported (java.lang<type=MemoryPool, name=Survivor Space><>UsageThresholdSupported)
# TYPE java_lang_MemoryPool_UsageThresholdSupported untyped
java_lang_MemoryPool_UsageThresholdSupported{name="Survivor Space",} 0.0
java_lang_MemoryPool_UsageThresholdSupported{name="Code Cache",} 1.0
java_lang_MemoryPool_UsageThresholdSupported{name="Tenured Gen",} 1.0
java_lang_MemoryPool_UsageThresholdSupported{name="Metaspace",} 1.0
java_lang_MemoryPool_UsageThresholdSupported{name="Eden Space",} 0.0
java_lang_MemoryPool_UsageThresholdSupported{name="Compressed Class Space",} 1.0
# HELP java_lang_Threading_ThreadContentionMonitoringEnabled ThreadContentionMonitoringEnabled (java.lang<type=Threading><>ThreadContentionMonitoringEnabled)
# TYPE java_lang_Threading_ThreadContentionMonitoringEnabled untyped
java_lang_Threading_ThreadContentionMonitoringEnabled 0.0
# HELP java_lang_OperatingSystem_CommittedVirtualMemorySize CommittedVirtualMemorySize (java.lang<type=OperatingSystem><>CommittedVirtualMemorySize)
# TYPE java_lang_OperatingSystem_CommittedVirtualMemorySize untyped
java_lang_OperatingSystem_CommittedVirtualMemorySize 3.245871104E9
# HELP org_apache_logging_log4j2_517e8000_IncludeLocation Attribute exposed for management (org.apache.logging.log4j2<type=517e8000, component=Loggers, name=><>IncludeLocation)
# TYPE org_apache_logging_log4j2_517e8000_IncludeLocation untyped
org_apache_logging_log4j2_517e8000_IncludeLocation{component="Loggers",name="",} 1.0
org_apache_logging_log4j2_517e8000_IncludeLocation{component="Loggers",name="org.apache.pulsar.functions.runtime.shaded.org.apache.bookkeeper",} 1.0
# HELP java_lang_MemoryPool_CollectionUsage_max java.lang.management.MemoryUsage (java.lang<type=MemoryPool, name=Survivor Space><CollectionUsage>max)
# TYPE java_lang_MemoryPool_CollectionUsage_max untyped
java_lang_MemoryPool_CollectionUsage_max{name="Survivor Space",} 3.5782656E7
java_lang_MemoryPool_CollectionUsage_max{name="Tenured Gen",} 7.15849728E8
java_lang_MemoryPool_CollectionUsage_max{name="Eden Space",} 2.86326784E8
# HELP java_lang_GarbageCollector_LastGcInfo_endTime CompositeType for GC info for Copy (java.lang<type=GarbageCollector, name=Copy><LastGcInfo>endTime)
# TYPE java_lang_GarbageCollector_LastGcInfo_endTime untyped
java_lang_GarbageCollector_LastGcInfo_endTime{name="Copy",} 317457.0
java_lang_GarbageCollector_LastGcInfo_endTime{name="MarkSweepCompact",} 62598.0
# HELP java_lang_Memory_HeapMemoryUsage_max java.lang.management.MemoryUsage (java.lang<type=Memory><HeapMemoryUsage>max)
# TYPE java_lang_Memory_HeapMemoryUsage_max untyped
java_lang_Memory_HeapMemoryUsage_max 1.037959168E9
# HELP java_lang_MemoryPool_CollectionUsageThresholdCount CollectionUsageThresholdCount (java.lang<type=MemoryPool, name=Survivor Space><>CollectionUsageThresholdCount)
# TYPE java_lang_MemoryPool_CollectionUsageThresholdCount untyped
java_lang_MemoryPool_CollectionUsageThresholdCount{name="Survivor Space",} 0.0
java_lang_MemoryPool_CollectionUsageThresholdCount{name="Tenured Gen",} 0.0
java_lang_MemoryPool_CollectionUsageThresholdCount{name="Eden Space",} 0.0
# HELP java_lang_MemoryPool_PeakUsage_used java.lang.management.MemoryUsage (java.lang<type=MemoryPool, name=Survivor Space><PeakUsage>used)
# TYPE java_lang_MemoryPool_PeakUsage_used untyped
java_lang_MemoryPool_PeakUsage_used{name="Survivor Space",} 3014648.0
java_lang_MemoryPool_PeakUsage_used{name="Code Cache",} 2.0273792E7
java_lang_MemoryPool_PeakUsage_used{name="Tenured Gen",} 5.4061368E7
java_lang_MemoryPool_PeakUsage_used{name="Metaspace",} 6.5378296E7
java_lang_MemoryPool_PeakUsage_used{name="Eden Space",} 2.4641536E7
java_lang_MemoryPool_PeakUsage_used{name="Compressed Class Space",} 7816984.0
# HELP java_lang_OperatingSystem_MaxFileDescriptorCount MaxFileDescriptorCount (java.lang<type=OperatingSystem><>MaxFileDescriptorCount)
# TYPE java_lang_OperatingSystem_MaxFileDescriptorCount untyped
java_lang_OperatingSystem_MaxFileDescriptorCount 100000.0
# HELP java_lang_Threading_CurrentThreadUserTime CurrentThreadUserTime (java.lang<type=Threading><>CurrentThreadUserTime)
# TYPE java_lang_Threading_CurrentThreadUserTime untyped
java_lang_Threading_CurrentThreadUserTime 4.0E7
# HELP java_lang_Threading_ThreadCount ThreadCount (java.lang<type=Threading><>ThreadCount)
# TYPE java_lang_Threading_ThreadCount untyped
java_lang_Threading_ThreadCount 43.0
# HELP java_lang_GarbageCollector_LastGcInfo_memoryUsageAfterGc_committed java.lang.management.MemoryUsage (java.lang<type=GarbageCollector, name=Copy, key=Survivor Space><LastGcInfo, memoryUsageAfterGc>committed)
# TYPE java_lang_GarbageCollector_LastGcInfo_memoryUsageAfterGc_committed untyped
java_lang_GarbageCollector_LastGcInfo_memoryUsageAfterGc_committed{name="Copy",key="Survivor Space",} 3014656.0
java_lang_GarbageCollector_LastGcInfo_memoryUsageAfterGc_committed{name="Copy",key="Compressed Class Space",} 8257536.0
java_lang_GarbageCollector_LastGcInfo_memoryUsageAfterGc_committed{name="Copy",key="Eden Space",} 2.4641536E7
java_lang_GarbageCollector_LastGcInfo_memoryUsageAfterGc_committed{name="Copy",key="Metaspace",} 6.7764224E7
java_lang_GarbageCollector_LastGcInfo_memoryUsageAfterGc_committed{name="Copy",key="Code Cache",} 2.0774912E7
java_lang_GarbageCollector_LastGcInfo_memoryUsageAfterGc_committed{name="Copy",key="Tenured Gen",} 6.1042688E7
java_lang_GarbageCollector_LastGcInfo_memoryUsageAfterGc_committed{name="MarkSweepCompact",key="Survivor Space",} 2621440.0
java_lang_GarbageCollector_LastGcInfo_memoryUsageAfterGc_committed{name="MarkSweepCompact",key="Compressed Class Space",} 8126464.0
java_lang_GarbageCollector_LastGcInfo_memoryUsageAfterGc_committed{name="MarkSweepCompact",key="Eden Space",} 2.1430272E7
java_lang_GarbageCollector_LastGcInfo_memoryUsageAfterGc_committed{name="MarkSweepCompact",key="Metaspace",} 6.6060288E7
java_lang_GarbageCollector_LastGcInfo_memoryUsageAfterGc_committed{name="MarkSweepCompact",key="Code Cache",} 2.0774912E7
java_lang_GarbageCollector_LastGcInfo_memoryUsageAfterGc_committed{name="MarkSweepCompact",key="Tenured Gen",} 5.4173696E7
# HELP java_lang_Memory_ObjectPendingFinalizationCount ObjectPendingFinalizationCount (java.lang<type=Memory><>ObjectPendingFinalizationCount)
# TYPE java_lang_Memory_ObjectPendingFinalizationCount untyped
java_lang_Memory_ObjectPendingFinalizationCount 0.0
# HELP java_lang_MemoryPool_Usage_used java.lang.management.MemoryUsage (java.lang<type=MemoryPool, name=Survivor Space><Usage>used)
# TYPE java_lang_MemoryPool_Usage_used untyped
java_lang_MemoryPool_Usage_used{name="Survivor Space",} 1687192.0
java_lang_MemoryPool_Usage_used{name="Code Cache",} 1.9221184E7
java_lang_MemoryPool_Usage_used{name="Tenured Gen",} 4.898048E7
java_lang_MemoryPool_Usage_used{name="Metaspace",} 6.5378296E7
java_lang_MemoryPool_Usage_used{name="Eden Space",} 5882496.0
java_lang_MemoryPool_Usage_used{name="Compressed Class Space",} 7816984.0
# HELP java_lang_GarbageCollector_CollectionCount CollectionCount (java.lang<type=GarbageCollector, name=Copy><>CollectionCount)
# TYPE java_lang_GarbageCollector_CollectionCount untyped
java_lang_GarbageCollector_CollectionCount{name="Copy",} 123.0
java_lang_GarbageCollector_CollectionCount{name="MarkSweepCompact",} 6.0
# HELP java_lang_Threading_SynchronizerUsageSupported SynchronizerUsageSupported (java.lang<type=Threading><>SynchronizerUsageSupported)
# TYPE java_lang_Threading_SynchronizerUsageSupported untyped
java_lang_Threading_SynchronizerUsageSupported 1.0
# HELP org_apache_logging_log4j2_7852e922_IgnoreExceptions Attribute exposed for management (org.apache.logging.log4j2<type=7852e922, component=Appenders, name=BkRollingFile><>IgnoreExceptions)
# TYPE org_apache_logging_log4j2_7852e922_IgnoreExceptions untyped
org_apache_logging_log4j2_7852e922_IgnoreExceptions{component="Appenders",name="BkRollingFile",} 1.0
org_apache_logging_log4j2_7852e922_IgnoreExceptions{component="Appenders",name="RollingFile",} 1.0
org_apache_logging_log4j2_7852e922_IgnoreExceptions{component="Appenders",name="Console",} 1.0
# HELP java_lang_GarbageCollector_LastGcInfo_GcThreadCount CompositeType for GC info for Copy (java.lang<type=GarbageCollector, name=Copy><LastGcInfo>GcThreadCount)
# TYPE java_lang_GarbageCollector_LastGcInfo_GcThreadCount untyped
java_lang_GarbageCollector_LastGcInfo_GcThreadCount{name="Copy",} 1.0
java_lang_GarbageCollector_LastGcInfo_GcThreadCount{name="MarkSweepCompact",} 1.0
# HELP java_lang_GarbageCollector_LastGcInfo_memoryUsageBeforeGc_committed java.lang.management.MemoryUsage (java.lang<type=GarbageCollector, name=Copy, key=Survivor Space><LastGcInfo, memoryUsageBeforeGc>committed)
# TYPE java_lang_GarbageCollector_LastGcInfo_memoryUsageBeforeGc_committed untyped
java_lang_GarbageCollector_LastGcInfo_memoryUsageBeforeGc_committed{name="Copy",key="Survivor Space",} 3014656.0
java_lang_GarbageCollector_LastGcInfo_memoryUsageBeforeGc_committed{name="Copy",key="Compressed Class Space",} 8257536.0
java_lang_GarbageCollector_LastGcInfo_memoryUsageBeforeGc_committed{name="Copy",key="Eden Space",} 2.4641536E7
java_lang_GarbageCollector_LastGcInfo_memoryUsageBeforeGc_committed{name="Copy",key="Metaspace",} 6.7764224E7
java_lang_GarbageCollector_LastGcInfo_memoryUsageBeforeGc_committed{name="Copy",key="Code Cache",} 2.0774912E7
java_lang_GarbageCollector_LastGcInfo_memoryUsageBeforeGc_committed{name="Copy",key="Tenured Gen",} 6.1042688E7
java_lang_GarbageCollector_LastGcInfo_memoryUsageBeforeGc_committed{name="MarkSweepCompact",key="Survivor Space",} 2621440.0
java_lang_GarbageCollector_LastGcInfo_memoryUsageBeforeGc_committed{name="MarkSweepCompact",key="Compressed Class Space",} 8126464.0
java_lang_GarbageCollector_LastGcInfo_memoryUsageBeforeGc_committed{name="MarkSweepCompact",key="Eden Space",} 2.1430272E7
java_lang_GarbageCollector_LastGcInfo_memoryUsageBeforeGc_committed{name="MarkSweepCompact",key="Metaspace",} 6.6060288E7
java_lang_GarbageCollector_LastGcInfo_memoryUsageBeforeGc_committed{name="MarkSweepCompact",key="Code Cache",} 2.0774912E7
java_lang_GarbageCollector_LastGcInfo_memoryUsageBeforeGc_committed{name="MarkSweepCompact",key="Tenured Gen",} 5.4173696E7
# HELP java_lang_Threading_CurrentThreadCpuTimeSupported CurrentThreadCpuTimeSupported (java.lang<type=Threading><>CurrentThreadCpuTimeSupported)
# TYPE java_lang_Threading_CurrentThreadCpuTimeSupported untyped
java_lang_Threading_CurrentThreadCpuTimeSupported 1.0
# HELP java_lang_ClassLoading_LoadedClassCount LoadedClassCount (java.lang<type=ClassLoading><>LoadedClassCount)
# TYPE java_lang_ClassLoading_LoadedClassCount untyped
java_lang_ClassLoading_LoadedClassCount 10866.0
# HELP java_lang_MemoryPool_PeakUsage_max java.lang.management.MemoryUsage (java.lang<type=MemoryPool, name=Survivor Space><PeakUsage>max)
# TYPE java_lang_MemoryPool_PeakUsage_max untyped
java_lang_MemoryPool_PeakUsage_max{name="Survivor Space",} 3.5782656E7
java_lang_MemoryPool_PeakUsage_max{name="Code Cache",} 2.5165824E8
java_lang_MemoryPool_PeakUsage_max{name="Tenured Gen",} 7.15849728E8
java_lang_MemoryPool_PeakUsage_max{name="Metaspace",} -1.0
java_lang_MemoryPool_PeakUsage_max{name="Eden Space",} 2.86326784E8
java_lang_MemoryPool_PeakUsage_max{name="Compressed Class Space",} 1.073741824E9
# HELP java_lang_MemoryPool_Usage_max java.lang.management.MemoryUsage (java.lang<type=MemoryPool, name=Survivor Space><Usage>max)
# TYPE java_lang_MemoryPool_Usage_max untyped
java_lang_MemoryPool_Usage_max{name="Survivor Space",} 3.5782656E7
java_lang_MemoryPool_Usage_max{name="Code Cache",} 2.5165824E8
java_lang_MemoryPool_Usage_max{name="Tenured Gen",} 7.15849728E8
java_lang_MemoryPool_Usage_max{name="Metaspace",} -1.0
java_lang_MemoryPool_Usage_max{name="Eden Space",} 2.86326784E8
java_lang_MemoryPool_Usage_max{name="Compressed Class Space",} 1.073741824E9
# HELP java_lang_GarbageCollector_Valid Valid (java.lang<type=GarbageCollector, name=Copy><>Valid)
# TYPE java_lang_GarbageCollector_Valid untyped
java_lang_GarbageCollector_Valid{name="Copy",} 1.0
java_lang_GarbageCollector_Valid{name="MarkSweepCompact",} 1.0
# HELP java_lang_MemoryManager_Valid Valid (java.lang<type=MemoryManager, name=CodeCacheManager><>Valid)
# TYPE java_lang_MemoryManager_Valid untyped
java_lang_MemoryManager_Valid{name="CodeCacheManager",} 1.0
java_lang_MemoryManager_Valid{name="Metaspace Manager",} 1.0
# HELP java_lang_GarbageCollector_LastGcInfo_memoryUsageBeforeGc_used java.lang.management.MemoryUsage (java.lang<type=GarbageCollector, name=Copy, key=Survivor Space><LastGcInfo, memoryUsageBeforeGc>used)
# TYPE java_lang_GarbageCollector_LastGcInfo_memoryUsageBeforeGc_used untyped
java_lang_GarbageCollector_LastGcInfo_memoryUsageBeforeGc_used{name="Copy",key="Survivor Space",} 2359832.0
java_lang_GarbageCollector_LastGcInfo_memoryUsageBeforeGc_used{name="Copy",key="Compressed Class Space",} 7808464.0
java_lang_GarbageCollector_LastGcInfo_memoryUsageBeforeGc_used{name="Copy",key="Eden Space",} 2.4641536E7
java_lang_GarbageCollector_LastGcInfo_memoryUsageBeforeGc_used{name="Copy",key="Metaspace",} 6.53534E7
java_lang_GarbageCollector_LastGcInfo_memoryUsageBeforeGc_used{name="Copy",key="Code Cache",} 1.9117056E7
java_lang_GarbageCollector_LastGcInfo_memoryUsageBeforeGc_used{name="Copy",key="Tenured Gen",} 4.6834992E7
java_lang_GarbageCollector_LastGcInfo_memoryUsageBeforeGc_used{name="MarkSweepCompact",key="Survivor Space",} 770232.0
java_lang_GarbageCollector_LastGcInfo_memoryUsageBeforeGc_used{name="MarkSweepCompact",key="Compressed Class Space",} 7605216.0
java_lang_GarbageCollector_LastGcInfo_memoryUsageBeforeGc_used{name="MarkSweepCompact",key="Eden Space",} 0.0
java_lang_GarbageCollector_LastGcInfo_memoryUsageBeforeGc_used{name="MarkSweepCompact",key="Metaspace",} 6.349404E7
java_lang_GarbageCollector_LastGcInfo_memoryUsageBeforeGc_used{name="MarkSweepCompact",key="Code Cache",} 1.8809664E7
java_lang_GarbageCollector_LastGcInfo_memoryUsageBeforeGc_used{name="MarkSweepCompact",key="Tenured Gen",} 5.4061368E7
# HELP java_lang_MemoryPool_Usage_init java.lang.management.MemoryUsage (java.lang<type=MemoryPool, name=Survivor Space><Usage>init)
# TYPE java_lang_MemoryPool_Usage_init untyped
java_lang_MemoryPool_Usage_init{name="Survivor Space",} 2162688.0
java_lang_MemoryPool_Usage_init{name="Code Cache",} 2555904.0
java_lang_MemoryPool_Usage_init{name="Tenured Gen",} 4.3384832E7
java_lang_MemoryPool_Usage_init{name="Metaspace",} 0.0
java_lang_MemoryPool_Usage_init{name="Eden Space",} 1.7301504E7
java_lang_MemoryPool_Usage_init{name="Compressed Class Space",} 0.0
# HELP org_apache_logging_log4j2_517e8000_Additive Attribute exposed for management (org.apache.logging.log4j2<type=517e8000, component=Loggers, name=><>Additive)
# TYPE org_apache_logging_log4j2_517e8000_Additive untyped
org_apache_logging_log4j2_517e8000_Additive{component="Loggers",name="",} 1.0
org_apache_logging_log4j2_517e8000_Additive{component="Loggers",name="org.apache.pulsar.functions.runtime.shaded.org.apache.bookkeeper",} 0.0
# HELP java_lang_Compilation_TotalCompilationTime TotalCompilationTime (java.lang<type=Compilation><>TotalCompilationTime)
# TYPE java_lang_Compilation_TotalCompilationTime untyped
java_lang_Compilation_TotalCompilationTime 48457.0
# HELP java_lang_MemoryPool_UsageThresholdExceeded UsageThresholdExceeded (java.lang<type=MemoryPool, name=Code Cache><>UsageThresholdExceeded)
# TYPE java_lang_MemoryPool_UsageThresholdExceeded untyped
java_lang_MemoryPool_UsageThresholdExceeded{name="Code Cache",} 0.0
java_lang_MemoryPool_UsageThresholdExceeded{name="Tenured Gen",} 0.0
java_lang_MemoryPool_UsageThresholdExceeded{name="Metaspace",} 0.0
java_lang_MemoryPool_UsageThresholdExceeded{name="Compressed Class Space",} 0.0
# HELP java_lang_Compilation_CompilationTimeMonitoringSupported CompilationTimeMonitoringSupported (java.lang<type=Compilation><>CompilationTimeMonitoringSupported)
# TYPE java_lang_Compilation_CompilationTimeMonitoringSupported untyped
java_lang_Compilation_CompilationTimeMonitoringSupported 1.0
# HELP java_lang_GarbageCollector_LastGcInfo_startTime CompositeType for GC info for Copy (java.lang<type=GarbageCollector, name=Copy><LastGcInfo>startTime)
# TYPE java_lang_GarbageCollector_LastGcInfo_startTime untyped
java_lang_GarbageCollector_LastGcInfo_startTime{name="Copy",} 317453.0
java_lang_GarbageCollector_LastGcInfo_startTime{name="MarkSweepCompact",} 62330.0
# HELP java_lang_OperatingSystem_AvailableProcessors AvailableProcessors (java.lang<type=OperatingSystem><>AvailableProcessors)
# TYPE java_lang_OperatingSystem_AvailableProcessors untyped
java_lang_OperatingSystem_AvailableProcessors 1.0
# HELP java_lang_MemoryPool_CollectionUsageThresholdSupported CollectionUsageThresholdSupported (java.lang<type=MemoryPool, name=Survivor Space><>CollectionUsageThresholdSupported)
# TYPE java_lang_MemoryPool_CollectionUsageThresholdSupported untyped
java_lang_MemoryPool_CollectionUsageThresholdSupported{name="Survivor Space",} 1.0
java_lang_MemoryPool_CollectionUsageThresholdSupported{name="Code Cache",} 0.0
java_lang_MemoryPool_CollectionUsageThresholdSupported{name="Tenured Gen",} 1.0
java_lang_MemoryPool_CollectionUsageThresholdSupported{name="Metaspace",} 0.0
java_lang_MemoryPool_CollectionUsageThresholdSupported{name="Eden Space",} 1.0
java_lang_MemoryPool_CollectionUsageThresholdSupported{name="Compressed Class Space",} 0.0
# HELP java_lang_GarbageCollector_LastGcInfo_memoryUsageBeforeGc_max java.lang.management.MemoryUsage (java.lang<type=GarbageCollector, name=Copy, key=Survivor Space><LastGcInfo, memoryUsageBeforeGc>max)
# TYPE java_lang_GarbageCollector_LastGcInfo_memoryUsageBeforeGc_max untyped
java_lang_GarbageCollector_LastGcInfo_memoryUsageBeforeGc_max{name="Copy",key="Survivor Space",} 3.5782656E7
java_lang_GarbageCollector_LastGcInfo_memoryUsageBeforeGc_max{name="Copy",key="Compressed Class Space",} 1.073741824E9
java_lang_GarbageCollector_LastGcInfo_memoryUsageBeforeGc_max{name="Copy",key="Eden Space",} 2.86326784E8
java_lang_GarbageCollector_LastGcInfo_memoryUsageBeforeGc_max{name="Copy",key="Metaspace",} -1.0
java_lang_GarbageCollector_LastGcInfo_memoryUsageBeforeGc_max{name="Copy",key="Code Cache",} 2.5165824E8
java_lang_GarbageCollector_LastGcInfo_memoryUsageBeforeGc_max{name="Copy",key="Tenured Gen",} 7.15849728E8
java_lang_GarbageCollector_LastGcInfo_memoryUsageBeforeGc_max{name="MarkSweepCompact",key="Survivor Space",} 3.5782656E7
java_lang_GarbageCollector_LastGcInfo_memoryUsageBeforeGc_max{name="MarkSweepCompact",key="Compressed Class Space",} 1.073741824E9
java_lang_GarbageCollector_LastGcInfo_memoryUsageBeforeGc_max{name="MarkSweepCompact",key="Eden Space",} 2.86326784E8
java_lang_GarbageCollector_LastGcInfo_memoryUsageBeforeGc_max{name="MarkSweepCompact",key="Metaspace",} -1.0
java_lang_GarbageCollector_LastGcInfo_memoryUsageBeforeGc_max{name="MarkSweepCompact",key="Code Cache",} 2.5165824E8
java_lang_GarbageCollector_LastGcInfo_memoryUsageBeforeGc_max{name="MarkSweepCompact",key="Tenured Gen",} 7.15849728E8
# HELP java_nio_BufferPool_MemoryUsed MemoryUsed (java.nio<type=BufferPool, name=direct><>MemoryUsed)
# TYPE java_nio_BufferPool_MemoryUsed untyped
java_nio_BufferPool_MemoryUsed{name="direct",} 521037.0
java_nio_BufferPool_MemoryUsed{name="mapped",} 0.0
# HELP java_nio_BufferPool_TotalCapacity TotalCapacity (java.nio<type=BufferPool, name=direct><>TotalCapacity)
# TYPE java_nio_BufferPool_TotalCapacity untyped
java_nio_BufferPool_TotalCapacity{name="direct",} 521034.0
java_nio_BufferPool_TotalCapacity{name="mapped",} 0.0
# HELP java_lang_Memory_HeapMemoryUsage_used java.lang.management.MemoryUsage (java.lang<type=Memory><HeapMemoryUsage>used)
# TYPE java_lang_Memory_HeapMemoryUsage_used untyped
java_lang_Memory_HeapMemoryUsage_used 5.8938848E7
# HELP java_lang_MemoryPool_CollectionUsage_used java.lang.management.MemoryUsage (java.lang<type=MemoryPool, name=Survivor Space><CollectionUsage>used)
# TYPE java_lang_MemoryPool_CollectionUsage_used untyped
java_lang_MemoryPool_CollectionUsage_used{name="Survivor Space",} 1687192.0
java_lang_MemoryPool_CollectionUsage_used{name="Tenured Gen",} 3.6623248E7
java_lang_MemoryPool_CollectionUsage_used{name="Eden Space",} 0.0
# HELP java_lang_OperatingSystem_SystemCpuLoad SystemCpuLoad (java.lang<type=OperatingSystem><>SystemCpuLoad)
# TYPE java_lang_OperatingSystem_SystemCpuLoad untyped
java_lang_OperatingSystem_SystemCpuLoad 0.2766990291262136
# HELP java_lang_Threading_ThreadAllocatedMemorySupported ThreadAllocatedMemorySupported (java.lang<type=Threading><>ThreadAllocatedMemorySupported)
# TYPE java_lang_Threading_ThreadAllocatedMemorySupported untyped
java_lang_Threading_ThreadAllocatedMemorySupported 1.0
# HELP java_lang_Threading_ThreadCpuTimeSupported ThreadCpuTimeSupported (java.lang<type=Threading><>ThreadCpuTimeSupported)
# TYPE java_lang_Threading_ThreadCpuTimeSupported untyped
java_lang_Threading_ThreadCpuTimeSupported 1.0
# HELP java_lang_Threading_DaemonThreadCount DaemonThreadCount (java.lang<type=Threading><>DaemonThreadCount)
# TYPE java_lang_Threading_DaemonThreadCount untyped
java_lang_Threading_DaemonThreadCount 20.0
# HELP java_lang_Threading_TotalStartedThreadCount TotalStartedThreadCount (java.lang<type=Threading><>TotalStartedThreadCount)
# TYPE java_lang_Threading_TotalStartedThreadCount untyped
java_lang_Threading_TotalStartedThreadCount 57.0
# HELP java_lang_OperatingSystem_SystemLoadAverage SystemLoadAverage (java.lang<type=OperatingSystem><>SystemLoadAverage)
# TYPE java_lang_OperatingSystem_SystemLoadAverage untyped
java_lang_OperatingSystem_SystemLoadAverage 0.27
# HELP org_apache_logging_log4j2_7852e922_Additive Attribute exposed for management (org.apache.logging.log4j2<type=7852e922, component=Loggers, name=org.apache.pulsar.functions.runtime.shaded.org.apache.bookkeeper><>Additive)
# TYPE org_apache_logging_log4j2_7852e922_Additive untyped
org_apache_logging_log4j2_7852e922_Additive{component="Loggers",name="org.apache.pulsar.functions.runtime.shaded.org.apache.bookkeeper",} 0.0
org_apache_logging_log4j2_7852e922_Additive{component="Loggers",name="",} 1.0
# HELP java_lang_Threading_ObjectMonitorUsageSupported ObjectMonitorUsageSupported (java.lang<type=Threading><>ObjectMonitorUsageSupported)
# TYPE java_lang_Threading_ObjectMonitorUsageSupported untyped
java_lang_Threading_ObjectMonitorUsageSupported 1.0
# HELP java_lang_GarbageCollector_LastGcInfo_duration CompositeType for GC info for Copy (java.lang<type=GarbageCollector, name=Copy><LastGcInfo>duration)
# TYPE java_lang_GarbageCollector_LastGcInfo_duration untyped
java_lang_GarbageCollector_LastGcInfo_duration{name="Copy",} 4.0
java_lang_GarbageCollector_LastGcInfo_duration{name="MarkSweepCompact",} 268.0
# HELP java_lang_GarbageCollector_LastGcInfo_memoryUsageAfterGc_max java.lang.management.MemoryUsage (java.lang<type=GarbageCollector, name=Copy, key=Survivor Space><LastGcInfo, memoryUsageAfterGc>max)
# TYPE java_lang_GarbageCollector_LastGcInfo_memoryUsageAfterGc_max untyped
java_lang_GarbageCollector_LastGcInfo_memoryUsageAfterGc_max{name="Copy",key="Survivor Space",} 3.5782656E7
java_lang_GarbageCollector_LastGcInfo_memoryUsageAfterGc_max{name="Copy",key="Compressed Class Space",} 1.073741824E9
java_lang_GarbageCollector_LastGcInfo_memoryUsageAfterGc_max{name="Copy",key="Eden Space",} 2.86326784E8
java_lang_GarbageCollector_LastGcInfo_memoryUsageAfterGc_max{name="Copy",key="Metaspace",} -1.0
java_lang_GarbageCollector_LastGcInfo_memoryUsageAfterGc_max{name="Copy",key="Code Cache",} 2.5165824E8
java_lang_GarbageCollector_LastGcInfo_memoryUsageAfterGc_max{name="Copy",key="Tenured Gen",} 7.15849728E8
java_lang_GarbageCollector_LastGcInfo_memoryUsageAfterGc_max{name="MarkSweepCompact",key="Survivor Space",} 3.5782656E7
java_lang_GarbageCollector_LastGcInfo_memoryUsageAfterGc_max{name="MarkSweepCompact",key="Compressed Class Space",} 1.073741824E9
java_lang_GarbageCollector_LastGcInfo_memoryUsageAfterGc_max{name="MarkSweepCompact",key="Eden Space",} 2.86326784E8
java_lang_GarbageCollector_LastGcInfo_memoryUsageAfterGc_max{name="MarkSweepCompact",key="Metaspace",} -1.0
java_lang_GarbageCollector_LastGcInfo_memoryUsageAfterGc_max{name="MarkSweepCompact",key="Code Cache",} 2.5165824E8
java_lang_GarbageCollector_LastGcInfo_memoryUsageAfterGc_max{name="MarkSweepCompact",key="Tenured Gen",} 7.15849728E8
# HELP java_lang_Threading_ThreadCpuTimeEnabled ThreadCpuTimeEnabled (java.lang<type=Threading><>ThreadCpuTimeEnabled)
# TYPE java_lang_Threading_ThreadCpuTimeEnabled untyped
java_lang_Threading_ThreadCpuTimeEnabled 1.0
# HELP java_lang_OperatingSystem_OpenFileDescriptorCount OpenFileDescriptorCount (java.lang<type=OperatingSystem><>OpenFileDescriptorCount)
# TYPE java_lang_OperatingSystem_OpenFileDescriptorCount untyped
java_lang_OperatingSystem_OpenFileDescriptorCount 399.0
# HELP jmx_scrape_duration_seconds Time this JMX scrape took, in seconds.
# TYPE jmx_scrape_duration_seconds gauge
jmx_scrape_duration_seconds 0.092074279
# HELP jmx_scrape_error Non-zero if this scrape failed.
# TYPE jmx_scrape_error gauge
jmx_scrape_error 0.0
# HELP jmx_scrape_cached_beans Number of beans with their matching rule cached
# TYPE jmx_scrape_cached_beans gauge
jmx_scrape_cached_beans 0.0
# HELP pulsar_source_source_exception Exception from source.
# TYPE pulsar_source_source_exception gauge
# HELP process_cpu_seconds_total Total user and system CPU time spent in seconds.
# TYPE process_cpu_seconds_total counter
process_cpu_seconds_total 38.79
# HELP process_start_time_seconds Start time of the process since unix epoch in seconds.
# TYPE process_start_time_seconds gauge
process_start_time_seconds 1.650931647403E9
# HELP process_open_fds Number of open file descriptors.
# TYPE process_open_fds gauge
process_open_fds 399.0
# HELP process_max_fds Maximum number of open file descriptors.
# TYPE process_max_fds gauge
process_max_fds 100000.0
# HELP process_virtual_memory_bytes Virtual memory size in bytes.
# TYPE process_virtual_memory_bytes gauge
process_virtual_memory_bytes 3.245871104E9
# HELP process_resident_memory_bytes Resident memory size in bytes.
# TYPE process_resident_memory_bytes gauge
process_resident_memory_bytes 3.2917504E8
# HELP jvm_memory_bytes_used Used bytes of a given JVM memory area.
# TYPE jvm_memory_bytes_used gauge
jvm_memory_bytes_used{area="heap",} 6.193488E7
jvm_memory_bytes_used{area="nonheap",} 9.2527408E7
# HELP jvm_memory_bytes_committed Committed (bytes) of a given JVM memory area.
# TYPE jvm_memory_bytes_committed gauge
jvm_memory_bytes_committed{area="heap",} 8.869888E7
jvm_memory_bytes_committed{area="nonheap",} 9.7058816E7
# HELP jvm_memory_bytes_max Max (bytes) of a given JVM memory area.
# TYPE jvm_memory_bytes_max gauge
jvm_memory_bytes_max{area="heap",} 1.037959168E9
jvm_memory_bytes_max{area="nonheap",} -1.0
# HELP jvm_memory_bytes_init Initial bytes of a given JVM memory area.
# TYPE jvm_memory_bytes_init gauge
jvm_memory_bytes_init{area="heap",} 6.5011712E7
jvm_memory_bytes_init{area="nonheap",} 2555904.0
# HELP jvm_memory_pool_bytes_used Used bytes of a given JVM memory pool.
# TYPE jvm_memory_pool_bytes_used gauge
jvm_memory_pool_bytes_used{pool="Code Cache",} 1.9315648E7
jvm_memory_pool_bytes_used{pool="Metaspace",} 6.5394776E7
jvm_memory_pool_bytes_used{pool="Compressed Class Space",} 7816984.0
jvm_memory_pool_bytes_used{pool="Eden Space",} 1.1267208E7
jvm_memory_pool_bytes_used{pool="Survivor Space",} 1687192.0
jvm_memory_pool_bytes_used{pool="Tenured Gen",} 4.898048E7
# HELP jvm_memory_pool_bytes_committed Committed bytes of a given JVM memory pool.
# TYPE jvm_memory_pool_bytes_committed gauge
jvm_memory_pool_bytes_committed{pool="Code Cache",} 2.0774912E7
jvm_memory_pool_bytes_committed{pool="Metaspace",} 6.8026368E7
jvm_memory_pool_bytes_committed{pool="Compressed Class Space",} 8257536.0
jvm_memory_pool_bytes_committed{pool="Eden Space",} 2.4641536E7
jvm_memory_pool_bytes_committed{pool="Survivor Space",} 3014656.0
jvm_memory_pool_bytes_committed{pool="Tenured Gen",} 6.1042688E7
# HELP jvm_memory_pool_bytes_max Max bytes of a given JVM memory pool.
# TYPE jvm_memory_pool_bytes_max gauge
jvm_memory_pool_bytes_max{pool="Code Cache",} 2.5165824E8
jvm_memory_pool_bytes_max{pool="Metaspace",} -1.0
jvm_memory_pool_bytes_max{pool="Compressed Class Space",} 1.073741824E9
jvm_memory_pool_bytes_max{pool="Eden Space",} 2.86326784E8
jvm_memory_pool_bytes_max{pool="Survivor Space",} 3.5782656E7
jvm_memory_pool_bytes_max{pool="Tenured Gen",} 7.15849728E8
# HELP jvm_memory_pool_bytes_init Initial bytes of a given JVM memory pool.
# TYPE jvm_memory_pool_bytes_init gauge
jvm_memory_pool_bytes_init{pool="Code Cache",} 2555904.0
jvm_memory_pool_bytes_init{pool="Metaspace",} 0.0
jvm_memory_pool_bytes_init{pool="Compressed Class Space",} 0.0
jvm_memory_pool_bytes_init{pool="Eden Space",} 1.7301504E7
jvm_memory_pool_bytes_init{pool="Survivor Space",} 2162688.0
jvm_memory_pool_bytes_init{pool="Tenured Gen",} 4.3384832E7
# HELP pulsar_source_written_total_1min Total number of records written to a Pulsar topic in the last 1 minute.
# TYPE pulsar_source_written_total_1min counter
pulsar_source_written_total_1min{tenant="public",namespace="public/default",name="cassandra-source-sales-sales_orders",instance_id="0",cluster="MyPulsarCluster",fqfn="public/default/cassandra-source-sales-sales_orders",} 0.0
# HELP pulsar_source_source_exceptions_total_1min Total number of source exceptions in the last 1 minute.
# TYPE pulsar_source_source_exceptions_total_1min counter
pulsar_source_source_exceptions_total_1min{tenant="public",namespace="public/default",name="cassandra-source-sales-sales_orders",instance_id="0",cluster="MyPulsarCluster",fqfn="public/default/cassandra-source-sales-sales_orders",} 0.0
# HELP pulsar_source_source_exceptions_total Total number of source exceptions.
# TYPE pulsar_source_source_exceptions_total counter
pulsar_source_source_exceptions_total{tenant="public",namespace="public/default",name="cassandra-source-sales-sales_orders",instance_id="0",cluster="MyPulsarCluster",fqfn="public/default/cassandra-source-sales-sales_orders",} 0.0
# HELP pulsar_source_written_total Total number of records written to a Pulsar topic.
# TYPE pulsar_source_written_total counter
pulsar_source_written_total{tenant="public",namespace="public/default",name="cassandra-source-sales-sales_orders",instance_id="0",cluster="MyPulsarCluster",fqfn="public/default/cassandra-source-sales-sales_orders",} 22881.0
# HELP jvm_info JVM version info
# TYPE jvm_info gauge
jvm_info{version="1.8.0_322-b06",vendor="Red Hat, Inc.",runtime="OpenJDK Runtime Environment",} 1.0
# HELP pulsar_source_last_invocation The timestamp of the last invocation of the source.
# TYPE pulsar_source_last_invocation gauge
pulsar_source_last_invocation{tenant="public",namespace="public/default",name="cassandra-source-sales-sales_orders",instance_id="0",cluster="MyPulsarCluster",fqfn="public/default/cassandra-source-sales-sales_orders",} 1.650931927302E12
# HELP pulsar_source_system_exceptions_total Total number of system exceptions.
# TYPE pulsar_source_system_exceptions_total counter
pulsar_source_system_exceptions_total{tenant="public",namespace="public/default",name="cassandra-source-sales-sales_orders",instance_id="0",cluster="MyPulsarCluster",fqfn="public/default/cassandra-source-sales-sales_orders",} 0.0
# HELP jvm_classes_loaded The number of classes that are currently loaded in the JVM
# TYPE jvm_classes_loaded gauge
jvm_classes_loaded 10871.0
# HELP jvm_classes_loaded_total The total number of classes that have been loaded since the JVM has started execution
# TYPE jvm_classes_loaded_total counter
jvm_classes_loaded_total 10871.0
# HELP jvm_classes_unloaded_total The total number of classes that have been unloaded since the JVM has started execution
# TYPE jvm_classes_unloaded_total counter
jvm_classes_unloaded_total 0.0
# TYPE pulsar_ml_cache_evictions gauge
pulsar_ml_cache_evictions{cluster="MyPulsarCluster"} 0 1650931969479
# TYPE pulsar_ml_cache_hits_rate gauge
pulsar_ml_cache_hits_rate{cluster="MyPulsarCluster"} 0.0 1650931969479
# TYPE pulsar_ml_cache_hits_throughput gauge
pulsar_ml_cache_hits_throughput{cluster="MyPulsarCluster"} 0.0 1650931969479
# TYPE pulsar_ml_cache_misses_rate gauge
pulsar_ml_cache_misses_rate{cluster="MyPulsarCluster"} 0.0 1650931969479
# TYPE pulsar_ml_cache_misses_throughput gauge
pulsar_ml_cache_misses_throughput{cluster="MyPulsarCluster"} 0.0 1650931969479
# TYPE pulsar_ml_cache_pool_active_allocations gauge
pulsar_ml_cache_pool_active_allocations{cluster="MyPulsarCluster"} 0 1650931969479
# TYPE pulsar_ml_cache_pool_active_allocations_huge gauge
pulsar_ml_cache_pool_active_allocations_huge{cluster="MyPulsarCluster"} 0 1650931969479
# TYPE pulsar_ml_cache_pool_active_allocations_normal gauge
pulsar_ml_cache_pool_active_allocations_normal{cluster="MyPulsarCluster"} 0 1650931969479
# TYPE pulsar_ml_cache_pool_active_allocations_small gauge
pulsar_ml_cache_pool_active_allocations_small{cluster="MyPulsarCluster"} 0 1650931969479
# TYPE pulsar_ml_cache_pool_active_allocations_tiny gauge
pulsar_ml_cache_pool_active_allocations_tiny{cluster="MyPulsarCluster"} 0 1650931969479
# TYPE pulsar_ml_cache_pool_allocated gauge
pulsar_ml_cache_pool_allocated{cluster="MyPulsarCluster"} 0 1650931969479
# TYPE pulsar_ml_cache_pool_used gauge
pulsar_ml_cache_pool_used{cluster="MyPulsarCluster"} 0 1650931969479
# TYPE pulsar_ml_cache_used_size gauge
pulsar_ml_cache_used_size{cluster="MyPulsarCluster"} 0 1650931969479
# TYPE pulsar_ml_count gauge
pulsar_ml_count{cluster="MyPulsarCluster"} 5 1650931969479
# TYPE pulsar_ml_AddEntryBytesRate gauge
pulsar_ml_AddEntryBytesRate{cluster="MyPulsarCluster", namespace="public/functions/persistent"} 0.0 1650931969479
# TYPE pulsar_ml_AddEntryErrors gauge
pulsar_ml_AddEntryErrors{cluster="MyPulsarCluster", namespace="public/functions/persistent"} 0.0 1650931969479
# TYPE pulsar_ml_AddEntryLatencyBuckets gauge
pulsar_ml_AddEntryLatencyBuckets{cluster="MyPulsarCluster", namespace="public/functions/persistent", quantile="0.0_0.5"} 0.0 1650931969479
pulsar_ml_AddEntryLatencyBuckets{cluster="MyPulsarCluster", namespace="public/functions/persistent", quantile="0.5_1.0"} 0.0 1650931969479
pulsar_ml_AddEntryLatencyBuckets{cluster="MyPulsarCluster", namespace="public/functions/persistent", quantile="1.0_5.0"} 0.0 1650931969479
pulsar_ml_AddEntryLatencyBuckets{cluster="MyPulsarCluster", namespace="public/functions/persistent", quantile="10.0_20.0"} 0.0 1650931969479
pulsar_ml_AddEntryLatencyBuckets{cluster="MyPulsarCluster", namespace="public/functions/persistent", quantile="100.0_200.0"} 0.0 1650931969479
pulsar_ml_AddEntryLatencyBuckets{cluster="MyPulsarCluster", namespace="public/functions/persistent", quantile="20.0_50.0"} 0.0 1650931969479
pulsar_ml_AddEntryLatencyBuckets{cluster="MyPulsarCluster", namespace="public/functions/persistent", quantile="200.0_1000.0"} 0.0 1650931969479
pulsar_ml_AddEntryLatencyBuckets{cluster="MyPulsarCluster", namespace="public/functions/persistent", quantile="5.0_10.0"} 0.0 1650931969479
pulsar_ml_AddEntryLatencyBuckets{cluster="MyPulsarCluster", namespace="public/functions/persistent", quantile="50.0_100.0"} 0.0 1650931969479
# TYPE pulsar_ml_AddEntryLatencyBuckets_OVERFLOW gauge
pulsar_ml_AddEntryLatencyBuckets_OVERFLOW{cluster="MyPulsarCluster", namespace="public/functions/persistent"} 0.0 1650931969479
# TYPE pulsar_ml_AddEntryMessagesRate gauge
pulsar_ml_AddEntryMessagesRate{cluster="MyPulsarCluster", namespace="public/functions/persistent"} 0.0 1650931969479
# TYPE pulsar_ml_AddEntrySucceed gauge
pulsar_ml_AddEntrySucceed{cluster="MyPulsarCluster", namespace="public/functions/persistent"} 0.0 1650931969479
# TYPE pulsar_ml_AddEntryWithReplicasBytesRate gauge
pulsar_ml_AddEntryWithReplicasBytesRate{cluster="MyPulsarCluster", namespace="public/functions/persistent"} 0.0 1650931969479
# TYPE pulsar_ml_EntrySizeBuckets gauge
pulsar_ml_EntrySizeBuckets{cluster="MyPulsarCluster", namespace="public/functions/persistent", quantile="0.0_128.0"} 0.0 1650931969479
pulsar_ml_EntrySizeBuckets{cluster="MyPulsarCluster", namespace="public/functions/persistent", quantile="1024.0_2048.0"} 0.0 1650931969479
pulsar_ml_EntrySizeBuckets{cluster="MyPulsarCluster", namespace="public/functions/persistent", quantile="102400.0_1232896.0"} 0.0 1650931969479
pulsar_ml_EntrySizeBuckets{cluster="MyPulsarCluster", namespace="public/functions/persistent", quantile="128.0_512.0"} 0.0 1650931969479
pulsar_ml_EntrySizeBuckets{cluster="MyPulsarCluster", namespace="public/functions/persistent", quantile="16384.0_102400.0"} 0.0 1650931969479
pulsar_ml_EntrySizeBuckets{cluster="MyPulsarCluster", namespace="public/functions/persistent", quantile="2048.0_4096.0"} 0.0 1650931969479
pulsar_ml_EntrySizeBuckets{cluster="MyPulsarCluster", namespace="public/functions/persistent", quantile="4096.0_16384.0"} 0.0 1650931969479
pulsar_ml_EntrySizeBuckets{cluster="MyPulsarCluster", namespace="public/functions/persistent", quantile="512.0_1024.0"} 0.0 1650931969479
# TYPE pulsar_ml_EntrySizeBuckets_OVERFLOW gauge
pulsar_ml_EntrySizeBuckets_OVERFLOW{cluster="MyPulsarCluster", namespace="public/functions/persistent"} 0.0 1650931969479
# TYPE pulsar_ml_LedgerAddEntryLatencyBuckets gauge
pulsar_ml_LedgerAddEntryLatencyBuckets{cluster="MyPulsarCluster", namespace="public/functions/persistent", quantile="0.0_0.5"} 0.0 1650931969479
pulsar_ml_LedgerAddEntryLatencyBuckets{cluster="MyPulsarCluster", namespace="public/functions/persistent", quantile="0.5_1.0"} 0.0 1650931969479
pulsar_ml_LedgerAddEntryLatencyBuckets{cluster="MyPulsarCluster", namespace="public/functions/persistent", quantile="1.0_5.0"} 0.0 1650931969479
pulsar_ml_LedgerAddEntryLatencyBuckets{cluster="MyPulsarCluster", namespace="public/functions/persistent", quantile="10.0_20.0"} 0.0 1650931969479
pulsar_ml_LedgerAddEntryLatencyBuckets{cluster="MyPulsarCluster", namespace="public/functions/persistent", quantile="100.0_200.0"} 0.0 1650931969479
pulsar_ml_LedgerAddEntryLatencyBuckets{cluster="MyPulsarCluster", namespace="public/functions/persistent", quantile="20.0_50.0"} 0.0 1650931969479
pulsar_ml_LedgerAddEntryLatencyBuckets{cluster="MyPulsarCluster", namespace="public/functions/persistent", quantile="200.0_1000.0"} 0.0 1650931969479
pulsar_ml_LedgerAddEntryLatencyBuckets{cluster="MyPulsarCluster", namespace="public/functions/persistent", quantile="5.0_10.0"} 0.0 1650931969479
pulsar_ml_LedgerAddEntryLatencyBuckets{cluster="MyPulsarCluster", namespace="public/functions/persistent", quantile="50.0_100.0"} 0.0 1650931969479
# TYPE pulsar_ml_LedgerAddEntryLatencyBuckets_OVERFLOW gauge
pulsar_ml_LedgerAddEntryLatencyBuckets_OVERFLOW{cluster="MyPulsarCluster", namespace="public/functions/persistent"} 0.0 1650931969479
# TYPE pulsar_ml_LedgerSwitchLatencyBuckets gauge
pulsar_ml_LedgerSwitchLatencyBuckets{cluster="MyPulsarCluster", namespace="public/functions/persistent", quantile="0.0_0.5"} 0.0 1650931969479
pulsar_ml_LedgerSwitchLatencyBuckets{cluster="MyPulsarCluster", namespace="public/functions/persistent", quantile="0.5_1.0"} 0.0 1650931969479
pulsar_ml_LedgerSwitchLatencyBuckets{cluster="MyPulsarCluster", namespace="public/functions/persistent", quantile="1.0_5.0"} 0.0 1650931969479
pulsar_ml_LedgerSwitchLatencyBuckets{cluster="MyPulsarCluster", namespace="public/functions/persistent", quantile="10.0_20.0"} 0.0 1650931969479
pulsar_ml_LedgerSwitchLatencyBuckets{cluster="MyPulsarCluster", namespace="public/functions/persistent", quantile="100.0_200.0"} 0.0 1650931969479
pulsar_ml_LedgerSwitchLatencyBuckets{cluster="MyPulsarCluster", namespace="public/functions/persistent", quantile="20.0_50.0"} 0.0 1650931969479
pulsar_ml_LedgerSwitchLatencyBuckets{cluster="MyPulsarCluster", namespace="public/functions/persistent", quantile="200.0_1000.0"} 0.0 1650931969479
pulsar_ml_LedgerSwitchLatencyBuckets{cluster="MyPulsarCluster", namespace="public/functions/persistent", quantile="5.0_10.0"} 0.0 1650931969479
pulsar_ml_LedgerSwitchLatencyBuckets{cluster="MyPulsarCluster", namespace="public/functions/persistent", quantile="50.0_100.0"} 0.0 1650931969479
# TYPE pulsar_ml_LedgerSwitchLatencyBuckets_OVERFLOW gauge
pulsar_ml_LedgerSwitchLatencyBuckets_OVERFLOW{cluster="MyPulsarCluster", namespace="public/functions/persistent"} 0.0 1650931969480
# TYPE pulsar_ml_MarkDeleteRate gauge
pulsar_ml_MarkDeleteRate{cluster="MyPulsarCluster", namespace="public/functions/persistent"} 0.0 1650931969480
# TYPE pulsar_ml_NumberOfMessagesInBacklog gauge
pulsar_ml_NumberOfMessagesInBacklog{cluster="MyPulsarCluster", namespace="public/functions/persistent"} 0.0 1650931969480
# TYPE pulsar_ml_ReadEntriesBytesRate gauge
pulsar_ml_ReadEntriesBytesRate{cluster="MyPulsarCluster", namespace="public/functions/persistent"} 0.0 1650931969480
# TYPE pulsar_ml_ReadEntriesErrors gauge
pulsar_ml_ReadEntriesErrors{cluster="MyPulsarCluster", namespace="public/functions/persistent"} 0.0 1650931969480
# TYPE pulsar_ml_ReadEntriesRate gauge
pulsar_ml_ReadEntriesRate{cluster="MyPulsarCluster", namespace="public/functions/persistent"} 0.0 1650931969480
# TYPE pulsar_ml_ReadEntriesSucceeded gauge
pulsar_ml_ReadEntriesSucceeded{cluster="MyPulsarCluster", namespace="public/functions/persistent"} 0.0 1650931969480
# TYPE pulsar_ml_StoredMessagesSize gauge
pulsar_ml_StoredMessagesSize{cluster="MyPulsarCluster", namespace="public/functions/persistent"} 1430.0 1650931969480
pulsar_ml_AddEntryBytesRate{cluster="MyPulsarCluster", namespace="sales_tenant/sales_ns/persistent"} 0.0 1650931969480
pulsar_ml_AddEntryErrors{cluster="MyPulsarCluster", namespace="sales_tenant/sales_ns/persistent"} 0.0 1650931969480
pulsar_ml_AddEntryLatencyBuckets{cluster="MyPulsarCluster", namespace="sales_tenant/sales_ns/persistent", quantile="0.0_0.5"} 0.0 1650931969480
pulsar_ml_AddEntryLatencyBuckets{cluster="MyPulsarCluster", namespace="sales_tenant/sales_ns/persistent", quantile="0.5_1.0"} 0.0 1650931969480
pulsar_ml_AddEntryLatencyBuckets{cluster="MyPulsarCluster", namespace="sales_tenant/sales_ns/persistent", quantile="1.0_5.0"} 0.0 1650931969480
pulsar_ml_AddEntryLatencyBuckets{cluster="MyPulsarCluster", namespace="sales_tenant/sales_ns/persistent", quantile="10.0_20.0"} 0.0 1650931969480
pulsar_ml_AddEntryLatencyBuckets{cluster="MyPulsarCluster", namespace="sales_tenant/sales_ns/persistent", quantile="100.0_200.0"} 0.0 1650931969480
pulsar_ml_AddEntryLatencyBuckets{cluster="MyPulsarCluster", namespace="sales_tenant/sales_ns/persistent", quantile="20.0_50.0"} 0.0 1650931969480
pulsar_ml_AddEntryLatencyBuckets{cluster="MyPulsarCluster", namespace="sales_tenant/sales_ns/persistent", quantile="200.0_1000.0"} 0.0 1650931969480
pulsar_ml_AddEntryLatencyBuckets{cluster="MyPulsarCluster", namespace="sales_tenant/sales_ns/persistent", quantile="5.0_10.0"} 0.0 1650931969480
pulsar_ml_AddEntryLatencyBuckets{cluster="MyPulsarCluster", namespace="sales_tenant/sales_ns/persistent", quantile="50.0_100.0"} 0.0 1650931969480
pulsar_ml_AddEntryLatencyBuckets_OVERFLOW{cluster="MyPulsarCluster", namespace="sales_tenant/sales_ns/persistent"} 0.0 1650931969480
pulsar_ml_AddEntryMessagesRate{cluster="MyPulsarCluster", namespace="sales_tenant/sales_ns/persistent"} 0.0 1650931969480
pulsar_ml_AddEntrySucceed{cluster="MyPulsarCluster", namespace="sales_tenant/sales_ns/persistent"} 0.0 1650931969480
pulsar_ml_AddEntryWithReplicasBytesRate{cluster="MyPulsarCluster", namespace="sales_tenant/sales_ns/persistent"} 0.0 1650931969480
pulsar_ml_EntrySizeBuckets{cluster="MyPulsarCluster", namespace="sales_tenant/sales_ns/persistent", quantile="0.0_128.0"} 0.0 1650931969480
pulsar_ml_EntrySizeBuckets{cluster="MyPulsarCluster", namespace="sales_tenant/sales_ns/persistent", quantile="1024.0_2048.0"} 0.0 1650931969480
pulsar_ml_EntrySizeBuckets{cluster="MyPulsarCluster", namespace="sales_tenant/sales_ns/persistent", quantile="102400.0_1232896.0"} 0.0 1650931969480
pulsar_ml_EntrySizeBuckets{cluster="MyPulsarCluster", namespace="sales_tenant/sales_ns/persistent", quantile="128.0_512.0"} 0.0 1650931969480
pulsar_ml_EntrySizeBuckets{cluster="MyPulsarCluster", namespace="sales_tenant/sales_ns/persistent", quantile="16384.0_102400.0"} 0.0 1650931969480
pulsar_ml_EntrySizeBuckets{cluster="MyPulsarCluster", namespace="sales_tenant/sales_ns/persistent", quantile="2048.0_4096.0"} 0.0 1650931969480
pulsar_ml_EntrySizeBuckets{cluster="MyPulsarCluster", namespace="sales_tenant/sales_ns/persistent", quantile="4096.0_16384.0"} 0.0 1650931969480
pulsar_ml_EntrySizeBuckets{cluster="MyPulsarCluster", namespace="sales_tenant/sales_ns/persistent", quantile="512.0_1024.0"} 0.0 1650931969480
pulsar_ml_EntrySizeBuckets_OVERFLOW{cluster="MyPulsarCluster", namespace="sales_tenant/sales_ns/persistent"} 0.0 1650931969480
pulsar_ml_LedgerAddEntryLatencyBuckets{cluster="MyPulsarCluster", namespace="sales_tenant/sales_ns/persistent", quantile="0.0_0.5"} 0.0 1650931969480
pulsar_ml_LedgerAddEntryLatencyBuckets{cluster="MyPulsarCluster", namespace="sales_tenant/sales_ns/persistent", quantile="0.5_1.0"} 0.0 1650931969480
pulsar_ml_LedgerAddEntryLatencyBuckets{cluster="MyPulsarCluster", namespace="sales_tenant/sales_ns/persistent", quantile="1.0_5.0"} 0.0 1650931969480
pulsar_ml_LedgerAddEntryLatencyBuckets{cluster="MyPulsarCluster", namespace="sales_tenant/sales_ns/persistent", quantile="10.0_20.0"} 0.0 1650931969480
pulsar_ml_LedgerAddEntryLatencyBuckets{cluster="MyPulsarCluster", namespace="sales_tenant/sales_ns/persistent", quantile="100.0_200.0"} 0.0 1650931969480
pulsar_ml_LedgerAddEntryLatencyBuckets{cluster="MyPulsarCluster", namespace="sales_tenant/sales_ns/persistent", quantile="20.0_50.0"} 0.0 1650931969480
pulsar_ml_LedgerAddEntryLatencyBuckets{cluster="MyPulsarCluster", namespace="sales_tenant/sales_ns/persistent", quantile="200.0_1000.0"} 0.0 1650931969480
pulsar_ml_LedgerAddEntryLatencyBuckets{cluster="MyPulsarCluster", namespace="sales_tenant/sales_ns/persistent", quantile="5.0_10.0"} 0.0 1650931969480
pulsar_ml_LedgerAddEntryLatencyBuckets{cluster="MyPulsarCluster", namespace="sales_tenant/sales_ns/persistent", quantile="50.0_100.0"} 0.0 1650931969480
pulsar_ml_LedgerAddEntryLatencyBuckets_OVERFLOW{cluster="MyPulsarCluster", namespace="sales_tenant/sales_ns/persistent"} 0.0 1650931969480
pulsar_ml_LedgerSwitchLatencyBuckets{cluster="MyPulsarCluster", namespace="sales_tenant/sales_ns/persistent", quantile="0.0_0.5"} 0.0 1650931969480
pulsar_ml_LedgerSwitchLatencyBuckets{cluster="MyPulsarCluster", namespace="sales_tenant/sales_ns/persistent", quantile="0.5_1.0"} 0.0 1650931969480
pulsar_ml_LedgerSwitchLatencyBuckets{cluster="MyPulsarCluster", namespace="sales_tenant/sales_ns/persistent", quantile="1.0_5.0"} 0.0 1650931969480
pulsar_ml_LedgerSwitchLatencyBuckets{cluster="MyPulsarCluster", namespace="sales_tenant/sales_ns/persistent", quantile="10.0_20.0"} 0.0 1650931969480
pulsar_ml_LedgerSwitchLatencyBuckets{cluster="MyPulsarCluster", namespace="sales_tenant/sales_ns/persistent", quantile="100.0_200.0"} 0.0 1650931969480
pulsar_ml_LedgerSwitchLatencyBuckets{cluster="MyPulsarCluster", namespace="sales_tenant/sales_ns/persistent", quantile="20.0_50.0"} 0.0 1650931969480
pulsar_ml_LedgerSwitchLatencyBuckets{cluster="MyPulsarCluster", namespace="sales_tenant/sales_ns/persistent", quantile="200.0_1000.0"} 0.0 1650931969480
pulsar_ml_LedgerSwitchLatencyBuckets{cluster="MyPulsarCluster", namespace="sales_tenant/sales_ns/persistent", quantile="5.0_10.0"} 0.0 1650931969480
pulsar_ml_LedgerSwitchLatencyBuckets{cluster="MyPulsarCluster", namespace="sales_tenant/sales_ns/persistent", quantile="50.0_100.0"} 0.0 1650931969480
pulsar_ml_LedgerSwitchLatencyBuckets_OVERFLOW{cluster="MyPulsarCluster", namespace="sales_tenant/sales_ns/persistent"} 0.0 1650931969480
pulsar_ml_MarkDeleteRate{cluster="MyPulsarCluster", namespace="sales_tenant/sales_ns/persistent"} 0.01666722224074136 1650931969480
pulsar_ml_NumberOfMessagesInBacklog{cluster="MyPulsarCluster", namespace="sales_tenant/sales_ns/persistent"} 0.0 1650931969480
pulsar_ml_ReadEntriesBytesRate{cluster="MyPulsarCluster", namespace="sales_tenant/sales_ns/persistent"} 0.0 1650931969480
pulsar_ml_ReadEntriesErrors{cluster="MyPulsarCluster", namespace="sales_tenant/sales_ns/persistent"} 0.0 1650931969480
pulsar_ml_ReadEntriesRate{cluster="MyPulsarCluster", namespace="sales_tenant/sales_ns/persistent"} 0.0 1650931969480
pulsar_ml_ReadEntriesSucceeded{cluster="MyPulsarCluster", namespace="sales_tenant/sales_ns/persistent"} 0.0 1650931969480
pulsar_ml_StoredMessagesSize{cluster="MyPulsarCluster", namespace="sales_tenant/sales_ns/persistent"} 1.7013678E7 1650931969480
# TYPE pulsar_active_connections gauge
pulsar_active_connections{cluster="MyPulsarCluster", broker="localhost", metric="broker_connection"} 8 1650931969480
# TYPE pulsar_connection_closed_total_count gauge
pulsar_connection_closed_total_count{cluster="MyPulsarCluster", broker="localhost", metric="broker_connection"} 0 1650931969480
# TYPE pulsar_connection_create_fail_count gauge
pulsar_connection_create_fail_count{cluster="MyPulsarCluster", broker="localhost", metric="broker_connection"} 0 1650931969480
# TYPE pulsar_connection_create_success_count gauge
pulsar_connection_create_success_count{cluster="MyPulsarCluster", broker="localhost", metric="broker_connection"} 8 1650931969480
# TYPE pulsar_connection_created_total_count gauge
pulsar_connection_created_total_count{cluster="MyPulsarCluster", broker="localhost", metric="broker_connection"} 8 1650931969480
```
