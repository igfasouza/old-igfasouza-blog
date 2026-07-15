---
layout: post
title: Raspberry Pi Helidon 14 segment display
date: '2021-02-22'
slug: raspberry-pi-helidon-14-segment-display
tags:
- Java
- Pi4J
- Raspberry PI
description: How goes the battle? 2021/02/22 This post is to show how I created a
  Helidon demo with a Raspberry PI. A simple web application to control a 14 segments
  display. This is another blog about Java on Ras
image: wp/2021/02/helidon_raspberry.jpg
---

![](/old-igfasouza-blog/images/wp/2021/02/helidon_raspberry.jpg)

**How goes the battle?**  
2021/02/22

This post is to show how I created a Helidon demo with a Raspberry PI. A simple web application to control a 14 segments display. This is another blog about Java on Raspberry PI.

![](/old-igfasouza-blog/images/wp/2021/02/PXL_20210219_205957688-1024x768.jpg)

Originally named J4C (Java for Cloud), Helidon was designed to be simple and fast, and the framework supports two programming models for writing microservices: Helidon SE and Helidon MP. Helidon SE is designed to be a microframework that supports the reactive programming model, it features three core APIs to create a microservice; a web server, configuration, and security. Helidon MP, on the other hand, is an Eclipse MicroProfile runtime that allows the Jakarta EE community to run microservices in a portable way; supports the MicroProfile 1.1 specification for building microservices-based applications.  
But in both cases, a Helidon microservice is a Java SE application that starts a tinny HTTP server from the main method.

![](/old-igfasouza-blog/images/wp/2021/02/helidon-se_mp.png)  
Helidon architecture

![](/old-igfasouza-blog/images/wp/2021/02/helidon-graph.png)  
Microservices frameworks categories

![](/old-igfasouza-blog/images/wp/2021/02/helidonn20.jpg)  
Helidon 2.0 adds significant improvements for both Helidon SE and Helidon MP programming styles

**Fun Facts**  
Helidon is a Greek word for swallow, a type of bird that according to Wikipedia has “a slender, streamlined body and long pointed wings, which allow great maneuverability and very efficient flight”. Perfect for darting through the clouds.

## Idea

A simple Helidon example that shows a 14 segments display and control in real-time a real one with a Raspberry Pi 3 B.

I have the “**5421AG**” model. 14 segments display – [5421AG](https://pdf1.alldatasheet.com/datasheet-pdf/view/683745/FORYARD/FYD-5421AX-32.html)

![](/old-igfasouza-blog/images/wp/2021/02/14segment.jpg)

![](/old-igfasouza-blog/images/wp/2021/02/14segment_pins.jpg)

The PI4J uses a different GPIO number.

**Note**: Pi4J (by default) uses an abstract pin numbering scheme to help insulate software from hardware changes. Pi4J implements the same pin number scheme as the Wiring Pi

<http://wiringpi.com/pins/>

![](/old-igfasouza-blog/images/wp/2020/09/Pi4J_GPIO.png)

![](/old-igfasouza-blog/images/wp/2021/02/Screenshot-2021-02-22-at-17.27.02-388x1024.png)

PIN 11 -> GPIO 11  
PIN16 -> GPIO 25

## Code

```
static Routing createRouting() {
List<class<? extends="" encoder="">&gt; encoders = Collections.singletonList(UppercaseEncoder.class);</class<?>
```

```

```

```
return Routing.builder()
.register("/rest", component)
.register("/websocket",
TyrusSupport.builder().register(
ServerEndpointConfig.Builder.create(MessageBoardEndpoint.class, "/board")
.encoders(encoders).build())
.build())
.register("/web", StaticContentSupport.builder("/WEB").build())
.build();
}
```

Disclaimer – I use the same CSS that I used in my [Quarkus Qute example](/old-igfasouza-blog/quarkus-qute-with-raspberry-pi/) and I started this demo using this [WebSocket sample](https://github.com/oracle/helidon/tree/master/examples/webserver/websocket)

You can get the full code on my [GitHub](https://github.com/igfasouza/helidon-14segments-display).

![](/old-igfasouza-blog/images/wp/2021/02/Screenshot-2021-02-22-at-13.48.17-204x300.png)

Links

<https://helidon.io>

<https://github.com/oracle/helidon>

<https://www.youtube.com/channel/UChg00-uTTrCMmPsuzUNaZsA>

<https://medium.com/helidon>

<https://twitter.com/helidon_project>

<https://www.jetbrains.com/help/idea/helidon.html>

<https://microprofile.io/>
