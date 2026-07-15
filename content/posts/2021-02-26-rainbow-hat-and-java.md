---
layout: post
title: Rainbow HAT and Java
date: '2021-02-26'
slug: rainbow-hat-and-java
tags:
- Java
- Raspberry PI
description: How’s it going there? 2021/02/26 The Rainbow HAT is an add-on board for
  Raspberry Pi, is a collection of sensors, inputs and outputs from popular components
  in one board, which we can attach the 40 pi
image: wp/2021/02/PXL_20210224_202642207.jpg
---

![](/images/wp/2021/02/PXL_20210224_202642207-1024x768.jpg)

**How’s it going there?**  
2021/02/26

The Rainbow HAT is an add-on board for Raspberry Pi, is a collection of sensors, inputs and outputs from popular components in one board, which we can attach the 40 pin pin-out of the Pi.  
After Google announced Android Things Pimoroni designed the all-singing, all-dancing Rainbow HAT. Jam-packed with LEDs, buttons and sensors, it enables you to experiment with Android Things and use it with the wide range of protocols available on the Raspberry Pi.

Rainbow HAT is designed to stimulate ideas – a development platform that can be used to build new and exciting IoT hardware and software. It’s also meant to be fun to use, and that should be apparent just by looking at it – the playful rainbow formed from the seven APA102 LEDs and the barometer type markings below it.

![](/images/wp/2021/02/android-things-starter-kit-1-1024x681.jpg)

**Technical Specification:**

- Seven APA102 multicolor LEDs
- Four 14-segment alphanumeric displays (green LEDs)
- HT16K33 display driver chip
- Three capacitive touch buttons
- Atmel QT1070 capacitive touch driver chip
- Blue, green, and red LEDs
- BMP280 temperature and pressure sensor
- Piezo buzzer
- Breakout pins for servo, 12C, SPI, and UART (all 3v3)

The board is designed specifically to show off the wide range of protocols available on the Raspberry Pi, including SPI (the APA102 LEDs), 12C (the BPM280 sensor and 14-segment displays), GPIO (the capacitive touch buttons and LEDs), and PWM (the piezo buzzer).

[GPIO](https://pinout.xyz/pinout/rainbow_hat)

**Android Things**

Originally known as Project Brillo, Google’s relaunched Android Things operating system is designed to be used with IoT devices. The smart home project got its start in 2015 under the name Brillo, which was meant to provide the “underlying operating system for the internet of things.” In 2016, Google revamped Brillo and relaunched the initiative as Android Things, which was likewise meant to run on products like connected speakers, security cameras, and routers. By relying on Android, the OS was supposed to be familiar to developers and easy to get started with. Google envisioned it as an operating system that would let developers code for a whole world of smart devices using the tools they already knew from coding for Android phones. At the time, that included speakers and displays, but also more experimental gadgets, like small robots, art installations, a projector, a 3D printer, and more.

In 2018, some initial smart speakers and smart displays came out using the underlying OS, and then nothing happened. Nearly two years later, and Android Things is now on track to be shut down. Google recently announced phasing out its Android Things IoT platform. New projects will not be accepted after January 5, 2021, and the Android Things console will be turned down for all projects in 2022.

<https://developer.android.com/things/>

**Getting started with the Rainbow HAT**

For information on how to get started with Android Things and RainbowHAT visit the official developer site for Android Things. To put the latest Android Things image on your SD card, see the instructions [here](https://developer.android.com/things/hardware/raspberrypi.html).

You can find the driver and samples published in the official [GitHub organization](https://github.com/androidthings).

With Raspbian you can check the Python library [here](https://github.com/pimoroni/rainbow-hat).

The Rainbow HAT uses the same 14 segments display that I showed in the [Helidon demo](/raspberry-pi-helidon-14-segment-display/).

**HT16K33 driver**

The HT16K33 is a memory mapping and multi-function LED controller driver. The max. Display segment numbers in the device is 128 patterns (16 segments and 8 commons) with a 13\*3 (MAX.) matrix key scan circuit. The software configuration features of the HT16K33 make it suitable for multiple LED applications including LED modules and display subsystems.

![](/images/wp/2021/02/rainbowhat01-1024x512.png)

I created a Java API to control the Rainbow Hat 14 segments display, using the HT16K33 driver.

This is just a simple test and I create the driver just for the 14 segment display, but one idea is to complete the driver to control all other Rainbow HAT components.  
I follow the idea of the [Android thing](https://github.com/androidthings/contrib-drivers) and translate it to PI4j.

This time I decided to do an example with Javalin.

![](/images/wp/2021/02/javalin.png)

Javalin is a very lightweight web framework for Java 8 (and later) and Kotlin. It supports modern features such as HTTP/2, WebSocket, and asynchronous requests. Javalin is servlet-based, and its main goals are simplicity, a great developer experience, and first-class interoperability between Java and Kotlin. Javalin is built on top of Jetty, and its performance is equivalent to raw Jetty code.

## Idea

A simple Javalin example that shows a 14 segments display and control in real-time using my Java API Rainbow Hat 14 segments display. A 14 segments display – 5421AG with HT16K33 Driver

![](/images/wp/2021/02/result01.jpg)

## Code

|  |  |
| --- | --- |
| 1 2 3 4 5 6 7 8 9 10 | public static void main([String](http://www.google.com/search?hl=en&q=allinurl%3Adocs.oracle.com+javase+docs+api+string)[] args) {  try {  AlphanumericDisplay segment = new AlphanumericDisplay("I2C1");  segment.setBrightness(Ht16k33.HT16K33\_BRIGHTNESS\_MAX);  segment.display("Igor");  segment.setEnabled(true);  } catch ([IOException](http://www.google.com/search?hl=en&q=allinurl%3Adocs.oracle.com+javase+docs+api+ioexception) | UnsupportedBusNumberException e) {  e.printStackTrace();  }  } |

Disclaimer – I got the CSS and JS [here](http://www.3quarks.com/en/SegmentDisplay/).

You can get the full code on my [GitHub](https://github.com/igfasouza/javalin-RainbowHat).

Another cool thing about this idea is that some other Hats use the HT16K33 driver as well, and this means that we can reuse this code just by changing the GPIO numbers. For example the Four Letter pHat.

![](/images/wp/2021/02/four_letter_phat.jpg)

## Links

<https://javalin.io/>

<https://pdf1.alldatasheet.com/datasheet-pdf/view/683745/FORYARD/FYD-5421AX-32.html>

<https://pinout.xyz/pinout/rainbow_hat>

<https://shop.pimoroni.com/products/rainbow-hat-for-android-things>

<https://developer.android.com/things>

<https://shop.pimoroni.com/products/four-letter-phat>

<https://cdn-shop.adafruit.com/datasheets/ht16K33v110.pdf>  
<https://www.adafruit.com/product/1427>
