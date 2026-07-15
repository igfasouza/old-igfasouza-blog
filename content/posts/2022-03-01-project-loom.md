---
layout: post
title: Project Loom
date: '2022-03-01'
slug: project-loom
tags:
- Java
description: Story Horse? Currently, there is no coroutines implementation in Java,
  and Project Loom is a proposal implementation. Is not yet clear when this should
  be added to Java, but there is a big expectation
image: wp/2022/02/loom01.jpeg
---

![](/images/wp/2022/03/loom_banner1.png)

**Story Horse?**

Currently, there is no coroutines implementation in Java, and Project Loom is a proposal implementation. Is not yet clear when this should be added to Java, but there is a big expectation for Java 19.

Check out my blog about [Coroutines](/coroutines/) for a better understanding.

Project Loom is an attempt by the OpenJDK community to introduce a lightweight concurrency construct to Java. The prototypes for Loom so far have introduced a change in the JVM as well as the Java library.

In the recent prototypes in OpenJDK, a new class named Fiber is introduced to the library alongside the Thread class. Project Loom is a proposal to add Fibers and continuations as a native JVM construct. Fibers are lightweight threads, which can be created in large quantities, without worrying about exhausting system resources. Fibers are going to change how we write concurrent programs in Java.

Fibers is similar to Thread, the user implementation should also remain similar, however, there are two main differences;

- Fiber would wrap any task in an internal user-mode continuation. This would allow the task to suspend and resume in Java runtime instead of the kernel
- A pluggable user-mode scheduler (ForkJoinPool, for example) would be used

A continuation (or co-routine) is a sequence of instructions that can yield and be resumed by the caller at a later stage. Every continuation has an entry point and a yield point. The yield point is where it was suspended. Whenever the caller resumes the continuation, the control returns to the last yield point.  
It’s important to realize that this suspend/resume now occurs in the language runtime instead of the OS. Therefore, it prevents the expensive context switch between kernel threads.

![](/images/wp/2022/02/loom01.jpeg)  
Picture 1: https://cr.openjdk.java.net/~rpressler/loom/Loom-Proposal.html

Currently, Java developers are faced with a choice between writing code that’s harmonious with the design of the platform but is not scalable, or writing code that makes efficient use of existing hardware with asynchronous programming and fighting the platform. Project Loom is supposed to break that dilemma through virtual threads.

Virtual threads are cheap enough to have a single thread per task, and eliminate many of the common issues with writing concurrent code in Java. There aren’t any new APIs you have to learn, but you do need to unlearn many habits such as using thread pools to deal with resource contention.

Debugging is still challenging and the project Loom team is working with the various IDE vendors on how to present large numbers of threads.

Loom has support for a pluggable scheduler to allow developers to experiment with different scheduling algorithms; the default scheduler uses fork/join which is based on a work-stealing algorithm. In the future (post the first GA release), the team may look at adding explicit tail-call optimisation.

In OpenJDK, Java threads are just thin wrappers around OS threads and OS threads are a very precious resource; a modern OS can’t support more than a few thousand active threads at a time.

![](/images/wp/2022/02/fibers.png)  
Picture 2: Coroutines with Fibers

You can create several Fibers that will be translated in only fill threads and this will be transparent for the user. In this way, you can have better use of the CPU.

Project Loom allows us to write highly scalable code with one lightweight thread per task, this simplifies development, as you do not need to use reactive programming to write scalable code. Another benefit is that lots of legacy code can use this optimization without much change in the codebase. The improvements that Project Loom brings are exciting and allow Java programmers to write scale applications without reactive programming.

These are the two main JEP’s related to Project Loom

- JEP 425: Virtual Threads
- JEP 428: Structured Concurrency

Stay tuned, because here I can explore more about Coroutines and Project Loom with Apache Kafka and Coroutines in the Raspberry Pi world.

## Links

<https://jdk.java.net/loom/>

<https://openjdk.java.net/projects/loom/>

<https://blogs.oracle.com/javamagazine/post/going-inside-javas-project-loom-and-virtual-threads>

<https://nipafx.dev/inside-java-newscast-17/>

<https://developerlife.com/2019/12/02/project-loom-experiment/>

<https://www.javaadvent.com/2020/12/project-loom-and-structured-concurrency.html>

<https://openjdk.org/jeps/425>

<https://openjdk.org/jeps/428>
