---
layout: post
title: Real-Time Locating System with Kafka
date: '2021-03-03'
slug: real-time-locating-system-with-kafka
tags:
- Java
- Kafka
- Raspberry PI
description: How’s the craic? 2021/03/03 This is another blog about Raspberry PI,
  and today I want to show how I did a simple Kafka cluster demo using the Inky pHAT.
  It’s kind of a continuation from my previous bl
image: wp/2021/03/dublin-bus-out-of-service.jpg
---

![](/images/wp/2021/03/dublin-bus-out-of-service.jpg)

**How’s the craic?**  
2021/03/03

This is another blog about Raspberry PI, and today I want to show how I did a simple Kafka cluster demo using the Inky pHAT. It’s kind of a continuation from my previous blog, [Kafka at the edge with Raspberry PI](/kafka-at-the-edge-with-raspberry-pi/).

If you’re not familiar with Kafka, I suggest you have a look at my previous post [What is Kafka?](/what-is-kafka/) before, and you can have a look at how I created the Kafka cluster [here](/raspberry-pi-kafka-cluster/).

The Inky pHAT is an add-on board for Raspberry Pi, that has a low-energy, high-falutin, electronic paper (ePaper / eInk / EPD) display for your Pi, in three different color schemes: red/black/white, yellow/black/white, and black/white.  
You can learn more about Inky pHAT [here](https://shop.pimoroni.com/products/inky-phat?variant=12549254217811) and check the API [here](https://github.com/pimoroni/inky).

![](/images/wp/2021/03/eink.jpg)

Real-Time Locating System (RTLS) enables identifying and tracking the location of objects or people in real-time. It is used everywhere in transportation and logistics across industries.

**Use Cases**

- **Real-time alerting on a single event:** Monitor assets and people and send an alert to a controller, mobile app, or any other interface if an issue happens.
- **Continuous real-time aggregation of multiple events:** Correlation data while it is in motion. Calculate average, enforce business rules, apply an analytic model for predictions on new events, or any other business logic.
- **Batch analytics on all historical events:** Take all historical data to find insights, e.g., for analyzing issues of the past, planning future location requirements, or training analytic models.

This is not an exhaustive list.

A postmodern RTLS requires an open architecture and high scalability and of course, the implementations can rely on Kafka.

## Idea

A simple Raspberry Pi Kafka example where I can use one node to get the open Dublin Bus data and display it in real-time on the other node using Inky phat.

For the producer part, you can use my Micronaut Sense hat example as a start point and just change to use Dublin Bus data instead. You can get the full Micronaut Kafka Producer code on my [GitHub](https://github.com/igfasouza/micronaut_sensehat).

<https://data.smartdublin.ie/dataset/gtfs-r-real-time-passenger-information>  
<https://developer.nationaltransport.ie/api-details#api=gtfsr&operation=gtfsr>

For the consumer part, you can use my Quarkus example. You can get the full Quarkusl Kafka Consumer code on my [GitHub](https://github.com/igfasouza/quarkus-kafka-consumer).

**Results**

![](/images/wp/2021/03/eink3-300x211.jpg)

> Raspberry PI + fun  
> real time bus with apache kafka[@Raspberry\_Pi](https://twitter.com/Raspberry_Pi?ref_src=twsrc%5Etfw) [@apachekafka](https://twitter.com/apachekafka?ref_src=twsrc%5Etfw) [@pimoroni](https://twitter.com/pimoroni?ref_src=twsrc%5Etfw)[#pimoroni](https://twitter.com/hashtag/pimoroni?src=hash&ref_src=twsrc%5Etfw) [#apachekafka](https://twitter.com/hashtag/apachekafka?src=hash&ref_src=twsrc%5Etfw) [#raspberrypi](https://twitter.com/hashtag/raspberrypi?src=hash&ref_src=twsrc%5Etfw) [pic.twitter.com/oE8eNjBJW1](https://t.co/oE8eNjBJW1)
>
> — Igor De Souza (@Igfasouza) [August 23, 2020](https://twitter.com/Igfasouza/status/1297556313518616576?ref_src=twsrc%5Etfw)

Kafka can be deployed as a single broker in a vehicle and a global Kafka infrastructure can spread to multiple cloud providers, regions, countries, or even continents and integrate with tens or hundreds of factories or other edge locations.

![](/images/wp/2021/03/kafka_at_the_edge1.jpg)

**Curiosity**

1- Dublin bus is already using an e-ink display to show bus stop data.

![](/images/wp/2021/03/eink1-223x300.jpg)

2- I did a demo for real-time data from connected vehicles some time ago.

> Streaming demo, Lambda and Kappa architecture.
>
> Real time data from connect vehicles.
>
> Flume + OCI Streaming + Spark + NoSQL + Spring boot dashboard[#oracle](https://twitter.com/hashtag/oracle?src=hash&ref_src=twsrc%5Etfw) [#oci](https://twitter.com/hashtag/oci?src=hash&ref_src=twsrc%5Etfw) [pic.twitter.com/GTUem3CWWH](https://t.co/GTUem3CWWH)
>
> — Igor De Souza (@Igfasouza) [September 5, 2019](https://twitter.com/Igfasouza/status/1169716228610506754?ref_src=twsrc%5Etfw)

3- I won a prize at Europe’s First government-funded Blockchain Hackathon with the idea of an app to track medical devices combining Kafka and BlockChain.

> Europe's First government funded Blockchain Hackathon! [#ireland](https://twitter.com/hashtag/ireland?src=hash&ref_src=twsrc%5Etfw)  
> Team: BlockPirates[#BlockAthonIRE](https://twitter.com/hashtag/BlockAthonIRE?src=hash&ref_src=twsrc%5Etfw) [@BlockAthonIRE](https://twitter.com/BlockAthonIRE?ref_src=twsrc%5Etfw) [@juarezjunior](https://twitter.com/juarezjunior?ref_src=twsrc%5Etfw) Elaine Akemi [pic.twitter.com/zk8jBxZfXf](https://t.co/zk8jBxZfXf)
>
> — Igor De Souza (@Igfasouza) [January 26, 2019](https://twitter.com/Igfasouza/status/1089217382952910849?ref_src=twsrc%5Etfw)

## Links

<https://towardsdatascience.com/tracking-nyc-citi-bike-real-time-utilization-using-kafka-streams-1c0ea9e24e79>

<https://eng.lyft.com/a-new-real-time-map-matching-algorithm-at-lyft-da593ab7b006>

<https://github.com/ds4es/real-time-units-gps-tracking>
