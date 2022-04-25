# Monitor CDC Files

#### After we have enabled CDC feature and also modified "cdc = true" for required tables, we can check ` cdc_raw ` folder.
#### ` cdc_raw ` folder will now have ` CommitLog-*_cdc.idx ` files.

<br>

```
$ ls -ltrh ~/data/cdc_raw
-rw-r--r-- 1 cassandra cassgrp 32M Mar 31 07:32 CommitLog-7-1648725886727.log
-rw-r--r-- 2 cassandra cassgrp 32M Mar 31 07:37 CommitLog-7-1648726655310.log
-rw-r--r-- 2 cassandra cassgrp 32M Mar 31 10:26 CommitLog-7-1648726655309.log
-rw-r--r-- 1 cassandra cassgrp   8 Mar 31 10:26 CommitLog-7-1648726655309_cdc.idx
$
```

```
$ file ~/data/cdc_raw/CommitLog-7-1648726655309_cdc.idx
CommitLog-7-1648726655309_cdc.idx: ASCII text, with no line terminators
```

```
$ cat ~/data/cdc_raw/CommitLog-7-1648726655309_cdc.idx
14410080
$
```

#### ` CommitLog-*_cdc.idx ` files only contain an offset info to the CommitLogSegment.

