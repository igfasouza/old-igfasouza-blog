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

![](/old-igfasouza-blog/images/wp/2021/04/time-zone.jpg)

**How’s the lad?**  
2021/04/18

This post is to show how I created an app demo to control a 4-7 segment display with a Raspberry PI. This is another blog about Java on Raspberry PI.

It’s kind of a continuation from my previous blog [7-segment-display](/old-igfasouza-blog/7-segment-display/) but I pivoted the idea a little bit. I divide the app into front end and back end using React and Quarkus.

![](/old-igfasouza-blog/images/wp/2021/04/react_quarkus.jpg)

## Components

- 1x Raspberry Pi
- 1x 4-7segment display
- 4x Resistor 330 ohm
- 12x Jumper wires (generic)

## Schematics

I have the “***hs420561k-32***” model.

![](/old-igfasouza-blog/images/wp/2021/04/47seg-pinout.jpg)  
Picture1: component Schematics

![](/old-igfasouza-blog/images/wp/2021/04/gpio-283x300.png)  
Table1: Pins and GPIOs mapping

**Note**: Pi4J (by default) uses an abstract pin numbering scheme to help insulate software from hardware changes.Pi4J implements the same pin number scheme as the Wiring Pi

This is the Number for the PI 3 B model.

![](/old-igfasouza-blog/images/wp/2020/09/Pi4J_GPIO-165x300.png)  
Picture2: PI4J GPIO

## Idea

An application that reads available timezones from worldtimeapi.org and displays them in an autocomplete list. When a region is selected it calls the Qurakus REST API passing the current time and Quarkus set the time value on the segment display.

![](/old-igfasouza-blog/images/wp/2021/04/47segment_app01.png)  
Picture3: End-to-end flow

![](/old-igfasouza-blog/images/wp/2021/04/47segment_sequence.png)  
Picture4: Sequence Diagram

The way that you get each digit displaying something different is to switch them on and off again, in turn, faster than the eye can observe. Using the same circuitry to control more than one ‘thing’ is called multiplexing.

## Code

```java
package quarkus47segments.igor;
...
@Path("/clock")
public class Main {
final GpioController gpio = GpioFactory.getInstance();
    GpioPinDigitalOutput pin01 = gpio.provisionDigitalOutputPin(RaspiPin.GPIO_08, "1", PinState.LOW);
...
    @GET
    @Path("/{name}")
    public String greeting(@PathParam("name") String name) throws InterruptedException {
        System.out.println("Time " + name);
        setClockValue(name);
        return "hello " + name;
    }
    public void setClockValue(String value) throws InterruptedException {
    ...
    }
    public void display(int number) {
    ...
    }
}
```

The code itself is pretty ugly. I could make it into a library so that everything looks nice and clean. But bla bla bla …

![](/old-igfasouza-blog/images/wp/2021/04/code_meme01-1024x485.jpg)  
Picture5: meme

Kudos to [Elaine Akemi](https://www.linkedin.com/in/elaineakemi/) that created the React app for me. You can get the React code [here](https://github.com/elaineakemi/react-timezone).  
You can get the Quarkus code on my [GitHub](https://github.com/igfasouza/timezone-quarkus47display).

## Result

![](/old-igfasouza-blog/images/wp/2021/04/react01.jpg)  
Picture6: React app with an auto-complete Combobox

![](/old-igfasouza-blog/images/wp/2021/04/PXL_20210417_215558015-1024x768.jpg)  
Picture7: example

## Links

<https://pi4j.com/>

<https://github.com/Pi4J/pi4j>

<https://en.wikipedia.org/wiki/Multiplexing>
