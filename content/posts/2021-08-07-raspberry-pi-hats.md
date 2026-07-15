---
layout: post
title: Raspberry Pi Hats
date: '2021-08-07'
slug: raspberry-pi-hats
tags:
- Java
- Raspberry PI
description: How’s the lad? This is another blog about Raspberry PI, and today I want
  to talk about Raspberry Pi Hats or pHats. Thanks to their GPIO headers, most Pi
  computers can connect to devices called HATs, w
image: wp/2021/08/igor-pi.jpg
---

![](/old-igfasouza-blog/images/wp/2021/08/igor-pi.jpg)

**How’s the lad?**

This is another blog about Raspberry PI, and today I want to talk about Raspberry Pi Hats or pHats.

Thanks to their GPIO headers, most Pi computers can connect to devices called HATs, which stands for Hardware Attached on Top. HATs are incredible add-ons to the Raspberry Pi that increase its functionality in a huge number of ways.

In short, it’s an additional card that you plug into your Raspberry Pi to bring new features. Generally, it uses the GPIO ports to connect the two cards together. The Raspberry Pi recognizes the HAT thanks to an EEPROM module on the board that identifies the HAT model.  
The Raspberry Pi is an awesome platform for learning and experimentation. We can learn to code, build robots, monitor the location of the International Space Station, and so much more. But to make the most of the Pi, it helps to have the right HAT. There are hundreds of extensions that you can find for your Raspberry and there are several manufacturers for these Hats.

Today I want to show you a list of some Raspberry Pi HATs on the market.

**Table of contents**

1. Hat VS pHat  
2. Hat list

- 01. PoE+ Hat
- 02 .Enviro Plus
- 03. Explorer Hat Pro
- 04. GFX Hat
- 05. Inky pHat
- 06. Unicorn HD Hat
- 07. Cluster Hat
- 08. TV Hat
- 09. Automation Hat
- 10. Grow Hat
- 11 .NFC Hat
- 12. RFID Hat
- 13. DockerPi Sensor Hub
- 14. PiFinger – Fingerprint Hat
- 15. SparkFun Top pHat
- 16. Pioneer600 Raspberry Pi Expansion Board

3. Camjam  
4. Google AIY  
5. Grove Kit Hat  
6. Manufacturer list  
7. Links

![](/old-igfasouza-blog/images/wp/2021/08/Base-hat.png)  
Picture 1: Raspberry Pi Hat

Perhaps when you think about a Raspberry PI Hat the two most common and popular ones are the [Sense Hat](/old-igfasouza-blog/sense-hat/) and the [Rainbow Hat](/old-igfasouza-blog/rainbow-hat-and-java/) and I didn’t add them to this list because I already did a blog post for each one.

You can also see my blog about Raspberry [Christmas Hat](/old-igfasouza-blog/raspberry-christmas-hat/).

## 1. Hat VS pHat

In a short explanation, Hats are designed to work with standard Raspberry Pi computers (such as the Model B 4), while pHats are designed to work with the Raspberry Pi Zero.

![](/old-igfasouza-blog/images/wp/2021/08/pi-orientation.png)  
Picture 2: Hat formats

You will find in the product documentation how to assemble the hat and generally, there is a specific library for your Hat. They are plug-and-play.

![](/old-igfasouza-blog/images/wp/2018/02/attach-sense-hat-to-pi.gif)  
Picture 3: Place the hat on the GPIO pins

Unfortunately, some Hats don’t have any Java API or wrapper around to use Java.

## 2. Hat list

This is not an exhaustive list and doesn’t have any particular order. I started with 5 in my mind and ended with 16 Hats on my list.

**01.PoE+ Hat** [Link](https://thepihut.com/products/raspberry-pi-poe-plus-hat)  
![](/old-igfasouza-blog/images/wp/2021/08/01-PoEhat.jpg)

The Raspberry Pi PoE+ HAT is a new version of the original Raspberry Pi PoE HAT, now with 5V 4A output for the most demanding Raspberry Pi applications! It is designed to replace the original PoE HAT in all new and existing designs and meets all requirements of the IEEE 802.3af (802.3at Type 1) specifications.

<https://thepihut.com/products/raspberry-pi-power-over-ethernet-poe-hat>

[controversy](https://www.youtube.com/watch?v=XZ08QKAbBoU)

**02. Enviro Plus** [Link](https://shop.pimoroni.com/products/enviro?variant=31155658489939)  
![](/old-igfasouza-blog/images/wp/2021/08/02.-Enviro-Plus.jpg)

Monitor your world with Enviro and Enviro + Air Quality for Raspberry Pi! There’s a whole bunch of fancy environmental sensors on these boards, and a gorgeous little full-color LCD to display your data. They’re the perfect way to get started with citizen science and environmental monitoring!

<https://github.com/pimoroni/enviroplus-python>

There are a lot of ideas and projects using this hat with IOT, MQTT and data analysis.

**03. Explorer Hat Pro** [Link](https://thepihut.com/products/explorer-hat)  
![](/old-igfasouza-blog/images/wp/2021/08/03-Explorer-Hat-Pro.jpg)

The Explorer Hat Pro has digital inputs and outputs, capacitive touch pads, croc. clip compatible pads, colored LEDs, analog inputs, motor drivers, and a mini breadboard for prototyping your projects

<https://github.com/pimoroni/explorer-hat>

<https://github.com/romilly/explorer-hat-examples>

Perhaps after Sense hat and Rainbow hat the third most popular.

**04. GFX Hat** [Link](https://thepihut.com/products/gfx-hat-128x64-lcd-display-with-rgb-backlight-and-touch-buttons)  
![](/old-igfasouza-blog/images/wp/2021/08/04-GFX-Hat.jpg)

A 128×64 pixel, 2.15″ LCD display with snazzy six-zone RGB backlight and six capacitive touch buttons. GFX HAT makes an ideal display and interfaces for your headless Pi projects.  
GFX HAT riffs off our beloved Display-O-Tron HAT, but gives you the flexibility of individual pixels, letting you display more complex graphics and real typefaces, while retaining the handy capacitive touch buttons for input/navigation.

**05. Inky pHat** [Link](https://shop.pimoroni.com/products/inky-phat?variant=12549254938707)  
![](/old-igfasouza-blog/images/wp/2021/08/05-Inky-pHat.jpg)

A low-energy, high-falutin, electronic paper (ePaper / eInk / EPD) display for your Pi, in three different colour schemes: red/black/white, yellow/black/white, and black/white!

I found this Android of things [API](https://github.com/novoda/contrib-drivers/tree/inky-phat/inkyphat) that could be translated in PI4j

The e-ink display has several sizes and formats and several other vendors doing a similar one like; Adafruit, SparkFun and Waveshare.

Unfortunately, I never found a blog or site with any comparison. Hello Adafruit, SparkFun and Waveshare, I will love to do this if you guys send one to test and play around.

Perhaps is famous because of the Pwnagotchi project or the Pwnagotchi project became famous because of the several e-ink hats options.

**Pwnagotchi** is an A2C-based “AI” powered by bettercap and running on a Raspberry Pi Zero W that learns from its surrounding WiFi environment to maximize the crackable WPA key material it captures (either through passive sniffing or by performing deauthentication and association attacks). This material is collected on disk as PCAP files containing any form of handshake supported by hashcat, including full and half WPA handshakes as well as PMKIDs.

<https://pwnagotchi.ai/>

**06. Unicorn HD Hat** [Link](https://thepihut.com/products/unicorn-hat-hd)  
![](/old-igfasouza-blog/images/wp/2021/08/06-Unicorn-HD-Hat.jpg)

Unicorn HAT HD crams 256 RGB LEDs, in a 16×16 matrix, onto a single HAT. High-definition rainbow goodness!

**07. Cluster Hat** [Link](https://thepihut.com/products/cluster-hat-v2-0)  
![](/old-igfasouza-blog/images/wp/2021/08/07-Cluster-Hat.jpg)

The Cluster HAT v2.5 interfaces a Raspberry Pi 4 (or older A+/B+/2/3) with 4 Raspberry Pi Zeros. Configured to use USB Gadget mode, it is an ideal tool for teaching, testing or simulating small-scale clusters.

**08. TV Hat** [Link](https://thepihut.com/products/raspberry-pi-tv-hat)  
![](/old-igfasouza-blog/images/wp/2021/08/08-TV-Hat.jpg)

The Raspberry Pi TV HAT is a DVB-T2 Digital TV receiver add on for the Raspberry Pi, compatible with the Raspberry Pi 3 Model B+ or Raspberry Pi Zero W (and older Raspberry Pi 2 & 3 models)

**09. Automation Hat** [Link](https://thepihut.com/products/automation-hat)  
![](/old-igfasouza-blog/images/wp/2021/08/09-Automation-Hat.jpg)

Take control of and monitor your world with our ultimate jack-of-all-trades Raspberry Pi HAT!  
With relays, analog channels, powered outputs, and buffered inputs (all 24V tolerant) you can now hook up a plethora of goodies to your Raspberry Pi all at once.

**10. Grow Hat** [Link](https://shop.pimoroni.com/products/grow?variant=32208365486163)  
![](/old-igfasouza-blog/images/wp/2021/08/10-Grow-Hat.jpg)

A compact Raspberry Pi-powered monitoring system designed to help you take the best possible care of your plants. It will tell you how well they’re hydrated, attract your attention when they need water and, if you want to go a step further, even give them water!

Check out @alexellisuk and the has tag #growlab on Twitter.

**11. NFC Hat** [Link](https://thepihut.com/products/nfc-hat-for-raspberry-pi-pn532)  
![](/old-igfasouza-blog/images/wp/2021/08/11-NFC-Hat.jpg)

This is a Raspberry Pi NFC HAT based on the PN532 operating in the 13.56MHz frequency range. It supports three communication interfaces: I2C, SPI, and UART.

**12. RFID Hat** [Link](https://thepihut.com/products/rfid-hat-for-raspberry-pi)  
![](/old-igfasouza-blog/images/wp/2021/08/12-RFID-Hat.jpg)

The RFID HAT for the Raspberry Pi boasts an updated UART interface running at the frequency of 125KHz with a compact design that includes a programmable 0.91” OLED Display. The HAT also comes with an RFID key card and fob.

**13. DockerPi Sensor Hub** [Link](https://thepihut.com/products/dockerpi-sensor-hub-for-raspberry-pi)  
![](/old-igfasouza-blog/images/wp/2021/08/13-Sensor-Hub.jpg)

The DockerPi SensorHub is great for obtaining environmental parameters for an Internet of Things (IoT) project with your Raspberry Pi.

<https://wiki.52pi.com/index.php/DockerPi_Sensor_Hub_Development_Board_SKU:_EP-0106>

I liked this one because the documentation has a Java example and this hat has a good price.

**14. PiFinger** [Link](https://thepihut.com/products/pifinger-fingerprint-hat-for-raspberry-pi)  
![](/old-igfasouza-blog/images/wp/2021/08/14-PiFinger.jpg)

The PiFinger is quite possibly the first-ever Fingerprint HAT for the Raspberry Pi! This unique HAT allows you to capture and compare fingerprints with high accuracy, allowing you to make your secure projects using fingerprints as a trigger/access key for data or any other output.

**15. SparkFun Top pHat** [Link](https://thepihut.com/products/sparkfun-top-phat-for-raspberry-pi)  
![](/old-igfasouza-blog/images/wp/2021/08/15-SparkFun-Top-pHat-.png)

The SparkFun Top pHAT for Raspberry Pi is intended to be at the top of a pHAT stack so you won’t find any pins for stacking on top of this board, but that’s ok because you will want to preserve your view of the 2.4″ TFT display, six RGB LED’s and three switches squeezed onto this board!

**16. Pioneer600 Expansion Board** [Link](https://thepihut.com/products/pioneer600-raspberry-pi-expansion-board)  
![](/old-igfasouza-blog/images/wp/2021/08/16-Pioneer600-Expansion-Board.jpg)

The Pioneer600 is an all-in-one multifunction expansion board for the Raspberry Pi (compatible with all 40-pin GPIO models).

<https://www.waveshare.com/wiki/Pioneer600>

**Note**: I just used Pimoroni and The Pi Hut links because was the easy ones and I’m not training to advertise anything.

## 3. Camjam

CamJam – The Cambridge Raspberry Jam is a computing event and meet-up for those interested in the Raspberry Pi and other technologies which encourage making and education.

<http://camjam.me>

They have EduKit, which is a partnership with The Pi Hut.

CamJam EduKit 1 – [Starter](https://camjam.me/?page_id=236)  
CamJam EduKit 2 – [Sensors](https://camjam.me/?page_id=623)  
CamJam EduKit 3 – [Robotics](https://camjam.me/?page_id=1035)

## 4. Google AIY

The AIY Voice Kit from Google lets you build your natural language processor and connect it to the Google Assistant or Cloud Speech-to-Text service, allowing you to ask questions and issue voice commands to your programs. All of this fits in a handy little cardboard cube, powered by a Raspberry Pi.

As a play on words from the classic Do-It-Yourself acronym, “AIY” simply stands for Artificial-Intelligence-Yourself and they aren’t kidding. They have released several projects and there is a TPU board as well.

<https://aiyprojects.withgoogle.com>

## 5. Grove Kit Hat

Grove is a modular prototyping system that consists of a base unit and various modules with standardized connectors. The base unit is generally a microprocessor that allows for communicating, processes and controls the input or output from the Grove modules. Every single Grove module typically addresses a single function, ranging from a simple button to a more complex heart rate sensor. The standardized Grove connector allows users to assemble Grove units with a building block approach, compared to the jumper or solder-based system it is much easier to assemble or disassemble, which simplifies the learning system for experimenting, building and prototyping.

There are several hats as well.  
<https://wiki.seeedstudio.com/Grove_Base_Kit_for_Raspberry_Pi>

## 6. Manufacturer list

This is not an exhaustive list.

- 4tronix
- Adafruit
- ModMyPi
- The Pi Hut
- Pimoroni
- SparkFun
- Waveshare

Youtube – Top 20 Raspberry Pi projects you must try in 2021

## 7. Links

<https://magpi.raspberrypi.org/articles/best-raspberry-pi-hats>

<https://pinout.xyz>

<https://camjam.me>

<https://aiyprojects.withgoogle.com>

<https://wiki.seeedstudio.com/Grove_Base_Kit_for_Raspberry_Pi>

Remember to use the hashtag #JavaOnRaspberryPi on Twitter to show the world Raspberry Pi with Java.
