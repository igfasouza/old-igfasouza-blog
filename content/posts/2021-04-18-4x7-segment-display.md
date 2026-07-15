---
layout: post
title: 4×7 Segment Display
date: '2021-04-18'
slug: 4x7-segment-display
tags:
- Java
- Quarkus
- Raspberry PI
description: How’s the lad? 2021/04/18 This post is to show how I created an app demo
  to control a 4-7 segment display with a Raspberry PI. This is another blog about
  Java on Raspberry PI. It’s kind of a continuat
image: wp/2021/04/react_quarkus.jpg
---

![](/images/wp/2021/04/time-zone.jpg)

**How’s the lad?**  
2021/04/18

This post is to show how I created an app demo to control a 4-7 segment display with a Raspberry PI. This is another blog about Java on Raspberry PI.

It’s kind of a continuation from my previous blog [7-segment-display](/7-segment-display/) but I pivoted the idea a little bit. I divide the app into front end and back end using React and Quarkus.

![](/images/wp/2021/04/react_quarkus.jpg)

## Components

- 1x Raspberry Pi
- 1x 4-7segment display
- 4x Resistor 330 ohm
- 12x Jumper wires (generic)

## Schematics

I have the “***hs420561k-32***” model.

![](/images/wp/2021/04/47seg-pinout.jpg)  
Picture1: component Schematics

![](/images/wp/2021/04/gpio-283x300.png)  
Table1: Pins and GPIOs mapping

**Note**: Pi4J (by default) uses an abstract pin numbering scheme to help insulate software from hardware changes.Pi4J implements the same pin number scheme as the Wiring Pi

This is the Number for the PI 3 B model.

![](/images/wp/2020/09/Pi4J_GPIO-165x300.png)  
Picture2: PI4J GPIO

## Idea

An application that reads available timezones from worldtimeapi.org and displays them in an autocomplete list. When a region is selected it calls the Qurakus REST API passing the current time and Quarkus set the time value on the segment display.

![](/images/wp/2021/04/47segment_app01.png)  
Picture3: End-to-end flow

![](/images/wp/2021/04/47segment_sequence.png)  
Picture4: Sequence Diagram

The way that you get each digit displaying something different is to switch them on and off again, in turn, faster than the eye can observe. Using the same circuitry to control more than one ‘thing’ is called multiplexing.

## Code

|  |  |
| --- | --- |
| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 | package quarkus47segments.igor;  ...    @Path("/clock")  public class Main {        final GpioController gpio = GpioFactory.getInstance();      GpioPinDigitalOutput pin01 = gpio.provisionDigitalOutputPin(RaspiPin.GPIO\_08, "1", PinState.LOW);  ...        @GET      @Path("/{name}")      public [String](http://www.google.com/search?hl=en&q=allinurl%3Adocs.oracle.com+javase+docs+api+string) greeting(@PathParam("name") [String](http://www.google.com/search?hl=en&q=allinurl%3Adocs.oracle.com+javase+docs+api+string) name) throws [InterruptedException](http://www.google.com/search?hl=en&q=allinurl%3Adocs.oracle.com+javase+docs+api+interruptedexception) {          [System](http://www.google.com/search?hl=en&q=allinurl%3Adocs.oracle.com+javase+docs+api+system).out.println("Time " + name);          setClockValue(name);          return "hello " + name;      }        public void setClockValue([String](http://www.google.com/search?hl=en&q=allinurl%3Adocs.oracle.com+javase+docs+api+string) value) throws [InterruptedException](http://www.google.com/search?hl=en&q=allinurl%3Adocs.oracle.com+javase+docs+api+interruptedexception) {      ...      }        public void display(int number) {      ...      }    } |

The code itself is pretty ugly. I could make it into a library so that everything looks nice and clean. But bla bla bla …

![](/images/wp/2021/04/code_meme01-1024x485.jpg)  
Picture5: meme

Kudos to [Elaine Akemi](https://www.linkedin.com/in/elaineakemi/) that created the React app for me. You can get the React code [here](https://github.com/elaineakemi/react-timezone).  
You can get the Quarkus code on my [GitHub](https://github.com/igfasouza/timezone-quarkus47display).

## Result

![](/images/wp/2021/04/react01.jpg)  
Picture6: React app with an auto-complete Combobox

![](/images/wp/2021/04/PXL_20210417_215558015-1024x768.jpg)  
Picture7: example

## Links

<https://pi4j.com/>

<https://github.com/Pi4J/pi4j>

<https://en.wikipedia.org/wiki/Multiplexing>
