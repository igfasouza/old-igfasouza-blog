---
layout: post
title: Kafka Connect
date: '2020-04-21'
slug: kafka-connect
tags:
- Kafka
- Kafka Connect
description: How are you? This blog post is part of my series of posts regarding Kafka
  Connect. If you’re not familiar with Kafka, I suggest you have a look at some of
  my previous post; What is Kafka? Kafka Connec
image: wp/2020/04/Screenshot-78.png
---

![](/old-igfasouza-blog/images/wp/2020/04/Screenshot-78.png)

**How are you?**

This blog post is part of my series of posts regarding Kafka Connect.  
If you’re not familiar with Kafka, I suggest you have a look at some of my previous post;

[What is Kafka?](/old-igfasouza-blog/what-is-kafka/)  
[Kafka Connect Overview](/old-igfasouza-blog/kafka-connect-overview/)  
[Kafka Connector Architecture](/old-igfasouza-blog/kafka-connector-architecture/)

This post is a collection of links, videos, tutorials, blogs and books that I found mixed with my opinion.

## Table of contents

1. Source Standalone mode  
2. Source Distributed mode  
3. Sink  
4. Don’t use Docker composer  
5. Lensesio  
6. Strimzi  
7. Debezium  
8. JDBC  
9. Link

## 1. Source Standalone mode

Standalone mode is the best way to get started with minimum config and infrastructure setup. In this section, we will see how to configure a connector in Standalone mode and transfer file content to Kafka topic.

Here I’m going to show how to use the [FileSource Connector](https://docs.confluent.io/current/connect/filestream_connector.html)

Let’s create a Docker compose file. “docker-compose.yml”

```
zookeeper:
    image: zookeeper:3.4.9
    restart: unless-stopped
    hostname: zookeeper
    container_name: zookeeper
    ports:
      - "2181:2181"
    environment:
        ZOO_MY_ID: 1
        ZOO_PORT: 2181
        ZOO_SERVERS: server.1=zookeeper:2888:3888
  kafka:
    image: confluentinc/cp-kafka:5.1.0
    hostname: kafka
    container_name: kafka
    ports:
      - "9092:9092"
    environment:
      KAFKA_LISTENER_SECURITY_PROTOCOL_MAP: PLAINTEXT:PLAINTEXT,PLAINTEXT_HOST:PLAINTEXT
      KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://kafka:9092,PLAINTEXT_HOST://localhost:29092
      KAFKA_ZOOKEEPER_CONNECT: "zookeeper:2181"
      KAFKA_BROKER_ID: 1
      KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1
    depends_on:
      - zookeeper
  kafka-connect:
    image: confluentinc/cp-kafka-connect:5.1.0
    hostname: kafka-connect
    container_name: kafka-connect
    ports:
      - "8083:8083"
    environment:
      CONNECT_BOOTSTRAP_SERVERS: "kafka:9092"
      CONNECT_REST_ADVERTISED_HOST_NAME: connect
      CONNECT_REST_PORT: 8083
      CONNECT_GROUP_ID: compose-connect-group
      CONNECT_CONFIG_STORAGE_TOPIC: docker-connect-configs
      CONNECT_OFFSET_STORAGE_TOPIC: docker-connect-offsets
      CONNECT_STATUS_STORAGE_TOPIC: docker-connect-status
      CONNECT_KEY_CONVERTER: org.apache.kafka.connect.json.JsonConverter
      CONNECT_VALUE_CONVERTER: org.apache.kafka.connect.json.JsonConverter
      CONNECT_INTERNAL_KEY_CONVERTER: "org.apache.kafka.connect.json.JsonConverter"
      CONNECT_INTERNAL_VALUE_CONVERTER: "org.apache.kafka.connect.json.JsonConverter"
      CONNECT_CONFIG_STORAGE_REPLICATION_FACTOR: "1"
      CONNECT_OFFSET_STORAGE_REPLICATION_FACTOR: "1"
      CONNECT_STATUS_STORAGE_REPLICATION_FACTOR: "1"
      CONNECT_PLUGIN_PATH: '/usr/share/java,/etc/kafka-connect/jars'
      CONNECT_CONFLUENT_TOPIC_REPLICATION_FACTOR: 1
    depends_on:
      - zookeeper
      - kafka
```

In the same directory where we have created the yaml file execute the following command to start Kafka cluster. When the below command runs for the very first time it downloads the image. Once the image is downloaded it creates a Kafka cluster.

```bash
docker-compose up
```

For starting any Kafka connect cluster we require – workers config and connector (file-stream) config.  
Create two files: workers-config.properties and file-stream-connector-properties.

**Workers-config.properties:**

```
bootstrap.servers=127.0.0.1:9092
key.converter=org.apache.kafka.connect.json.JsonConverter
key.converter.schemas.enable=false
value.converter=org.apache.kafka.connect.json.JsonConverter
value.converter.schemas.enable=false
# we always leave the internal key to JsonConverter
internal.key.converter=org.apache.kafka.connect.json.JsonConverter
internal.key.converter.schemas.enable=false
internal.value.converter=org.apache.kafka.connect.json.JsonConverter
internal.value.converter.schemas.enable=false
# Rest API
rest.port=8086
rest.host.name=127.0.0.1
# this config is only for standalone workers
offset.storage.file.filename=standalone.offsets
offset.flush.interval.ms=10000
```

**File-stream-connector-properties:**

```
# These are standard kafka connect parameters, need for ALL connectors
name=file-stream-kafka-connect-standalone
connector.class=org.apache.kafka.connect.file.FileStreamSourceConnector
tasks.max=1
file/FileStreamSourceConnector.java
file=source-input.txt
topic=kafka-connect-standalone
```

You should see three files in the folder; docker-compose.yml, file-stream-connector-properties and workers-config.properties

Create an input file source-input.txt, the content of the file is transferred to Kafka topic.

```
touch source-input.txt
```

Mount a host directory in a docker container: Make sure we are in the directory where we have created the files. After mount, we automatically switch to cp-kafka-connect.

```bash
docker run --rm -it -v "$(pwd)":/kafka-connect/ --net=host confluentinc/cp-kafka-connect
```

This docker image expect the connector in this folder;  
/etc/kafka-connect/jars

Create Kafka topic “kafka-connect-standalone” with 3 partitions and replication factor 1.

```bash
kafka-topics --create --topic kafka-connect-standalone --partitions 3 --replication-factor 1 --zookeeper 127.0.0.1:2181
```

Create standalone connector using workers-config.properties and file-stream-connector-properties.

```
connect-standalone workers-config.properties file-stream-connector-properties
```

Now you can test: Open file source-input.txt and type some message to it & save it. The message should have been transferred to Kafka topic.

What happened in the background: We wrote data to the source file and Kafka connect standalone pushed the data to topic. No programming, just configs.

Now stop Kafka Connect (press Ctrl/Command + C). Once Kafka connect gracefully stopped, list all files in the given directory. We have a new guest in the form of a file “standalone.offsets”.  
This file is created by Kafka connect to keep track of from where it should resume reading messages from the source file on re-starts.  
When Kafka connect starts again it should resume reading without publishing duplicate messages to the topic.

Try to execute the above command (connect-standalone workers-config.properties file-stream-connector-properties) again and validate if you do not have a duplicate message.

## 2. Source Distributed mode

Now let’s configure a connector in distributed mode.

Create Kafka topic “kafka-connect-distibuted” with 3 partitions and replication factor 1.

```bash
kafka-topics --create --topic kafka-connect-distributed --partitions 3 --replication-factor 1 --zookeeper 127.0.0.1:2181
```

Create a config file “connect-source.json”.

```
name=file-stream-kafka-connect-distributed
connector.class=org.apache.kafka.connect.file.FileStreamSourceConnector
tasks.max=1
file=source-input.txt
topic=kafka-connect-distributed
key.converter=org.apache.kafka.connect.json.JsonConverter
key.converter.schemas.enable=true
value.converter=org.apache.kafka.connect.json.JsonConverter
value.converter.schemas.enable=true
```

and run;

```bash
curl -d @<path-to-config-file>/connect-source.json -H "Content-Type: application/json" -X POST http://localhost:8083/connectors
```

Now write some message in the source file and once the file is saved, all messages are posted in topic “kafka-connect-distributed”.

check for the message copied from file to topic by FileSourceConnector. Note that messages are stored in JSON format as the connector topic created earlier with config value.converter.schemas.enable=true.

We can run the command to check the topic;

```bash
kafka-console-consumer --topic kafka-connect-distributed --from-beginning --bootstrap-server 127.0.0.1:9092
```

## 3. Sink

Now we need a sink example; Let’s look at a JDBC one. MondoBD.  
We can add this to the docker composer file.

```
mongo-db:
    image: mongo:4.0.5
    hostname: mongo-db
    container_name: mongo-db
    expose:
      - "27017"
    ports:
      - "27017:27017"
    command: --bind_ip_all --smallfiles
    volumes:
      - ./mongo-db:/data
  mongoclient:
    image: mongoclient/mongoclient:2.2.0
    container_name: mongoclient
    hostname: mongoclient
    depends_on:
      - mongo-db
    ports:
      - 3000:3000
    environment:
      MONGO_URL: "mongodb://mongo-db:27017"
      PORT: 3000
    expose:
      - "3000"
```

and run;

```bash
curl -d @<path-to-config file>/connect-mongodb-sink.json -H "Content-Type: application/json" -X POST http://localhost:8083/connectors
```

Create a connect-mongodb-sink.json

```
{
    "name": "mongodb-sink",
    "config": {
        "connector.class": "at.grahsl.kafka.connect.mongodb.MongoDbSinkConnector",
        "tasks.max": 1,
        "topics": "connect-custom",
        "mongodb.connection.uri": "mongodb://mongo-db/test?retryWrites=true",
        "mongodb.collection": "MyCollection",
        "key.converter": "org.apache.kafka.connect.json.JsonConverter",
        "key.converter.schemas.enable": false,
        "value.converter": "org.apache.kafka.connect.json.JsonConverter",
        "value.converter.schemas.enable": false
    }
}
```

We have the following MongoDB-specific properties here:

- mongodb.connection.uri contains the connection string for our MongoDB instance
- mongodb.collection defines the collection

Since the MongoDB connector is expecting JSON, we have to set JsonConverter for key.converter and value.converter
- And we also need schemaless JSON for MongoDB, so we have to set key.converter.schemas.enable and value.converter.schemas.enable to false

**Elasticsearch**

```
elasticsearch:
    image: itzg/elasticsearch:2.4.3
    environment:
      PLUGINS: appbaseio/dejavu
      OPTS: -Dindex.number_of_shards=1 -Dindex.number_of_replicas=0
    ports:
      - "9200:9200"
```

Create a config file “connect-elasticsearch-sink.json”.

```
name=sink-elastic-twitter-distributed
connector.class=io.confluent.connect.elasticsearch.ElasticsearchSinkConnector
tasks.max=2
topics=kafka-connect-distributed-twitter
key.converter=org.apache.kafka.connect.json.JsonConverter
key.converter.schemas.enable=true
value.converter=org.apache.kafka.connect.json.JsonConverter
value.converter.schemas.enable=true
connection.url=http://elasticsearch:9200
type.name=kafka-connect
key.ignore=true
```

[Here](https://docs.confluent.io/5.0.0/installation/docker/docs/installation/connect-avro-jdbc.html) is a nice link to check about Docker options and images.

I found this with a nice and simple docker composer for single or multiple  
nodes [here](https://github.com/simplesteph/kafka-stack-docker-compose).

## 4. Don’t use Docker composer

```
#Start Zookeeper
docker run -it --rm --name zookeeper -p 2181:2181 -p 2888:2888 -p 3888:3888 zookeeper:3.5.5
#Start Kafka Broker
docker run -it --rm --name kafka -p 9092:9092 --link zookeeper:zookeeper debezium/kafka:1.0
#Start Kafka Connect
docker run -it --rm --name connect -p 8083:8083 \
-e GROUP_ID=1 \
-e CONFIG_STORAGE_TOPIC=kafka_connect_configs \
-e OFFSET_STORAGE_TOPIC=kafka_connect_offsets \
-e STATUS_STORAGE_TOPIC=kafka_connect_statuses \
--link zookeeper:zookeeper \
--link kafka:kafka \
debezium/connect:1.0
```

## 5. Lensesio

Another option is to use the lenses.io image that already contains several kafka connectors pre installed and a nice user interface.

```
services:
  # this is our kafka cluster.
  kafka-cluster:
    image: landoop/fast-data-dev:cp3.3.0
    environment:
      ADV_HOST: 127.0.0.1         # Change to 192.168.99.100 if using Docker Toolbox
      RUNTESTS: 0                 # Disable Running tests so the cluster starts faster
    ports:
      - 2181:2181                 # Zookeeper
      - 3030:3030                 # Landoop UI
      - 8081-8083:8081-8083       # REST Proxy, Schema Registry, Kafka Connect ports
      - 9581-9585:9581-9585       # JMX Ports
      - 9092:9092                 # Kafka Broker
```

<https://lenses.io/>  
<https://github.com/lensesio/fast-data-dev>

## 6. Strimzi

![](/old-igfasouza-blog/images/wp/2020/04/0-9gFlyQBLppFWo-Q4.png)

Strimzi simplifies the process of running Apache Kafka in a Kubernetes cluster. It provides container images and Operators for running Kafka on Kubernetes.

<https://strimzi.io/>

<https://medium.com/@sincysebastian/setup-kafka-with-debezium-using-strimzi-in-kubernetes-efd494642585>

<https://medium.com/@vamsiramakrishnan/strimzi-on-oracle-kubernetes-engine-oke-kafka-connect-on-oracle-streaming-service-oss-a-c73cc9714e90>

<https://itnext.io/kafka-connect-on-kubernetes-the-easy-way-b5b617b7d5e9>

## 7. Debezium

![](/old-igfasouza-blog/images/wp/2020/04/debezium.png)

Debezium before, it is an open source project for applying the Change Data Capture (CDC) pattern to your applications using Kafka.

<https://debezium.io/>

```yaml
version: '2'
services:
  zookeeper:
    image: debezium/zookeeper:${DEBEZIUM_VERSION}
    ports:
     - 2181:2181
     - 2888:2888
     - 3888:3888
  kafka:
    image: debezium/kafka:${DEBEZIUM_VERSION}
    ports:
     - 9092:9092
    links:
     - zookeeper
    environment:
     - ZOOKEEPER_CONNECT=zookeeper:2181
  mysql:
    image: debezium/example-mysql:${DEBEZIUM_VERSION}
    ports:
     - 3306:3306
    environment:
     - MYSQL_ROOT_PASSWORD=debezium
     - MYSQL_USER=mysqluser
     - MYSQL_PASSWORD=mysqlpw
  postgres:
    image: debezium/postgres:9.6
    ports:
     - "5432:5432"
    environment:
     - POSTGRES_USER=postgresuser
     - POSTGRES_PASSWORD=postgrespw
     - POSTGRES_DB=inventory
  elastic:
    image: docker.elastic.co/elasticsearch/elasticsearch:5.5.2
    ports:
     - "9200:9200"
    environment:
     - http.host=0.0.0.0
     - transport.host=127.0.0.1
     - xpack.security.enabled=false
  connect:
    image: debezium/connect-jdbc-es:${DEBEZIUM_VERSION}
    build:
      context: debezium-jdbc-es
    ports:
     - 8083:8083
     - 5005:5005
    links:
     - kafka
     - mysql
     - postgres
     - elastic
    environment:
     - BOOTSTRAP_SERVERS=kafka:9092
     - GROUP_ID=1
     - CONFIG_STORAGE_TOPIC=my_connect_configs
     - OFFSET_STORAGE_TOPIC=my_connect_offsets
     - STATUS_STORAGE_TOPIC=my_source_connect_statuses
```

And of course, you can use Strimzi and Debezium together [here](https://strimzi.io/blog/2020/01/27/deploying-debezium-with-kafkaconnector-resource/).

## 8. JDBC

One of the most common integrations that people want to do with Kafka is getting data in or from a database.

<https://www.confluent.io/blog/kafka-connect-deep-dive-jdbc-source-connector/>

<https://dev.to/rmoff/streaming-data-from-kafka-to-s3-video-walkthrough-2elh>

## 9. Link

<https://docs.confluent.io/current/connect/kafka-connect-jdbc/index.html>

<https://docs.confluent.io/3.1.2/cp-docker-images/docs/quickstart.html>

<https://github.com/confluentinc/cp-docker-images/tree/5.3.1-post/examples>

<https://www.baeldung.com/kafka-connectors-guide>

<https://blog.softwaremill.com/do-not-reinvent-the-wheel-use-kafka-connect-4bcabb143292>

<https://www.confluent.io/blog/webify-event-streams-using-kafka-connect-http-sink/>

**Stay tuned!** Next blog post I’ll show how to code your own Kafka connector.
