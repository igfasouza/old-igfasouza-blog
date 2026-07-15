---
layout: post
title: KRaft aka KIP-500 and Raspberry PI
date: '2021-04-02'
slug: kraft-aka-kip-500-and-raspberry-pi
tags:
- Kafka
description: How goes the battle? It is now possible to run Apache Kafka without Apache
  ZooKeeper! KRaft (aka KIP-500) mode Early Access Release is available to download.
  This is another blog about Kafka and Raspb
image: wp/2021/04/kafka-current-proposed-1024x445.png
---

![](/images/wp/2021/04/kafka-current-proposed-1024x445.png)

**How goes the battle?**

It is now possible to run Apache Kafka without Apache ZooKeeper! KRaft [(aka KIP-500)](https://www.confluent.io/blog/kafka-without-zookeeper-a-sneak-peek/) mode Early Access Release is available to [download](https://github.com/apache/kafka/blob/6d1d68617ecd023b787f54aafc24a4232663428d/config/kraft/README.md).

This is another blog about Kafka and Raspberry PI, where I want to show how I did a simple KRaft test.

If you’re not familiar with Kafka, I suggest you have a look at my previous post [What is Kafka](/what-is-kafka/) and I suggest you check my blog about how I created a [Raspberry PI Kafka cluster](/raspberry-pi-kafka-cluster/).

First, let’s download the new beta Kafka version.

|  |  |
| --- | --- |
| 1 | wget https://github.com/apache/kafka/archive/refs/tags/2.8.0-rc0.zip |

You can follow the GitHub readme. The first step is to generate an ID for your new cluster, using the kafka-storage tool

|  |  |
| --- | --- |
| 1 | ./bin/kafka-storage.sh random-uuid |

Format your storage directories.

|  |  |
| --- | --- |
| 1 | ./bin/kafka-storage.sh format -t  -c ./config/kraft/server.properties |

Start the Kafka server on each node.

|  |  |
| --- | --- |
| 1 | ./bin/kafka-server-start.sh ./config/kraft/server.properties |

Create a topic.

|  |  |
| --- | --- |
| 1 | ./bin/kafka-topics.sh --create --topic igor --partitions 1 --replication-factor 1 --bootstrap-server localhost:9092 |

Producer

|  |  |
| --- | --- |
| 1 | kafka-console-producer.sh --broker-list localhost:9092 --topic igor |

Consumer

|  |  |
| --- | --- |
| 1 | kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic igor --from-beginning |

Depending on each Raspberry Pi version you are using you will need to change the *bin/kafka-server-start.sh* with

|  |  |
| --- | --- |
| 1 | export KAFKA\_HEAP\_OPTS="-Xmx256M -Xms128M" |

![](/images/wp/2021/04/kafka-1024x583.jpg)  
Picture 1: Terminal Logs

And that is it. Now you are ready to play with Kafka without Apache ZooKeeper on your Raspberry PI.

I came up with the idea to use a simple REST interface application to produce and consume Kafka data.

![](/images/wp/2021/04/Screenshot-2021-04-02-at-10.44.48-1024x691.png)  
Picture 2: Kafka REST application. Created with excalidraw.com

It can be any webapp, it can use Quarkus, Micronaur, Spring or any other framework and I can run in a simple Raspberry PI zero. With that, I can integrate everything in my house with the Raspberry PI Kafka cluster.

KRaft is in Early Access and is not a production-ready product, but is perfect to test with Raspberry PI at home. No Zookeeper means less memory, less disk space and fewer steps to configure your cluster.
