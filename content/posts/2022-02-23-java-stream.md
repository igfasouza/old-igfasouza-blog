---
layout: post
title: java Stream
date: '2022-02-23'
slug: java-stream
tags:
- Java
description: How’s the form? Introduced in Java 8, the Stream API provides a functional
  approach to processing collections of objects. A stream is a sequence of objects
  that supports various methods which can be p
image: wp/2022/02/java_streams01.png
---

![](/images/wp/2022/02/java_streams01-1024x300.png)

**How’s the form?**

Introduced in Java 8, the Stream API provides a functional approach to processing collections of objects. A stream is a sequence of objects that supports various methods which can be pipelined to produce the desired result.

I got myself thinking about a way to explain Java Stream in an easy way and I decided to do some research. This post is a collection of links, videos, tutorials, blogs, and books that I found mixed with my opinion.

We can see Java Streams as a series of connected pipes, wherein each pipe our data gets processed differently; yes, It could use my [Led Strip](/learn-kafka-and-event-streams-with-fun/) idea as well.

![](/images/wp/2022/02/data_streams.jpg)  
Picture 1: Data Stream

Simply put, streams are wrappers around a data source, allowing us to operate with that data source and making bulk processing convenient and fast.  
A Java Stream is a component that is capable of internal iteration of its elements, meaning it can iterate its elements itself. In contrast, when you are using the Java Collections iteration features (e.g a Java Iterator or the Java for-each loop used with a Java Iterable) you have to implement the iteration of the elements yourself.

The whole idea of Java streams is to enable functional-style operations on streams of elements. A stream is an abstraction of a non-mutable collection of functions applied in some order to the data.

There are a lot of benefits to using streams in Java, such as the ability to write functions at a more abstract level which can reduce code bugs, compact functions into fewer and more readable lines of code, and the ease they offer for parallelization.

## Stream provides the following features

- Stream does not store elements. It simply conveys elements from a source such as a data structure, an array, or an I/O channel, through a pipeline of computational operations.
- Streams are functional in nature. Operations performed on a stream do not modify its source. For example, filtering a Stream obtained from a collection produces a new Stream without the filtered elements, rather than removing elements from the source collection.
- Stream is lazy and evaluates code only when required.
- The elements of a stream are only visited once during the life of a stream. Like an Iterator, a new stream must be generated to revisit the same elements of the source.

One of the most important characteristics of Java streams is that they allow for significant optimizations through lazy evaluations. Computation on the source data is only performed when the terminal operation is initiated, and source elements are consumed only as needed. All intermediate operations are lazy, so they’re not executed until a result of processing is actually needed.

A stream is not a collection where you can store elements. The most important difference between a stream and a structure is that a stream doesn’t hold the data. For example, you cannot point to a location in the stream where a certain element exists. You can only specify the functions that operate on that data. And when performing operations on a stream, it will affect the original stream.

The Java Stream API is not related to the Java InputStream and Java OutputStream of Java IO. The InputStream and OutputStream are related to streams of bytes. The Java Stream API is for processing streams of objects – not bytes.

## Characteristics of a stream

- **Declarative paradigm**  
  Streams are written specifying what has to be done, but not how.
- **Lazily evaluated**  
  This basically means that until we call a terminal operation, our stream won’t be doing anything, we will just have declared what our pipeline will be doing.
- **It can be consumed only once**  
  Once we call a terminal operation, a new stream would have to be generated in order to apply the same series of aggregate operations.
- **Can be parallelised**  
  Java Streams are sequential by default, but they can be very easily parallelised.

The Stream interface has a selection of terminal and non-terminal operations. A non-terminal stream operation is an operation that adds a listener to the stream without doing anything else. A terminal stream operation is an operation that starts the internal iteration of the elements, calls all the listeners and returns a result.

The non-terminal stream operations of the Java Stream API are operations that transform or filter the elements in the stream. When you add a non-terminal operation to a stream, you get a new stream back as result. The new stream represents the stream of elements resulting from the original stream with the non-terminal operation applied.

The terminal operations of the Java Stream interface typically return a single value. Once the terminal operation is invoked on a Stream, the iteration of the Stream and any of the chained streams will get started. Once the iteration is done, the result of the terminal operation is returned. A terminal operation typically does not return a new Stream instance. Thus, once you call a terminal operation on a stream, the chaining of Stream instances from non-terminal operation ends.

**A Java Stream is composed of three main phases**

- **Split** – we usually call it stream source. Data is collected from a collection, a channel, or a generator function for example. In this step, we convert a datasource to a Stream in order to process our data.
- **Apply** – we usually call it intermediate operations.  
  Every operation in the pipeline is applied to each element in the sequence.
- **Combine** – we usually call it terminal operation.  
  Completion with a terminal operation where the stream gets materialized.

<https://docs.oracle.com/javase/8/docs/api/java/util/Spliterator.html>

<https://docs.oracle.com/javase/8/docs/api/java/util/stream/Collector.html>

Streams can be created from various data sources, especially collections. Lists and Sets support new methods stream() and parallelStream() to either create a sequential or a parallel stream.

Java Streams operations are stored internally using a LinkedList structure and in its internal storage structure, each stage gets assigned a bitmap that follows this structure:

![](/images/wp/2022/02/streams_internal.png)  
Picture 2: Java Stream internal store structure

Some of the advantages that streams have are less verbose code, more intuitive code, and less error prone code.

Java 8 brought Java streams to the world, however, the following version of the language also contributed to the feature. Java 9 added some improvements to the Streams and takeWhile, dropWhile, ofNullable are some examples.

There are two main scenarios in the execution of a Java Stream: when all stages are stateless and when NOT all stages are stateless.

- **Stateless operations**  
  A stateless operation doesn’t need to know about any other element to be able to emit a result. Examples of stateless operations are filter, map, or flatMap.
- **Stateful operations**  
  On the contrary, stateful operations need to know about all the elements before emitting a result. Examples of stateful operations are sorted, limit, or distinct.

![](/images/wp/2022/02/java_streams_api.jpg)  
Picture 3: Java Util Stream

## Books

Java 8 in Action: Lambdas, Streams, and functional-style programming

Java 8 Lambdas: Pragmatic Functional Programming

## Course

<https://www.udemy.com/course/functional-programming-with-java/>

<https://www.udemy.com/course/java-streams/>

## Conclusion

There are some other items that you need to understand to make more sense of Java Streams, like; Functional programming, Predicate, Lambda expressions, and others. Here it could be a world without end.

The introduction of functions and streams in Java has been the biggest improvement by far in Java language in the last decade. Now not only our code is more readable and easier to follow, but also less error-prone and more fluent to write. Having to write complex loops and deal with variables just to iterate collections wasn’t the most efficient way of doing things in Java. (If you disagree, please leave a comment, I really want to know what you think was the biggest improvement in Java?)

Another benefit is that Java Streams have enabled a way to do concurrent programming for anyone.

## Links

<https://docs.oracle.com/javase/8/docs/api/java/util/stream/package-summary.html>

<https://developer.ibm.com/articles/j-java-streams-1-brian-goetz/>

<https://developer.ibm.com/articles/j-java-streams-3-brian-goetz/>

<https://www.javaguides.net/p/java-8-stream-api-tutorial.html>

<https://www.logicbig.com/tutorials/core-java-tutorial/java-util-stream.html>
