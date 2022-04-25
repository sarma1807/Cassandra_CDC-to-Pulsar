# In Apache Cassandra, CDC can be Enabled at TABLE Level


```
cqlsh>
SELECT keyspace_name, table_name, cdc
FROM system_schema.tables
WHERE keyspace_name = 'sales'
AND table_name IN ('products', 'sales_orders') ;

 keyspace_name | table_name   | cdc
---------------+--------------+-------
         sales |     products | False
         sales | sales_orders | False
```



` $ cqlsh --execute="use sales; desc schema;" | egrep "CREATE TABLE|cdc =" `
```
CREATE TABLE sales.products (
    AND cdc = false
CREATE TABLE sales.sales_orders (
    AND cdc = false
```

---

## Enable CDC on ` sales_orders ` table

```
cqlsh>
ALTER TABLE sales.sales_orders WITH cdc = true ;
```

---

```
cqlsh>
SELECT keyspace_name, table_name, cdc
FROM system_schema.tables
WHERE keyspace_name = 'sales'
AND table_name IN ('products', 'sales_orders') ;

 keyspace_name | table_name   | cdc
---------------+--------------+-------
         sales |     products | False
         sales | sales_orders |  True
```



` $ cqlsh --execute="use sales; desc schema;" | egrep "CREATE TABLE|cdc =" `
```
CREATE TABLE sales.products (
    AND cdc = false
CREATE TABLE sales.sales_orders (
    AND cdc = true
```

---

## We have Enabled CDC on ` sales_orders ` table

