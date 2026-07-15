---
layout: post
title: Raspberry Pi Kafka cluster
date: '2020-10-09'
slug: raspberry-pi-kafka-cluster
tags:
- Kafka
- Raspberry PI
description: How heya? This is another blog about Raspberry PI, and today I want to
  show how I did a simple Kafka cluster. If you’re not familiar with Kafka, I suggest
  you have a look at my previous post “What is Kafka?” before.
image: wp/2020/10/raspberry_kafka.jpg
---

![](/images/wp/2020/10/raspberry_kafka.jpg)

**How heya?**

This is another blog about Raspberry PI, and today I want to show how I did a simple Kafka cluster.

If you’re not familiar with Kafka, I suggest you have a look at my previous post “[What is Kafka?](/what-is-kafka/)” before.

This is a really simple tutorial and you can find similar instructions over the internet.

## Pre-Requisites

- Raspbian installed

## Components

- 3x Raspberry Pi3 B with power supply and micro SD card with Raspbian.

Despite every time that you look at a cluster tutorial they add a switch, router, and some internet cables I did use just simple wifi.

For the software part, we will download Zookeeper and Kafka, and there’s no installation. Is just about untar and changing some settings files.  
Download latest Apache Zookeeper & Apache Kafka.

## Steps

You should do this in all Raspberry PIs.

**1) Zookeeper**

|  |  |
| --- | --- |
| 1 | wget https://downloads.apache.org/zookeeper/zookeeper-3.6.1/apache-zookeeper-3.6.1-bin.tar.gz |

Modify the “*conf/zoo.cfg*” with;

|  |  |
| --- | --- |
| 1 2 3 4 5 6 7 8 9 | dataDir=/opt/zookeeper\_data  tickTime=2000  initLimit=10  syncLimit=5  dataDir=/var/zookeeper  clientPort=2181  server.1=192.168.0.18:2888:3888  server.2=192.168.0.15:2888:3888  server.3=192.168.0.16:2888:3888 |

create a file “*myid*” and the file should have only the id of the zookeeper node.  
I use 1, 2 and 3

Run this under the zookeeper’s root folder to start the Zookeeper service.

|  |  |
| --- | --- |
| 1 | ./bin/zkServer.sh start > /dev/null 2>&1 & |

**2) Kafka**

I downloaded the most recent stable version  
Modify the “*config/server.properties*” with:

|  |  |
| --- | --- |
| 1 2 3 | broker.id=1  port=9092  host.name=192.168.0.10 zookeeper.connect=192.168.0.18:2181,192.168.0.15:2181,192.168.0.16:2181 |

Boker.id should be 1,2 and 3 for each PI  
Host.name is the machine IP address  
zookeeper.connect should be equals in all

(Depends on each Raspberry PI version you are using)

Update the “*bin/kafka-server-start.sh*” with:

|  |  |
| --- | --- |
| 1 2 | export JMX\_PORT=${JMX\_PORT:-9999}  export KAFKA\_HEAP\_OPTS="-Xmx256M -Xms128M" |

Otherwise, JVM would complain not able to allocate the specified memory.

Update “*bin/kafka-run-class.sh*” with:

|  |  |
| --- | --- |
| 1 | KAFKA\_JVM\_PERFORMANCE\_OPTS="-client -XX:+UseParNewGC -XX:+UseConcMarkSweepGC -XX:+CMSClassUnloadingEnabled -XX:+CMSScavengeBeforeRemark -XX:+DisableExplicitGC -Djava.awt.headless=true" # change -server to -client |

You can run this to start Kafka

|  |  |
| --- | --- |
| 1 | /opt/kafka/bin/kafka-server-start.sh -daemon /opt/kafka/config/server.properties > /dev/null 2>&1 & |

And that’s it! Now you can do some basic tests.

Create a topic

|  |  |
| --- | --- |
| 1 | /opt/kafka/bin/kafka-topics.sh --create --zookeeper 192.168.0.15:9092,192.168.0.16:9092,192.168.0.18:9092  --replication-factor 1 --partitions 1 --topic test |

Describe this topic

|  |  |
| --- | --- |
| 1 | /opt/kafka/bin/kafka-topics.sh --zookeeper localhost:2181 --describe --topic test |

Star a terminal producer

|  |  |
| --- | --- |
| 1 | /opt/kafka/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic test |

Start a terminal consumer

|  |  |
| --- | --- |
| 1 | /opt/kafka/bin/kafka-console-consumer.sh  --bootstrap-server localhost:9092 --topic test --from-beginning |

I put my Zookeeper and Kafka in the “*/opt*” folder, but you can put it in any path.

## Final Thoughts

I did use a Raspberry PI 3 B, but Raspberry PI already released The Raspberry Pi4 with 8g.  
I don’t think we are too far from seeing a new Raspberry version, make Pi4 16gb or PI5, who knows.  
I did use the Raspbian that is 32bits OS, and Raspberry PI already released Raspberry Pi OS, (yes they changed the name), that is the new official operating system and there’s a 64bits version.

With a more powerful computer, memory, and a 64bits OS it’s open to a lot of more ideas and scenarios. Kubernetes, Strimzi, and keda are just some initial things.

Another thing is that Kafka is about to remove the Apache Zookeeper dependency, and this will make a lot of changes.

I found a lot of tutorials about Kubernetes and 64bits OS for Raspberry, but could not find any Kubernetes Kafka example or Strimzi. I think with this new OS and more powerful hardware is just a question of time.

**MicroK8s** – is a powerful, lightweight, reliable production-ready Kubernetes distribution. It is an enterprise-grade Kubernetes distribution that has a small disk and memory footprint while offering carefully selected add-ons out-the-box, such as Istio, Knative, Grafana, Cilium, and more.

Canonical has released Ubuntu 19.10 with a focus on accelerating developer productivity in AI/ML, new edge capabilities for MicroK8s, and delivering the fastest GNOME desktop performance.  
The Raspberry Pi 4 Model B is supported by Ubuntu 19.10. The latest board from the Raspberry Pi Foundation offers a faster system-on-a-chip with a processor that uses the Cortex-A72 architecture (quad-core 64-bit ARMv8 at 1.5GHz) and offers up to 8GB of RAM. With the Raspberry Pi 4 Model B, developers get access to a low-cost board, powerful enough to orchestrate workloads at the edge with MicroK8s.

[Canonical and Raspberry](https://www.hackster.io/news/canonical-walks-through-the-how-and-more-importantly-the-why-of-a-microk8s-raspberry-pi-cluster-0a9b88806c05)

[Raspberry with Ubuntu 20.04](https://ubuntu.com/blog/ubuntu-20-04-lts-is-certified-for-the-raspberry-pi)

**K3s** – a flavor of Kubernetes that is highly optimized for the edge. Though K3s is a simplified, miniature version of Kubernetes, it doesn’t compromise the API conformance and functionality.

## Links

[Kafka](https://kafka.apache.org/)  
[confluent](https://www.confluent.io/)  
[Raspberry PI](https://www.raspberrypi.org/)  
[8gb Raspberry PI4](https://www.raspberrypi.org/blog/8gb-raspberry-pi-4-on-sale-now-at-75/)  
[Raspberry Pi OS](https://www.raspberrypi.org/downloads/)  
[Strimzi](https://strimzi.io/)  
[kubernetes](https://kubernetes.io/)  
[Keda](https://keda.sh/)  
[K3s](https://k3s.io/)  
[Microk8s](https://microk8s.io/)

**Some similar tutorial;**

<https://towardsdatascience.com/kafka-and-zookeeper-over-ubuntu-in-a-3-node-cluster-a-data-science-big-data-laboratory-part-4-of-4-47631730d240>

<http://czcodezone.blogspot.com/2014/11/setup-kafka-in-cluster.html>

<https://pandariel.com/posts/kafka-cluster/>

<https://rdiot.tistory.com/329>
