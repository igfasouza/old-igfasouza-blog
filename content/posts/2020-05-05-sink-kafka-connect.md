---
layout: post
title: Sink Kafka connect
date: '2020-05-05'
slug: sink-kafka-connect
tags:
- Kafka
- Kafka Connect
description: Well? This blog post is part of my series of posts regarding Kafka Connect.
  If you’re not familiar with Kafka, I suggest you have a look at some of my previous
  post; What is Kafka? Kafka Connect Overv
image: wp/2020/05/sink_kafka_connect.jpg
---

![](/images/wp/2020/05/sink_kafka_connect.jpg)

**Well?**

This blog post is part of my series of posts regarding Kafka Connect.  
If you’re not familiar with Kafka, I suggest you have a look at some of my previous post;

[What is Kafka?](/what-is-kafka/)  
[Kafka Connect Overview](/kafka-connect-overview/)  
[Kafka Connector Architecture](/kafka-connector-architecture/)  
[Kafka Connect](/kafka-connect/)  
[Source Kafka Connect](/source-kafka-connect/)

This post is a collection of links, videos, tutorials, blogs and books that I found mixed with my opinion.

**TL;DR**

This post is about code, I’ll show all steps to develop your Sink Kafka Connector.

## Table of contents

1. Use Case  
2. Code  
3. Links

## 1. Use Case

One scenario that has become popular and I came across with some questions around in the last months is to use Kafka to trigger functions as service.

In simple words: Send a message in your kafka topic and your function(s) gets invoked with the payload which you sent to Kafka, you can now have a function trigger in response to messages in Kafka Topics.

My example is using OCI functions.

## 2. Code

![](/images/wp/2020/05/sink_class.jpg)

The connector needs extends SinkConnector. Is almost the same from source and you need to implement six methods here.

|  |  |
| --- | --- |
| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 | @Override      public [String](http://www.google.com/search?hl=en&q=allinurl%3Adocs.oracle.com+javase+docs+api+string) version() {          // TODO Auto-generated method stub          return null;      }        @Override      public void start(Map<[String](http://www.google.com/search?hl=en&q=allinurl%3Adocs.oracle.com+javase+docs+api+string), String> props) {          // TODO Auto-generated method stub                }        @Override      public Class<? extends Task> taskClass() {          // TODO Auto-generated method stub          return null;      }        @Override      public List<Map<[String](http://www.google.com/search?hl=en&q=allinurl%3Adocs.oracle.com+javase+docs+api+string), String>> taskConfigs(int maxTasks) {          // TODO Auto-generated method stub          return null;      }        @Override      public void stop() {          // TODO Auto-generated method stub                }        @Override      public ConfigDef config() {          // TODO Auto-generated method stub          return null;      } |

And the Task needs extends SinkTask Is almost the same from source but now you don’t have the poll method and instead, you have put.

|  |  |
| --- | --- |
| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 | @Override      public [String](http://www.google.com/search?hl=en&q=allinurl%3Adocs.oracle.com+javase+docs+api+string) version() {          // TODO Auto-generated method stub          return null;      }        @Override      public void start(Map<[String](http://www.google.com/search?hl=en&q=allinurl%3Adocs.oracle.com+javase+docs+api+string), String> props) {          // TODO Auto-generated method stub      }        @Override      public void put(Collection<SinkRecord> records) {          // here is where the magic happenings.          // just add a boolean triggerFn method that trigger the function.      }        @Override      public void stop() {          // TODO Auto-generated method stub                } |

**Run Docker**

|  |  |
| --- | --- |
| 1 2 3 4 5 6 7 | docker run -it --rm --name fn-oci-connect-demo -p 8083:8083 -e GROUP\_ID=1 \      -e BOOTSTRAP\_SERVERS="bootstrap\_URL" \      -e CONFIG\_STORAGE\_TOPIC=”ID-config” \      -e OFFSET\_STORAGE\_TOPIC=”ID-offset” \      -e STATUS\_STORAGE\_TOPIC=”ID-status” \      -v fn-sink-kafka-connector/target/fn-sink-kafka-connector-0.0.1-SNAPSHOT-jar-with-dependencies.jar/:/kafka/connect/fn-connector \      debezium/connect:latest |

**Configure**

|  |  |
| --- | --- |
| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 | curl -X POST \      http://localhost:8082/connectors \      -H 'content-type: application/json' \      -d '{      "name": "FnSinkConnector",      "config": {        "connector.class": "com.fn.sink.kafka.connect.FnSinkConnector",        "tasks.max": "1",        "topics": "test-sink-topic",        "tenant\_ocid": "<tenant\_ocid>",        "user\_ocid": "<user\_ocid>",        "public\_fingerprint": "<public\_fingerprint>",        "private\_key\_location": "/path/to/kafka-connect/secrets/<private\_key\_name>",        "function\_url": "<FUNCTION\_URL>"      }    }' |

I created a package “http” where I add the OCI FN part, the code is based on this one [here](https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/signingrequests.htm?TocPath=Developer%20Tools%20|REST%20APIs%20|_____4#Java).

**GitHub**  
You can check the full code in my [GitHub](https://github.com/igfasouza/oci-fn-connector-sink).

## 3. Links

<https://docs.confluent.io/current/connect/devguide.html>

<https://github.com/oracle/oci-java-sdk/blob/master/bmc-examples/src/main/java/InvokeFunctionExample.java>

<https://docs.cloud.oracle.com/en-us/iaas/Content/Functions/Concepts/functionsoverview.htm>

**Happy Coding.**
