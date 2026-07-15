---
layout: post
title: kafka at the edge with Raspberry PI
date: '2021-03-01'
slug: kafka-at-the-edge-with-raspberry-pi
tags:
- Java
- Kafka
- Raspberry PI
description: How’s the man? 2021/03/01 This is another blog about Raspberry PI, and
  today I want to show how I did a simple Kafka cluster demo using Sense Hat & GFX
  Hat. If you’re not familiar with Kafka, I sugges
image: wp/2021/03/sensehat_demo.png
---

![](/old-igfasouza-blog/images/wp/2021/03/sensehat_demo-1024x489.png)

**How’s the man?**  
2021/03/01

This is another blog about Raspberry PI, and today I want to show how I did a simple Kafka cluster demo using Sense Hat & GFX Hat.

If you’re not familiar with Kafka, I suggest you have a look at my previous post [What is Kafka?](/old-igfasouza-blog/what-is-kafka/) before, and you can have a look at how I created the Kafka cluster [here](/old-igfasouza-blog/raspberry-pi-kafka-cluster/).

The Sense HAT is an add-on board for Raspberry Pi, tha has an 8×8 RGB LED matrix, a five-button joystick and includes the following sensors: Gyroscope, Accelerometer, Magnetometer, Barometer, Temperature sensor and Relative Humidity sensor.  
You can learn more about [Sense hat](/old-igfasouza-blog/sense-hat/) in my previous blog.

The GFX HAT is an add-on board for Raspberry Pi, tha has a 128×64 pixel, 2.15″ LCD display with snazzy six-zone RGB backlight and six capacitive touch buttons. GFX HAT makes an ideal display and interface for your headless Pi projects.  
You can learn more about GFX hat [here](https://shop.pimoroni.com/products/gfx-hat) and check the API [here](https://github.com/pimoroni/gfx-hat).

![](/old-igfasouza-blog/images/wp/2021/03/hats-1024x395.jpg)

The idea here is to focus on scenarios where the Kafka clients and the Kafka brokers are running on the edge. This enables edge processing, integration, decoupling, low latency, and cost-efficient data processing.

**Edge Kafka** is not simply yet another IoT project using Kafka in a remote location. Edge Kafka is an essential component of a streaming nervous system that spans IoT (or OT in Industrial IoT) and non-IoT (traditional data-center / cloud infrastructures).

> Multi-cluster and cross-data center deployments of Apache Kafka have become the norm rather than an exception. A Kafka deployment at the edge can be an independent project. However, in most cases, Kafka at the edge is part of an overall Kafka architecture.  
> Apache Kafka is the New Black at the Edge in Industrial IoT, Logistics, and Retailing

<https://www.kai-waehner.de/blog/2020/01/01/apache-kafka-edge-computing-industrial-iot-retailing-logistics/>

## Idea

A Raspberry Pi 2 nodes Kafka cluster, with a Micronaut Kafka producer that gets sense hat data and a Quarkus Kafka consumer that puts the result in a REST that GFX Hat reads using python API.

![](/old-igfasouza-blog/images/wp/2021/03/diagran-1024x801.jpg)

The Micronaut producer gets the Sense Hat humidity, pressure, and temperature values and sends it to a Kafka topic.

The Quarkus consumer reads a Kafka topic and generates a REST interface with the last topic value. I used the GFX Hat to display the result.

You can get the full Micronaut Kafka Producer code on my [GitHub](https://github.com/igfasouza/micronaut_sensehat).  
You can get the full Quarkusl Kafka Consumer code on my [GitHub](https://github.com/igfasouza/quarkus-kafka-consumer).

**Results**

> A Raspberry 2 nodes Kafka cluster.  
> Micronaut kafka producer get sense hat data and quarkus kafka consumer put the result in a REST that GFX Hat read using python API[#raspberrypi](https://twitter.com/hashtag/raspberrypi?src=hash&ref_src=twsrc%5Etfw) [#raspberry](https://twitter.com/hashtag/raspberry?src=hash&ref_src=twsrc%5Etfw)[#sensehat](https://twitter.com/hashtag/sensehat?src=hash&ref_src=twsrc%5Etfw) [#gfxhat](https://twitter.com/hashtag/gfxhat?src=hash&ref_src=twsrc%5Etfw) [#Java](https://twitter.com/hashtag/Java?src=hash&ref_src=twsrc%5Etfw) [#python](https://twitter.com/hashtag/python?src=hash&ref_src=twsrc%5Etfw)[#micronaut](https://twitter.com/hashtag/micronaut?src=hash&ref_src=twsrc%5Etfw)[#quarkus](https://twitter.com/hashtag/quarkus?src=hash&ref_src=twsrc%5Etfw)[#apachekafka](https://twitter.com/hashtag/apachekafka?src=hash&ref_src=twsrc%5Etfw) [#kafka](https://twitter.com/hashtag/kafka?src=hash&ref_src=twsrc%5Etfw)[@Raspberry\_Pi](https://twitter.com/Raspberry_Pi?ref_src=twsrc%5Etfw) [pic.twitter.com/0zuohbaELd](https://t.co/0zuohbaELd)
>
> — Igor De Souza (@Igfasouza) [August 12, 2020](https://twitter.com/Igfasouza/status/1293514673896202240?ref_src=twsrc%5Etfw)

Kafka is a great solution for the edge. It enables deploying the same open, scalable, and reliable technology at the edge, data center, and the cloud. This is relevant across industries. Kafka is used in more and more places where nobody has seen it before. Edge sites include retail stores, restaurants, cell towers, trains, and many others.
