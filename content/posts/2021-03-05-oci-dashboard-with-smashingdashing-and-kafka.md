---
layout: post
title: OCI Dashboard with Smashing/Dashing and Kafka
date: '2021-03-05'
slug: oci-dashboard-with-smashingdashing-and-kafka
tags:
- Java
- Kafka
- Raspberry PI
- OCI
description: What’s up? 2021/03/05 This is another blog about Raspberry PI, and today
  I want to show how I did a simple Kafka cluster demo. It’s kind of a continuation
  from my two previous blogs, Kafka at the edge
image: wp/2021/03/OCI-kafka2.jpg
---

![](/old-igfasouza-blog/images/wp/2021/03/OCI-kafka2.jpg)

**What’s up?**  
2021/03/05

This is another blog about Raspberry PI, and today I want to show how I did a simple Kafka cluster demo. It’s kind of a continuation from my two previous blogs, [Kafka at the edge with Raspberry PI](/old-igfasouza-blog/kafka-at-the-edge-with-raspberry-pi/) and [Real-Time Locating System with Kafka](/old-igfasouza-blog/real-time-locating-system-with-kafka/).

If you’re not familiar with Kafka, I suggest you have a look at my previous post [What is Kafka?](/old-igfasouza-blog/what-is-kafka/) before, and you can have a look at how I created the Kafka cluster [here](/old-igfasouza-blog/raspberry-pi-kafka-cluster/).

## Idea

I found the idea of an [OCI dashboard with smashing dashing](https://www.oc-blog.com/2019/05/13/oci-dashboard-with-smashing-dashing/) in a colleague’s [blog](https://www.oc-blog.com/) some time ago and I decided to pivot a little bit in a simple Raspberry Pi Kafka example where I can get OCI data and combine it with the smashing dashing dashboard idea.

For the producer part, you can use my Micronaut Sense hat example as a start point and just change to get the OCI data. You can get the full Micronaut Kafka Producer code on my [GitHub](https://github.com/igfasouza/micronaut_sensehat).

<https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/javasdk.htm>  
<https://github.com/oracle/oci-java-sdk>

For the consumer part, you can use my Quarkus example. You can get the full Quarkusl Kafka Consumer code on my [GitHub](https://github.com/igfasouza/quarkus-kafka-consumer).

clone the [code](https://github.com/AnykeyNL/oci-smashing) and change the update.py file to read the value from the REST interface that Quarkus generates.

**Results**

![](/old-igfasouza-blog/images/wp/2021/03/OCI-kafka1.jpg)

Because this is a kind of Oracle Cloud solution you can use Oracle Streaming Service instead of hosting your Kafka.

Oracle Streaming Service (OSS) is a real-time, serverless, Apache Kafka-compatible event streaming platform for developers and data scientists, it provides a fully managed, scalable, and durable solution for ingesting and consuming high-volume data streams in real-time. To learn more about Oracle Streaming Service, see the [documentation overview](https://docs.oracle.com/en-us/iaas/Content/Streaming/Concepts/streamingoverview.htm).

You can check my [GitHub](https://github.com/igfasouza/OSS_examples) with some OSS examples and check the Micronaut one.

You just need to change the “application.yml” file from my Micronaut sense hat idea.

```
kafka:
bootstrap:
servers: streaming.{your-region}.oci.oraclecloud.com:9092
security:
protocol: SASL_SSL
sasl:
mechanism: PLAIN
key:
serializer: org.apache.kafka.common.serialization.StringSerializer
deserializer: org.apache.kafka.common.serialization.StringDeserializer
value:
serializer: org.apache.kafka.common.serialization.StringSerializer
deserializer: org.apache.kafka.common.serialization.StringDeserializer
retries: 5
max:
request:
size: 1048576
partition:
fetch:
bytes: 1048576
group:
id: group-0
```

And you can use all solutions in the cloud.

![](/old-igfasouza-blog/images/wp/2021/03/Screenshot-2021-03-03-at-15.01.06-1024x533.png)

The Kafka consumer and the dashboard can be hosted in a cloud VM as well.

OCI Logging service is a highly scalable and fully managed single pane of glass for all the logs in your tenancy. Logging provides access to logs from Oracle Cloud Infrastructure resources. These logs include critical diagnostic information that describes how resources are performing and being accessed. To learn more about the Logging service, see the [documentation overview](https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/loggingoverview.htm).

OCI Service Connector Hub moves data, such as logs from Logging, to services, such as Object Storage, Streaming, and Monitoring. It triggers functions for custom data processing and sends notifications about changes to cloud resources. To learn more about the Service Connector Hub, see the [documentation overview](https://docs.oracle.com/en-us/iaas/Content/service-connector-hub/overview.htm).

Here using Service Connector Hub I can get the logs from my tenancy and send them to OSS in a simple way.

## Links

<https://www.oc-blog.com/2019/05/13/oci-dashboard-with-smashing-dashing/>

<https://github.com/AnykeyNL/oci-smashing>
