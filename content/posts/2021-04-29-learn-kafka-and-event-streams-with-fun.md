---
layout: post
title: Learn Kafka and Event Streams with fun
date: '2021-04-29'
slug: learn-kafka-and-event-streams-with-fun
tags:
- Kafka
- Raspberry PI
description: Hey you! This is a start point for me to explore some ideas to learn
  Kafka and Event Streams in a fun way. My plan is to create a way to teach people
  Kafka concepts combining with some kind of hardware or game.
image: wp/2021/04/kafka_idea.jpg
---

![](/images/wp/2021/04/kafka_idea.jpg)

**Hey you!**

This is a start point for me to explore some ideas to learn Kafka and Event Streams in a fun way. My plan is to create a way to teach people Kafka concepts combining with some kind of hardware or game. Something like from scrap, for dummies, for kids, or from zero to one.

Is it possible to learn Kafka and Event Streams with fun?

[Stream processing](/what-is-stream-processing/) is the act of continuously incorporating new data to compute a result. Streaming is a data distribution technique where data producers write data records into an ordered data stream from which data consumers can read that data in the same order. Here is a simple data streaming diagram illustrating a data producer, a data stream, and a data consumer.

![](/images/wp/2019/10/data-streaming-introduction-1-1024x163.png)

And if you look only at the Data Stream part you will see something like a Led Strip

![](/images/wp/2021/04/led_stripe-1024x256.png)

The question is can I use a led Strip to teach Event Stream nicely and funnily?

I came with two ideas

- Led Race game – [blog](/led-race-another-dublinmaker/)
- Anki Overdrive – [blog](/connected-vehicles-self-driving-cars-with-kafka/)

![](/images/wp/2021/04/kafka_learn-1024x310.jpg)

## Led Race game

Led Race is a Raspberry PI Led Strip game. Minimalist cars race with a Led strip and two switches where the speed of the car is proportional to the pulsations of the control button. In this scenario, I can explore how to generate data and build a scoreboard and game statistics using Kafka.

![](/images/wp/2021/04/ledrace_kafka011-1024x537.png)

I can explore the same ideas from my [weather station blog](/kafka-weather-station/) and It is possible to combine them with IOT, connected vehicles, Kafka at the Edge, and several others ideas.

## Anki Overdrive

Anki Overdrive is an intelligent battle racing system that lets you explore the power of artificial intelligence (AI). It is a game where you drive the car using a smartphone or a tablet and you can race with friends.  
The Anki provides an API where you can get information in real-time from the game.  
Again I can explore how to generate data and build a scoreboard and game statistics using Kafka.

![](/images/wp/2021/04/anki_kafka01-1024x537.png)

I can explore the same ideas from my [weather station blog](/kafka-weather-station/) and It is possible to combine them with IOT, connected vehicles, Kafka at the Edge, and several others ideas.

And as you can see both ideas are similar in the sense that I can add and explore several scenarios around Data Stream.

![](/images/wp/2021/03/diagran-1024x801.jpg)

Each [producer](/real-time-locating-system-with-kafka/) could be a sensor, an IOT device, or a machine and I can use a Raspberry PI to show that. On the Kafka Cluster each broker, leader, and follower could be a Raspberry PI as well, and of Course the consumer as well.

This means that a bunch of Raspberry Pis and a Led Strip is a basic start point.  
The best part is that now with Raspberry PI 4 8g it is possible to [install Kafka](/raspberry-pi-kafka-cluster/) and show the concept of [Kafka at the edge](/kafka-at-the-edge-with-raspberry-pi/).

![](/images/wp/2021/03/kafka_at_the_edge1.jpg)

## Ideas outside

Of course, there are some ideas outside that somehow could fit in this purpose.

[Kafka Visualization](https://softwaremill.com/kafka-visualisation/)

[Building Event Streaming Applications with Pac-Man](https://www.confluent.io/resources/kafka-summit-2020/building-event-streaming-applications-with-pac-man/)

[What apache Kafka has in common with Rocky Balboa](https://riferrei.com/what-apache-kafka-has-in-common-with-rocky-balboa/)

[Learning Apache Kafka Theory 101 with My Little Ponies](https://www2.slideshare.net/AlejandraOlveraNovac/learning-kafka-theory-101-w-my-little-ponies)

[Understanding Kafka with Factorio](https://ruurtjan.medium.com/understanding-kafka-with-factorio-74e8fc9bf181)

If you know or have any similar ideas, please let me know in the comments.

Just did an idea intro presentation video.

**[learn Kafka and Event Streams with fun](https://www.slideshare.net/slideshow/learn-kafka-and-event-streams-with-fun/247341782 "learn Kafka and Event Streams with fun")**  from **[Igor De Souza](https://www.slideshare.net/IgorSouza137)**
