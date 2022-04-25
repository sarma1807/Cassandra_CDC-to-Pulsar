# Enable Apache Cassandra CDC (Change-Data-Capture) Feature

### CDC provides a mechanism to flag specific tables for archival as well as rejecting writes to those tables once a configurable size-on-disk for the CDC log is reached.


## vi <CASSANDRA_HOME>/conf/cassandra.yaml
```
# MODIFY THESE CONFIGURATION VALUES ON ALL NODES OF CASSANDRA WHICH BELONG TO SAME DATA CENTER

### by default CDC is disabled
# cdc_enabled: false
cdc_enabled: true


### location for cdc files
### it is suggested to put this on a dedicated mount away from data files
cdc_raw_directory: /apps/opt/cassandra/data/cdc_raw


### default space allocated for CDC is 4096 mb
### after this space is filled ... CDC enabled tables will reject future writes until CDC files are consumed and cleared
cdc_total_space_in_mb: 10240


# cdc_free_space_check_interval_ms: 250

```

### Restart all nodes in the Cassandra cluster to Enable CDC

---

### At this point, if you notice ` commitlogs ` folder and ` cdc_raw ` folder, they will contain similar files.

```
$ ls -lh ~/data/commitlog/
-rw-r--r-- 2 cassandra cassgrp 32M Mar 31 07:37 CommitLog-7-1648726655310.log
-rw-r--r-- 2 cassandra cassgrp 32M Mar 31 08:43 CommitLog-7-1648726655309.log
$
```
```
$ ls -lh ~/data/cdc_raw/
-rw-r--r-- 1 cassandra cassgrp 32M Mar 31 07:32 CommitLog-7-1648725886727.log
-rw-r--r-- 2 cassandra cassgrp 32M Mar 31 07:37 CommitLog-7-1648726655310.log
-rw-r--r-- 2 cassandra cassgrp 32M Mar 31 08:43 CommitLog-7-1648726655309.log
$
```

## one big noticeable difference :
### ` commitlog ` files are cleaned up when they are no longer required.
### ` cdc_raw ` files are NOT cleaned up automatically.

---

