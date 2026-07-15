---
layout: post
title: Coroutines
date: '2022-02-28'
slug: coroutines
tags:
- Java
description: Hey, you! Coroutines is something old that was forgotten for many years,
  but because of the trending of data-intensive applications nowadays is gaining popularity,
  and is here to stay, which means tha
image: wp/2022/02/coroutines01.png
---

![](/old-igfasouza-blog/images/wp/2022/02/coroutines01.png)

**Hey, you!**

Coroutines is something old that was forgotten for many years, but because of the trending of data-intensive applications nowadays is gaining popularity, and is here to stay, which means that developers will need to learn what coroutines is.

Coroutine is a concept that has been around since at least 1958. Coroutines are lightweight, independent instances of code that can be launched to do certain tasks, get suspended, usually wait for asynchronous events, and be resumed to continue their jobs. Is a computer program that generalises subroutines for non-preemptive multitasking, by allowing execution to be suspended and resumed.

Coroutines can be paused and resumed like a Thread, but the most important difference is that while a Thread creates its own context, coroutines use a Thread context and can simultaneously run along with others.

## Virtual Threads

Virtual threads are lightweight threads scheduled by the Java runtime to run on plain old java threads. The threads used to run virtual threads are called carrier threads. While plain old java threads can be fairly heavyweight due to the fact that they represent OS threads, millions of virtual threads can be spawned without causing problems.

The main feature here is that a virtual thread doesn’t block its current carrier thread on blocking operations and should allow more efficient use of the CPU and additionally reduce the total number of threads, since a thread running on a core which would normally be idle while waiting for a resource, can now work on something else, by replacing a blocked virtual thread with an another which isn’t blocked.

**Let’s see how coroutines work in an example.**

![](/old-igfasouza-blog/images/wp/2022/02/coroutines011.png)  
Picture 1: create several coroutines

You can create several coroutines, lightweight threads, and use the thread context to run them.

![](/old-igfasouza-blog/images/wp/2022/02/coroutines02.png)  
Picture 2: coroutines use a Thread context

The coroutines run as normal

![](/old-igfasouza-blog/images/wp/2022/02/coroutines03.png)  
Picture 3: get suspended, usually to wait for asynchronous events

Once the coroutines get suspended or get blocked with an IO task, the coroutines is removed from the thread and another task can take its place to be processed. This makes it faster and makes better use of the CPU.

![](/old-igfasouza-blog/images/wp/2022/02/coroutines04.png)  
Picture 4: be resumed to continue their jobs

Once the suspended task is finished it could back a thread to continue the process. It could be any available thread. The picture shows task Blue which was originally processed in thread 1 comeback in thread 2.

In the last few years, coroutines have grown in popularity and are now included in many popular programming languages but there is no silver bullet and with coroutines should be the same. Be aware of when to use and when not to use. Sometimes less means more. [Why I stopped using Coroutines](https://dev.to/martinhaeusler/why-i-stopped-using-coroutines-in-kotlin-kg0).

## Coroutines with Java

Java has been threaded since the beginning, around 25 years, and is only now getting virtual threads.

![](/old-igfasouza-blog/images/wp/2022/02/loom01.jpeg)  
Picture 5: https://cr.openjdk.java.net/~rpressler/loom/Loom-Proposal.html

Currently, there is no coroutines implementation in Java and Project Loom is a proposal implementation. Is not yet clear when this should be added to Java, but there is a big expectation for Java 19.

I found an open implementation in [GitHub](https://github.com/esoco/coroutines).

Project Loom is an attempt by the OpenJDK community to introduce a lightweight concurrency construct to Java. The prototypes for Loom so far have introduced a change in the JVM as well as the Java library.

In the recent prototypes in OpenJDK, a new class named Fiber is introduced to the library alongside the Thread class. Fibers is similar to Thread, the user implementation should also remain similar. However, there are two main differences;

- Fiber would wrap any task in an internal user-mode continuation. This would allow the task to suspend and resume in Java runtime instead of the kernel
- A pluggable user-mode scheduler (ForkJoinPool, for example) would be used

A continuation (or co-routine) is a sequence of instructions that can yield and be resumed by the caller at a later stage. Every continuation has an entry point and a yield point. The yield point is where it was suspended. Whenever the caller resumes the continuation, the control returns to the last yield point.

It’s important to realize that this suspend/resume now occurs in the language runtime instead of the OS. Therefore, it prevents the expensive context switch between kernel threads.

![](/old-igfasouza-blog/images/wp/2022/02/fibers.png)  
Picture 6: Coroutines with Fibers

You can create several Fibers that will be translated in only fill threads and this will be transparent for the user. In this way, you can have better use of the CPU.

Is a tradeoff to think about, the thread per task model is easy to implement but not scalable. Reactive programming is more scalable but the implementation is a bit more involved. A simple graph representing program complexity vs. program scalability would look like this:

![](/old-igfasouza-blog/images/wp/2022/02/scalability1.png)  
Picture 7: Scalability VS complexity tradeoff

## Fun time

![](/old-igfasouza-blog/images/wp/2022/02/result.gif)  
Picture 8: Virtual Threads or Coroutines in an animated gif

## Conclusion

Coroutines is not something new, in fact, is quite an old concept.

Coroutines use a thread context and can simultaneously run along with others. You can create several coroutines that will be translated into feel threads that are transparent for the user.

There is no current official implementation of Coroutines in Java and Project Loom is a proposal implementation.

Plain old java threads will most likely still have a purpose. There is no silver bullet.

## Links

<https://en.wikipedia.org/wiki/Coroutine>

<https://en.wikipedia.org/wiki/Green_threads>

<https://www.itproportal.com/features/the-rise-of-the-coroutines/>

<https://cr.openjdk.java.net/~rpressler/loom/Loom-Proposal.html>

<https://kotlinlang.org/docs/coroutines-basics.html>

<https://www.raywenderlich.com/books/kotlin-coroutines-by-tutorials/v2.0/chapters/3-getting-started-with-coroutines>
