---
layout: post
title: What is Apache Storm?
date: '2021-06-24'
slug: what-is-apache-storm
tags:
- Apache Storm
- Big Data
description: 'How’s the lad? This post is a collection of links, videos, tutorials,
  blogs, and books that I found mixed with my opinion. What is Apache Storm? From
  the Official website, Apache Storm does real-time '
image: wp/2021/06/storme_logo.png
---

![](/old-igfasouza-blog/images/wp/2021/06/Apache_Storm_logo.svg_.png)

**How’s the lad?**

This post is a collection of links, videos, tutorials, blogs, and books that I found mixed with my opinion.

## What is Apache Storm?

From the Official website, Apache Storm does real-time processing for unbounded chunks of data, similar to the pattern of Hadoop’s processing for data batches.

From Wikipedia, Apache Storm is an open-source distributed real-time computational system for processing data streams. Similar to what Hadoop does for batch processing, Apache Storm does for unbounded streams of data reliably.

From the internet, Apache Storm is a distributed real-time big data-processing system. Storm is designed to process vast amounts of data in a fault-tolerant and horizontal scalable method. It is a streaming data framework that has the capability of highest ingestion rates. Though Storm is stateless, it manages distributed environment and cluster state via Apache ZooKeeper. It is simple and you can execute all kinds of manipulations on real-time data in parallel.

Apache Storm does not have any state-managing capabilities and relies heavily on Apache ZooKeeper (a centralized service for managing the configurations in Big Data applications) to manage its cluster state – things like message acknowledgments, processing statuses, and other such messages.

Experts in the software industry consider Storm to be the Hadoop for real-time processing. While real-time processing was becoming a much talked about topic among the BI professionals and data analysts, Apache Storm evolved with all those capabilities which were needed to fasten up the traditional processes.

Storm runs topologies instead of the Apache Hadoop MapReduce. Storm topologies are composed of multiple components that are arranged in a directed acyclic graph (DAG). Data flows between the components in the graph. Each component consumes one or more data streams, and can optionally emit one or more streams.

You can check out my previous blog about [Hadoop](/old-igfasouza-blog/what-is-hadoop/) and [Big Data](/old-igfasouza-blog/what-is-big-data/).

![](/old-igfasouza-blog/images/wp/2021/06/storm01.png)  
Picture 1: Storm Topology

There are essentially two types of nodes involved in any Storm application

- Master Node (Nimbus Service)
- Worker Node (Supervisor Service)

Apache Storm guarantees that each incoming message is always fully processed, even when the data analysis is spread over hundreds of nodes.

The Nimbus node provides functionality similar to the Apache Hadoop JobTracker. Nimbus assigns tasks to other nodes in a cluster through Apache ZooKeeper. Zookeeper nodes provide coordination for a cluster and assist communication between Nimbus and the Supervisor process on the worker nodes. If one processing node goes down, the Nimbus node is informed, and it assigns the task and associated data to another node.

A Storm application has essentially four components/abstractions that are responsible for performing the tasks at hand.

![](/old-igfasouza-blog/images/wp/2021/06/storm02.png)  
Picture 2: Storm main four components/abstractions

- **Topology**: can be described as a network made of spouts and bolts. It can be compared to the Map and Reduce jobs of Hadoop. Spouts are the data stream source tasks and bolts are the accrual processing tasks. Every node in the network consists of processing logic and links to demonstrate the ways in which data will pass and the processes will be executed. Each time a topology is submitted to the Storm cluster, Nimbus consults the Supervisor nodes about the worker nodes.
- **Stream**: One of the basic abstractions of Storm architecture is a stream which is an unbounded pipeline of tuples. A tuple is a fundamental component in the Storm cluster containing a named list of values or elements.
- **Spout**: It is the entry point or the source of streams in the topology. It is responsible for getting in touch with the actual data source, receiving data continuously, transforming the data into the actual stream of tuples, and finally sending it to bolts to be processed.
- **Bolt**: Bolts keep the logic required for processing. They are responsible for consuming any number of input streams, processing them, and emitting the new streams for processing. They are capable of running functions, filtering tuples, aggregating and joining streams, linking with databases, etc.

## History

Storm was developed by Nathan Marz as a back type project which was later acquired by Twitter in the year 2011. In the year 2013, Twitter made Storm public by putting it into GitHub. Storm then entered Apache Software Foundation in the same year as an incubator project, delivering high-end applications. Written in Java and Clojure, it continues to be the standard for real-time data processing in the industry.

## What Can Apache Storm Do?

- Apache Storm can process over a million jobs on a node in a fraction of a second.
- It is integrated with Hadoop to harness higher throughputs.
- It is easy to implement and can be integrated with any programming language.

The workings of Apache Storm are quite similar to that of Hadoop. Both are distributed networks used for processing Big Data. They offer scalability and are widely used for business intelligence purposes.

- Storm does real-time stream processing, while Hadoop mostly does batch processing.
- Storm topology runs until shut down by the user. Hadoop processes are completed eventually in sequential order.
- Storm processes can access thousands of data on a cluster, within seconds. The Hadoop Distributed system uses the MapReduce framework to produce a vast amount of frameworks that will take minutes or hours.

## Books

Mastering Apache Storm by Ankit Jain

Storm Applied by Sean T. Allen, Matthew Jankowski, and Peter Pathirana

## Courses

<https://www.udemy.com/course/apache-storm-tutorial/>

<https://www.udemy.com/course/learn-by-example-apache-storm/>

## Links

<https://storm.apache.org/>

<https://www.tutorialspoint.com/apache_storm/index.htm>

<https://dzone.com/articles/apache-storm-architecture>

**Stay tuned!** Is just a question of time for me to create a post to show how to install Apache Storm in a Raspberry PI and how to consume Kafka data from Storm.
