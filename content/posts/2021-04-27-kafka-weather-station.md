---
layout: post
title: Kafka weather station
date: '2021-04-27'
slug: kafka-weather-station
tags:
- Kafka
- Raspberry PI
description: 'What’s the craic? In this blog, I want to set up a base use case that
  I can explore in future blogs. The weather stations are a simple idea where I can
  use a different source of data to get temperature, pressure, or humidity.'
image: wp/2021/04/raspberry_kafka.png
---

![](/images/wp/2021/04/Kafka_weatherstation.jpg)

**What’s the craic?**

In this blog, I want to set up a base use case that I can explore in future blogs. The weather stations are a simple idea where I can use a different source of data to get temperature, pressure, or humidity, send this to a Kafka topic, add an aggregator to do some Kafka Streams, like calculate average per hour and on the end, I can create several topics to play around the idea. I can add some kind of visualization and so on. It is a simple idea, but it is an idea that I can explore a lot of scenarios and I can easily expand and add more things.

I can explore not only Kafka, local, or cloud, but I can explore some frameworks, program languages, some tools for visualization, and of course I can add some hardware.

![](/images/wp/2021/04/PXL_20210408_093153928-1-scaled.jpg)  
Picture 1: Hats that I can use to generate some data

![](/images/wp/2021/04/Pi_hats_visualization.jpg)  
Picture2: Hats that I can use for visualization

I created a [GitHub](https://github.com/igfasouza/Kafka-weather-station) where I will add all links and codes for my blogs related to this idea.

![](/images/wp/2021/04/raspberry_kafka-1024x476.png)  
Picture3: Use Case

## Use Case

Submit temperature data to a Kafka topic every 5 seconds. Ideally, I’ll add more than one source, like 2 different sensors or weather APIs and so on. Possibility to explore the Producer and Kafka connect APIs.

Create an aggregator where I can explore the Stream APIs, I can use Kafka Stream or KSQL, and do some ETL.

Create different topics for different sensor data and aggregation values.

Use the Consumer Kafka APIs to read the values and create some visualization.  
It can send the data to some kind of storage, like a database, object store, or Hadoop.

I can explore this idea using Kafka at the Edge or on Cloud, and I can combine this with IOT, MQTT, and Advanced Message Queuing Protocol (AMQP).

I can combine with Spark, Storm Flink, and others Streaming tools.
