# Apache Pulsar - Admin Commands
https://pulsar.apache.org/docs/en/pulsar-admin/


```
~/pulsar-current/bin/pulsar-admin clusters list

~/pulsar-current/bin/pulsar-admin tenants list
```

<br>

## We will create a new tenant ` sales_tenant ` :

```
~/pulsar-current/bin/pulsar-admin tenants create sales_tenant
```

<br>

## We will create a new namespace ` sales_ns ` in ` sales_tenant ` :

```
~/pulsar-current/bin/pulsar-admin namespaces create "sales_tenant/sales_ns"
```

<br>

## We can list namespaces under ` sales_tenant ` :

```
~/pulsar-current/bin/pulsar-admin namespaces list "sales_tenant"
```

<br>

## We can list topics under ` sales_tenant/sales_ns ` :

```
~/pulsar-current/bin/pulsar-admin topics list "sales_tenant/sales_ns"
```

