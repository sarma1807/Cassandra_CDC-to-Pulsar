# Pulsar Schema Registry

### Cassandra CDC Agent & Source Connector will publish the schema in AVRO format

---

### schema for event topic :

` ~/pulsar-current/bin/pulsar-admin schemas get persistent://sales_tenant/sales_ns/events-sales.sales_orders `

```
{
  "version": 0,
  "schemaInfo": {
    "name": "events-sales.sales_orders",
    "schema": {
      "key": {
        "name": "sales_orders",
        "schema": {
          "type": "record",
          "name": "sales_orders",
          "namespace": "sales",
          "doc": "Primary key schema for table sales.sales_orders",
          "fields": [
            {
              "name": "order_date",
              "type": {
                "type": "int",
                "logicalType": "date"
              }
            },
            {
              "name": "order_date_hour",
              "type": "int"
            },
            {
              "name": "order_timestamp",
              "type": [
                "null",
                {
                  "type": "long",
                  "logicalType": "timestamp-millis"
                }
              ]
            },
            {
              "name": "order_code",
              "type": [
                "null",
                {
                  "type": "string",
                  "logicalType": "uuid"
                }
              ]
            }
          ]
        },
        "type": "AVRO",
        "properties": {}
      },
      "value": {
        "name": "",
        "schema": {
          "type": "record",
          "name": "MutationValue",
          "namespace": "com.datastax.oss.cdc",
          "fields": [
            {
              "name": "columns",
              "type": [
                "null",
                {
                  "type": "array",
                  "items": "string",
                  "java-class": "[Ljava.lang.String;"
                }
              ]
            },
            {
              "name": "md5Digest",
              "type": [
                "null",
                "string"
              ]
            },
            {
              "name": "nodeId",
              "type": [
                "null",
                {
                  "type": "string",
                  "logicalType": "uuid"
                }
              ]
            }
          ]
        },
        "type": "AVRO",
        "properties": {
          "__alwaysAllowNull": "true",
          "__jsr310ConversionEnabled": "false"
        }
      }
    },
    "type": "KEY_VALUE",
    "properties": {
      "key.schema.name": "sales_orders",
      "key.schema.properties": "{}",
      "key.schema.type": "AVRO",
      "kv.encoding.type": "SEPARATED",
      "value.schema.name": "",
      "value.schema.properties": "{\"__alwaysAllowNull\":\"true\",\"__jsr310ConversionEnabled\":\"false\"}",
      "value.schema.type": "AVRO"
    }
  }
}
```

---

### schema for data topic [WITH ALL COLUMNS] :

` ~/pulsar-current/bin/pulsar-admin schemas get persistent://sales_tenant/sales_ns/data-sales.sales_orders `

```
{
  "version": 0,
  "schemaInfo": {
    "name": "data-sales.sales_orders",
    "schema": {
      "key": {
        "name": "sales_orders",
        "schema": {
          "type": "record",
          "name": "sales_orders",
          "namespace": "sales",
          "doc": "Table sales.sales_orders",
          "fields": [
            {
              "name": "order_date",
              "type": {
                "type": "int",
                "logicalType": "date"
              }
            },
            {
              "name": "order_date_hour",
              "type": "int"
            },
            {
              "name": "order_timestamp",
              "type": [
                "null",
                {
                  "type": "long",
                  "logicalType": "timestamp-millis"
                }
              ]
            },
            {
              "name": "order_code",
              "type": [
                "null",
                {
                  "type": "string",
                  "logicalType": "uuid"
                }
              ]
            }
          ]
        },
        "type": "AVRO",
        "properties": {}
      },
      "value": {
        "name": "sales_orders",
        "schema": {
          "type": "record",
          "name": "sales_orders",
          "namespace": "sales",
          "doc": "Table sales.sales_orders",
          "fields": [
            {
              "name": "order_actual_shipping_date",
              "type": [
                "null",
                {
                  "type": "long",
                  "logicalType": "timestamp-millis"
                }
              ]
            },
            {
              "name": "order_discount_percent",
              "type": [
                "null",
                "int"
              ]
            },
            {
              "name": "order_estimated_shipping_date",
              "type": [
                "null",
                {
                  "type": "long",
                  "logicalType": "timestamp-millis"
                }
              ]
            },
            {
              "name": "order_grand_total",
              "type": [
                "null",
                {
                  "type": "record",
                  "name": "cql_decimal",
                  "namespace": "",
                  "fields": [
                    {
                      "name": "bigint",
                      "type": "bytes"
                    },
                    {
                      "name": "scale",
                      "type": "int"
                    }
                  ],
                  "logicalType": "cql_decimal"
                }
              ]
            },
            {
              "name": "order_number_of_products",
              "type": [
                "null",
                "int"
              ]
            },
            {
              "name": "order_total",
              "type": [
                "null",
                "cql_decimal"
              ]
            },
            {
              "name": "user_email_id",
              "type": [
                "null",
                "string"
              ]
            },
            {
              "name": "user_id",
              "type": [
                "null",
                "long"
              ]
            },
            {
              "name": "user_name",
              "type": [
                "null",
                "string"
              ]
            },
            {
              "name": "user_phone_number",
              "type": [
                "null",
                "string"
              ]
            },
            {
              "name": "user_platform",
              "type": [
                "null",
                "string"
              ]
            },
            {
              "name": "user_state_code",
              "type": [
                "null",
                "string"
              ]
            }
          ]
        },
        "type": "AVRO",
        "properties": {}
      }
    },
    "type": "KEY_VALUE",
    "properties": {
      "key.schema.name": "sales_orders",
      "key.schema.properties": "{}",
      "key.schema.type": "AVRO",
      "kv.encoding.type": "SEPARATED",
      "value.schema.name": "sales_orders",
      "value.schema.properties": "{}",
      "value.schema.type": "AVRO"
    }
  }
}
```

---

### schema for data topic [WITH ONLY FEW COLUMNS] :

` ~/pulsar-current/bin/pulsar-admin schemas get persistent://sales_tenant/sales_ns/data-sales.sales_orders `

```
{
  "version": 0,
  "schemaInfo": {
    "name": "data-sales.sales_orders",
    "schema": {
      "key": {
        "name": "sales_orders",
        "schema": {
          "type": "record",
          "name": "sales_orders",
          "namespace": "sales",
          "doc": "Table sales.sales_orders",
          "fields": [
            {
              "name": "order_date",
              "type": {
                "type": "int",
                "logicalType": "date"
              }
            },
            {
              "name": "order_date_hour",
              "type": "int"
            },
            {
              "name": "order_timestamp",
              "type": [
                "null",
                {
                  "type": "long",
                  "logicalType": "timestamp-millis"
                }
              ]
            },
            {
              "name": "order_code",
              "type": [
                "null",
                {
                  "type": "string",
                  "logicalType": "uuid"
                }
              ]
            }
          ]
        },
        "type": "AVRO",
        "properties": {}
      },
      "value": {
        "name": "sales_orders",
        "schema": {
          "type": "record",
          "name": "sales_orders",
          "namespace": "sales",
          "doc": "Table sales.sales_orders",
          "fields": [
            {
              "name": "order_grand_total",
              "type": [
                "null",
                {
                  "type": "record",
                  "name": "cql_decimal",
                  "namespace": "",
                  "fields": [
                    {
                      "name": "bigint",
                      "type": "bytes"
                    },
                    {
                      "name": "scale",
                      "type": "int"
                    }
                  ],
                  "logicalType": "cql_decimal"
                }
              ]
            },
            {
              "name": "user_email_id",
              "type": [
                "null",
                "string"
              ]
            },
            {
              "name": "user_state_code",
              "type": [
                "null",
                "string"
              ]
            }
          ]
        },
        "type": "AVRO",
        "properties": {}
      }
    },
    "type": "KEY_VALUE",
    "properties": {
      "key.schema.name": "sales_orders",
      "key.schema.properties": "{}",
      "key.schema.type": "AVRO",
      "kv.encoding.type": "SEPARATED",
      "value.schema.name": "sales_orders",
      "value.schema.properties": "{}",
      "value.schema.type": "AVRO"
    }
  }
}
```

