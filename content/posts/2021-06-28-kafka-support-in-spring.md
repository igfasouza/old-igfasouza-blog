---
layout: post
title: Kafka Support in Spring
date: '2021-06-28'
slug: kafka-support-in-spring
tags:
- Java
- Kafka
description: How the hell are you? Spring framework has evolved to become the most
  widely used Enterprise Java development framework. I hope you already know that
  the Spring framework is structured as a bunch of i
image: wp/2021/06/kafkaSpring3.jpg
---

![](/old-igfasouza-blog/images/wp/2021/06/kafkaSpring3.jpg)

**How the hell are you?**

Spring framework has evolved to become the most widely used Enterprise Java development framework. I hope you already know that the Spring framework is structured as a bunch of independent projects. A simple search for Kafka support in the Spring documentation will show you several references. And that often causes some confusion for a beginner.

This Post will give you a high-level overview of Kafka support in Spring and try to help you understand how Kafka support is structured in the Spring framework.

Kafka offers two types of APIs, Kafka Client APIs, and Kafka Streams API, Similarly, Spring implemented Kafka in two ways. Spring for Apache Kafka and Spring Cloud Stream.

Spring started implementing Kafka support in the Spring framework under the project name “Spring for Apache Kafka.” That one became a top-level Spring project to implement all the core features of Kafka client APIs.

Spring realized the requirement for a specialized stream processing framework, and the Spring Cloud project was born under the Spring Cloud framework. This project offers you to develop and deploy distributed applications in the cloud environment.  
If you get inside the Spring cloud framework, you will see a bunch of subprojects. Spring Cloud Stream is one of the subprojects inside the Spring Cloud project.

Handling streams of data, especially “live” data whose volume is not predetermined, requires special care in an asynchronous system, and for that Spring creates the Spring WebFlux that we need to check before seeing all Kafka support.

**Table of contents**

1. Spring WebFlux  
2. Spring for Apache Kafka  
3. Spring Cloud Stream  
4. Links

## 1. Spring WebFlux

![](/old-igfasouza-blog/images/wp/2021/06/spring_webflux.jpg)  
Picture 1: Spring WebFlux logo

Spring WebFlux provides reactive, async, non-blocking programming support for web applications in an annotated Controller format similar to SpringMVC. It moves away from the thread-per-request blocking model in traditional SpringMVC and moves towards a multi-EventLoop, async, non-blocking paradigm with back-pressure that is more scalable and efficient than traditional blocking code.

![](/old-igfasouza-blog/images/wp/2021/06/spring-mvc-webflux.png)  
Picture 2: The differences between Spring MVC and Spring WebFlux

Spring WebFlux is built on [Project Reactor](https://projectreactor.io/) which implements the [Reactive Streams specification](https://www.reactive-streams.org/).

**Why Use Spring WebFlux?**

Spring WebFlux will allow you to more efficiently leverage CPU and network resources, provide a more scalable architecture and a more responsive user experience.

![](/old-igfasouza-blog/images/wp/2021/06/kafkaspring01.png)  
Picture 3: Spring Reactive Stack

## 2. Spring for Apache Kafka

The Spring for Apache Kafka (Spring-Kafka) project applies core Spring concepts to the development of Kafka-based messaging solutions. It provides a “template” as a high-level abstraction for sending messages. It also provides support for Message-driven POJOs with @KafkaListener annotations and a “listener container”. These libraries promote the use of dependency injection and declarative. In all of these cases, you will see similarities to the JMS support in the Spring Framework and RabbitMQ support in Spring AMQP.

## 3. Spring Cloud Stream

![](/old-igfasouza-blog/images/wp/2021/06/Spring_cloud_stream.jpg)  
Picture 4: Spring Cloud Stream logo

Spring describes Spring Cloud Stream as “a framework for building highly scalable event-driven microservices connected with shared messaging systems”, is a Spring subproject that allows the developer to build event-driven architecture with messaging systems like Kafka or RabbitMQ. This is an abstraction layer on top of messaging platforms like Kafka and RabbitMQ. Hence, it hides the implementation-specific details of the platform.

Spring Cloud Stream uses a concept of Binders that handles the abstraction to the specific vendor. Most if not all the interfacing can then be handled the same, regardless of the vendor chosen. Configuration via application.yml files in Spring Boot handles all the interfacing needed.

Spring Cloud Stream uses Spring Boot for configuration, and the Binder abstraction makes it possible for a Spring Cloud Stream application to be flexible in how it connects to middleware. For example, deployers can dynamically choose, at runtime, the destinations (e.g., the Kafka topics or RabbitMQ exchanges) to which channels connect. Such configuration can be provided through external configuration properties and in any form supported by Spring Boot (including application arguments, environment variables, and application.yml or application.properties files).

![](/old-igfasouza-blog/images/wp/2021/06/kafka_spring05.jpg)  
Picture 5: Brokers and Binders

At the time of publication, there were binders for Apache Kafka, Kafka Streams, Rabbit MQ, Azure Event Hubs, Google Cloud PubSub, and many others. You can see the list [here](https://cloud.spring.io/spring-cloud-static/spring-cloud-stream/current/reference/html/spring-cloud-stream.html#_binder_implementations).

One of the key concepts of Spring Cloud Stream is its functional paradigm. Consumers, Producers, and Streamers of data can be defined with Java’s functional interface. Define any number of Functions, Consumers, or Suppliers as Spring beans, and these can be configured as streamers, consumers, or producers of messages respectively. This can be done completely with configuration (no boilerplate code!). The functions can even be composed together to create complex workflows, and since it is done with the configuration, Spring Cloud allows these to be changed on the fly.

supports the reactive programming model. It uses the Reactor library which allows us to write asynchronous, non-blocking, declarative code.

**Binder**

A binder handles the integration with a single framework. This abstraction allows your code to be middleware-neutral, focusing only on core business logic. The application core only needs to interact with a canonical message.

Binders can be used on both the input and output sides to interact with producers or consumers of data. An application can use more than one binder if it has multiple message destinations.

Each binder implementation contains configuration options for setting up features specific to it, such as concurrency, partitioning, and error handling.

![](/old-igfasouza-blog/images/wp/2021/06/spring_binders.png)  
Picture 6: Producers and Consumers – from Binders documentation

<https://docs.spring.io/spring-cloud-stream/docs/Brooklyn.RELEASE/reference/html/_binders.html>

**Why Is It Important?**

The components that abstract away the communication with message brokers, referred to as “binders,” allow developers to focus on code that emits and consumes messages without having to write code for a specific broker. Because of this, that also means migrating from one message broker to another can be as simple as the dependencies of your code.

Since Spring Cloud Stream is a part of the Spring framework, you can easily test your code as well. Spring provides methods for running tests without the need to specifically connect to a message broker, which allows it to fit in nicely with your current CI process.

**How Does It Work?**

Spring Cloud Stream introduces three main components that allow developers to utilize messaging in their code:

- **Binder** – The component that implements communication with a specific message broker. For example, there is a RabbitMQ Binder, a Kafka Binder, and so on.
- **Binding** – The interface for sending and receiving messages. This component links the abstract channels in your code with a topic or queue that’s handled by the binder.
- **Message** – The data structure used to communicate with the bindings between your code and your message broker. How this data is packaged and communicated over the message broker is determined by the binder.

![](/old-igfasouza-blog/images/wp/2021/06/kafkaspring03.png)  
Picture 7: Application overview

Spring Cloud Stream allows us to create broker-agnostic event-driven microservices in a surprisingly simple manner. Since all brokers are treated the same, configuring your Stream to communicate with it is just a matter of adding a dependency and a little extra configuration, and very little knowledge if any regarding the specific broker that we decide to use.  
Spring Cloud Stream takes all the boilerplate and hard work of configuring all the event-handling and lets you focus solely on the app-logic of your event-driven microservice.

## 4. Links

<https://docs.spring.io/spring-framework/docs/current/reference/html/web-reactive.html>

<https://www.reactive-streams.org/>

<https://spring.io/projects/spring-kafka#overview>

<https://spring.io/projects/spring-cloud-stream#overview>

<https://docs.spring.io/spring-cloud-stream/docs/Brooklyn.RELEASE/reference/html/index.html>

<https://www.baeldung.com/spring-cloud-stream>

<https://ordina-jworks.github.io/spring/2017/10/04/Spring-Cloud-Stream-Rick-And-Morty-Adventure.html>
