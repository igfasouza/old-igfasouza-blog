---
layout: post
title: Raspberry PI with Java
date: '2021-08-05'
slug: raspberry-pi-with-java
tags:
- Java
- Python
- Raspberry PI
description: How heya? This is another blog about Java on Raspberry Pi where I try
  to show that Raspberry PI is a good place to start programming with Java and you
  can use all Java ecosystem and programs to play a
image: wp/2021/08/PiJava01.jpg
---

![](/images/wp/2021/08/PiJava01.jpg)

**How heya?**

This is another blog about Java on Raspberry Pi where I try to show that Raspberry PI is a good place to start programming with Java and you can use all Java ecosystem and programs to play around and learn.

**Note**: I’m not trying to sell the idea that Java is better than other languages and I’ll not try to say anything about why Java.

The Raspberry Pi is a credit card-sized computer that has taken the technical world by storm. Originally developed to encourage children and schools to get into programming – the cheap device has been picked up by the development and hacking industries and has been the central device in projects no one would have dreamed of while it was being developed.

[What is a Raspberry PI](https://www.raspberrypi.org/help/what-%20is-a-raspberry-pi/)

The goal of the Raspberry Pi project was to build an inexpensive PC that is affordable for all, and different versions are available, depending on your budget.

At nine years old, the Raspberry Pi has become the third most popular computer of all time, recently crossing the threshold of 30 million units sold. The latest model (Raspberry Pi 4) is essentially a desktop computer, with a 1.5GHz ARM CPU, up to 4GB RAM, USB 3.0, and full Gigabit Ethernet.

![](/images/wp/2021/08/HistoryPi.png)  
Picture 1: Raspberry PI history

With the small footprint and electricity usage of the Pi, it is a perfect solution for an always-on device – meaning you can turn it on, set it up and leave it running somewhere without worrying too much about your electricity bill at the end of the month. One thing to be careful of is the processing power of the Pi itself – don’t expect it to be able to do any really heavy grunt work without grinding to a halt – however, it is fairly happy with most personal projects.

There are different operating systems available for the Raspberry Pi, Raspberry Pi OS (previously called Raspbian) is the official supported operating system.  
But it is not limited to Raspberry Pi OS, there are dozens of operating systems available on Raspberry Pi, including 64 bits options, and there is not a perfect distribution. Each distribution has its strengths and weaknesses and is more suited to a specific use.  
PI OS and Ubuntu are probably the most popular ones.

You can find not only Linux but Windows and Android OS as well. I wrote a blog with an intro to [Android Things](/rainbow-hat-and-java/), a Google IOT Android OS.

When you look at the Raspberry Pi board, you’ll find 40 pins (2 rows of 20). Those are the GPIOs (General-purpose input/output). Some of those can be used as a digital input or output pin. And the number of things you can do with it is amazing!

[Physical computing Raspberry PI](https://www.futurelearn.com/info/courses/physical-computing-raspberry-pi-python/0/steps/23033)

These GPIOs pins are even one of the main factors which made the Raspberry Pi such a success! You can indeed find a cheap second-hand laptop that includes a battery, screen, etc. but you’ll never be able to build experiments that combine soft- and hardware in such an easy way as you can do with the Raspberry Pi.

![](/images/wp/2021/08/pi4j.jpg)  
Picture 2: PI4J logo

PI4J is the most popular API to control the GPIOs using Java.

A small computer used for a variety of projects, the Raspberry Pi has long been a favorite of techies, engineers, and those that like to tinker, due to its low cost, flexibility, and simplicity. However, more recently, this incredibly cool little computer has been heralded as a great boon to education; with digital leaders using it to foster learning and collaboration in the classroom.

[Collaborative learning](https://resourced.prometheanworld.com/collaborative-learning-raspberry-pi/)

You want to use your Pi to improve your coding skills, you can use one of the supported programming languages (such as Java) to create programs. That could be anything from simply printing Hello World on screen, up to more complex projects, like making games.  
If you are interested in hardware and electronics, you can enhance this programming by using the GPIO to add switches, sensors, and real-world physical inputs to talk to this code. You can also add physical outputs like LEDs, speakers, and motors to do things when your code tells them to. Put these together, and you can make something like a robot in no time. Moving away from programming, there are a large number of users that buy a Pi as an alternative to other devices. Using a Pi as a KODI media center is a popular project, for example, taking the place of more expensive off-the-shelf alternatives.  
The masses of resources and community support are almost a guarantee that you won’t get stuck. If you can use Google, you can use a Raspberry Pi.

In the Java world, the projects and APIs that you can use are up to infinite.  
A list of the most popular ones.

![](/images/wp/2021/08/pijavaprojects01.jpg)  
Picture 3: Java Projects

And of course, you can install GraalVm and any other JVM languages as any OpenJDK distribution..

A list to check out.

- AdoptOpenJDK
- Corretto
- Dragonwell
- GraalVM
- JetBrains
- Liberica
- Mandrel
- Microsoft
- OJDK Build
- OpenLogic
- Oracle
- Oracle OpenJDK
- RedHat
- SAP Machine
- Trava
- Zulu
- Zulu Prime

Another project to check out is [JDKMon](https://github.com/HanSolo/JDKMon).

![](/images/wp/2021/08/graalvm.png)  
Picture 4: Graal VM logo

You can play with Java and Web as well, and you will find a lot of resources for Spring, Micronaut, Quarkus, Vert.x, Helidon, and others.

You can find a lot of tutorials and info about Raspberry Pi and [Kubernetes](https://enterprisersproject.com/article/2020/9/how-raspberry-pi-and-kubernetes-go-together) and Raspberry Pi and [machine learning](https://www.techrepublic.com/article/raspberry-pi-and-machine-learning-how-to-get-started/).

## Projects

The idea here is to show some ideas and projects that I created with Raspberry Pi and Java and perhaps give you some insights or ideas.

– A simple Quarkus Qute example that shows a 7 segment display and control in real-time a real one with a Raspberry Pi 3 B.  
[Link](/quarkus-qute-with-raspberry-pi/)

– A Micronaut Vecolcity interface that provides a way to control the 8×8 Led Matrix from SenseHat.  
[Link](/micronaut-velocity-with-raspberry-pi/)

– Using a cardboard and Duke image to create a servo demo where Duke moves his arm.  
[Link](/raspberry-pi-servo-java-duke-robot/)

– A simple Helidon example that shows a 14 segments display and control in real-time a real one with a Raspberry Pi 3 B.  
[Link](/raspberry-pi-helidon-14-segment-display/)

– An application that reads available timezones from worldtimeapi.org and displays them in an autocomplete list. When a region is selected it calls the Qurakus REST API passing the current time and Quarkus set the time value on the segment display.  
[Link](/4x7-segment-display/)

– A simple Spring Boot Thymeleaf app where it shows a form with a 128×64 table. Each table position is the representation of the LCD graphic display. I created an Array of bits with all positions of this table.  
[Link](/spring-thymeleaf-raspberry-pi-lcd/)

Another place to check out and get some ideas and material to learn is the CoderDojo.  
**CoderDojo** is a global volunteer-led community of free programming workshops for young people between 7 and 17. The movement is a grassroots organization with individual clubs acting independently.

I did a talk on **Raspberry Pi from Java to Data Streaming**, where I talked about the idea to use Raspberry PI to learn Java and other programming languages as well.

In this blog, I try to cover the Raspberry Pi and Java parts, and the Data Streaming is already covered in those three blogs

[Kafka at the edge](/kafka-at-the-edge-with-raspberry-pi/)  
[Learn Kafka and event streams with fun](/learn-kafka-and-event-streams-with-fun/)  
[Kafka weather station](/kafka-weather-station/)

Youtube – Raspberry Pi from Java to Data Streaming

**[Raspberry Pi – From Java to Data Streaming](//www.slideshare.net/IgorSouza137/raspberry-pi-from-java-to-data-streaming "Raspberry Pi - From Java to Data Streaming")**  from **[Igor De Souza](//www.slideshare.net/IgorSouza137)**

Powerpoint – Raspberry Pi from Java to Data Streaming

## Books

Getting Started with Java on Raspberry Pi by Frank Delporte

Raspberry Pi with Java: Programming the Internet of Things (IoT) (Oracle Press)  
By Stephen Chin and James Weaver

## Conclusion

The Raspberry Pi is a supremely versatile machine and perfect for any kind of side project or hobby where cost, size, or power consumption is a limitation. There is never a shortage of ideas as the ever-growing community of enthusiasts continues to find new and imaginative ways to put their Pi’s to work.

You can use Java, but you can start with any language that you want and use any technology that you want, from coding and container to data streaming and machine learning.

Remember to use the hashtag #JavaOnRaspberryPi on Twitter to show the world Raspberry Pi with Java.

## Links

<https://www.raspberrypi.org>

<https://pi4j.com/>

<https://openjfx.io/>

<https://www.jbang.dev/>

<https://jreleaser.org/>

<https://www.graalvm.org/>

<https://www.elektormagazine.com/articles/java-on-the-raspberry-pi-part-1-gpios>

<https://www.elektormagazine.com/articles/java-on-the-raspberry-pi-part-2-application>

<https://blogs.oracle.com/javamagazine/getting-started-with-javafx-on-raspberry-pi>

<https://developer.android.com/things>

<https://ubuntu.com/raspberry-pi>

<https://www.oracle.com/linux/downloads/linux-arm-downloads.html>

<https://coderdojo.com/>

<https://projects.raspberrypi.org/en/projects>
