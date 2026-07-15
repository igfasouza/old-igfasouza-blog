---
layout: post
title: Reactive Streams and Reactive programming
date: '2022-02-24'
slug: reactive-streams-and-reactive-programming
tags:
- Java
description: 'How’s the craic? Reactive Programming is trending nowadays and there
  is a lot of noise about it at the moment, not all of which is very easy to understand.
  Reactive Programming or Functional Reactive '
image: wp/2022/02/reactive_prog.jpg
---

![](/images/wp/2022/02/reactive_prog.jpg)

**How’s the craic?**

Reactive Programming is trending nowadays and there is a lot of noise about it at the moment, not all of which is very easy to understand. Reactive Programming or Functional Reactive Programming and Reactive Streams are again another topics that you can find several explanations for and sometimes could be a real trick to understand. I decided to do some research and this post is a collection of links, videos, tutorials, blogs, and books that I found mixed with my opinion.

The first thing to understand is that [Java Streams](https://docs.oracle.com/javase/8/docs/api/java/util/stream/package-summary.html) came from Java 8 and [Reactive Streams](https://docs.oracle.com/javase/9/docs/api/java/util/concurrent/Flow.html) came from Java 9 and they are completely different things.

Second, Reactive Programming is not the same thing as React, the JavaScript framework. Some people think Reactive is nothing new, and it’s what they do all day anyway, using JavaScript, and others seem to think that it’s a gift from Microsoft, who made a big splash about it when they released some C# extensions a while ago.

In a few words, Reactive Programming is a programming paradigm that deals with asynchronous data streams, sequences of events, and the specific propagation of change, which means it implements modifications to the execution environment, context, in a certain order.

[The Reactive Manifesto](https://www.reactivemanifesto.org/) of 2014 introduced reactive systems and their four principles.

![](/images/wp/2022/02/reactive-manifesto.png)  
Picture 1: https://dzone.com/articles/product-owner-and-reactive-microservices

**From Google I found;**

- Reactive programming is a declarative programming paradigm concerned with asynchronous data streams and the propagation of change.
- Reactive programming is programming with asynchronous data streams.
- The basic idea behind reactive programming is that there are certain datatypes that represent a value “overtime”. Computations that involve these changing-over-time values will themselves have values that change over time.
- Reactive Programming is a style of micro-architecture involving intelligent routing and consumption of events, all combining to change behaviour.
- Reactive programming is a programming model that deals with asynchronous data streams and the specific propagation of change.

Most of the Reactive Programming libraries I looked at use a model centred around “observables”. An observable is a type on which you can register “observers”, as defined in the observer pattern in the GoF book.

![](/images/wp/2022/02/observer_patter.png)  
Picture 2: https://en.wikipedia.org/wiki/Observer\_pattern

Objects can subscribe to a subject and get informed, whenever there is an update in the subject. Essentially, the subject maintains a list of its observers and automatically notifies them when any state is changed.

Now let’s divide Reactive programming into 3 main concepts to make it easier to understand; Asynchronous, Streams, and Propagation of change.

**Asynchronous**; When you execute something asynchronously, you can move on to another task before it finishes. With the reactive approach, a database call does not block the calling thread and instead returns immediately. The program is structured as an asynchronous stream of events. Simply put, you instantly move to the next task after having initiated some background effort to deal with the previous task.

**Streams or Data Streams**; Streams are the backbones of reactive programming, so it is necessary for you to understand what is data stream actually means. Yes, I could use my [Led Strip](/learn-kafka-and-event-streams-with-fun/) idea to understand this.

![](/images/wp/2022/02/data_streams.jpg)  
Picture 3: datastreams

The data stream is more of a pipeline of methods applied to the data as it passes through. In Reactive Programming, every sequence of values, data stream, is termed as observable.

**Propagation of change**; the streamed data has to be propagated to a consumer. Here ‘change’ refers to the transformation of data that passed through the stream. This changed or transformed data is consumed by observers who subscribed for this change.

Starting from the creation of a data stream to the end where observers receive their response, there is a wide set of ‘‘changes’’ that can be used in reactive programming.  
Reactive Programming = Observable + change + Propagation to observers

![](/images/wp/2022/02/reactive_streams01-1024x522.png)  
Picture 4: Publisher-Subscriber Communication

**The reactive approach involves 4 interfaces;**

- **Publisher**: It is the data emitter and is also referred to as the Observable.
- **Subscriber**: It subscribes to the observable to consume data and can identify all the emitted events including errors! If the subscriber is slow, it can be easily outperformed by the producer.
- **Subscription**: It’s a session between emitter and subscriber that can be cancelled when no more data is needed.
- **Processors**: These consume data from the publisher, apply some operation, eg. map, filter, etc and produce it to the subscriber. Hence, they can be thought of as a combination of the two, publisher and subscriber.

## Reactive in Java

There are a number of implementations of reactive programming in Java.

- [Reactive Streams API](https://www.reactive-streams.org/) — Introduced in Java 9, it’s an initiative to provide a standard for asynchronous stream processing with non-blocking backpressure
- [RxJava](https://github.com/ReactiveX/RxJava) — library for composing asynchronous and event-based programs by using observable sequences.
- [Project Reactor](https://projectreactor.io/) — reactive library, based on the Reactive Streams  
  specification, for building non-blocking applications on the JVM.

With the exponential increase in data being handled and an increasing number of concurrent users, Reactive Programming is more and more trending. The promise of Reactive Programming is that you can do more with less, specifically you can process higher loads with fewer threads, but there is no silver bullet, do not try to apply to Reactive Programming where there is no need to, e.g. where there is no live data, high load, or a large number of users who change data simultaneously. For the wrong problem, the effects might go into reverse; you actually make things worse.

Reactive Programming will bring some benefits;

- Increased performance; due to the possibility to handle huge volumes of data in a quick and stable way.
- Improved UX; due to the possibility to keep the application more responsive to its user.
- Simplified modifications and updates; due to more readable and easier to predict code.

## Real-life example

![](/images/wp/2022/02/AliceBob.jpg)  
Picture 5: Real life example

This is what the reactive approach is about. You wait till all async actions (changes) are completed and then proceed with further actions.

## Books

Reactive Systems in Java: Resilient, Event-Driven Architecture with Quarkus

Reactive Programming with RxJava

## Conclusion

Reactive Programming is a buzzword but still not clearly defined and there are a lot of things around. To make it easier to understand one idea is to divide into 3 main concepts; Asynchronous, Streams, and Propagation of change, plus the observer pattern from the GoF book.

The Reactive Manifesto introduced reactive systems and their four principles.

While the Streams API introduced in Java 8 is perfect to process data streams, map, reduce and all the variants, the Flow API introduced in Java 9 shines on the communication side request, slow down, drop, block, etc.

Do not try to apply Reactive Programming where there is no need to.

## Links

<https://www.reactivemanifesto.org/>

<https://www.reactive-streams.org/>

<https://github.com/ReactiveX/RxJava>

<https://projectreactor.io/>

<https://github.com/politrons/reactive>

<https://gist.github.com/staltz/868e7e9bc2a7b8c1f754>

<https://docs.spring.io/spring-framework/docs/current/reference/html/web-reactive.html>

<https://journal.stuffwithstuff.com/2015/02/01/what-color-is-your-function/>
