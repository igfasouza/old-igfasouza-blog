---
layout: post
title: Connected vehicles & Self-driving cars with Kafka
date: '2021-03-08'
slug: connected-vehicles-self-driving-cars-with-kafka
tags:
- Kafka
- Raspberry PI
description: How’s the form? 2021/03/08 The term connected vehicles refer to applications,
  services, and technologies that connect a vehicle to its surroundings. A connected
  vehicle includes the different communic
image: wp/2021/03/Connected-Vehicles_ktDePriK.jpg
---

![](/images/wp/2021/03/ankicar1.jpg)

**How’s the form?**  
2021/03/08

The term connected vehicles refer to applications, services, and technologies that connect a vehicle to its surroundings. A connected vehicle includes the different communication devices (embedded or portable) present in the vehicle, that enable in-car connectivity with other devices present in the vehicle and/or enable connection of the vehicle to external devices, networks, applications, and services.

Self-driving cars are vehicles capable of sensing their environment and operating without human involvement.

![](/images/wp/2021/03/Connected-Vehicles_ktDePriK.jpg)

So today I want to show a simple demo where I can stream car data in real-time using Kafka. Because I don’t have a real autonomous car and came with the idea to use Anki Car or Anki Overdrive.

Anki Overdrive is an intelligent battle racing system that lets you explore the power of artificial intelligence (AI). You can see a nice overview, [all the new features explained](https://www.pocket-lint.com/parenting/buyers-guides/132703-anki-overdrive-vs-anki-drive-all-the-new-features-explained).

All naming rights for Anki, Anki Drive and Anki Overdrive are property of Anki.

With the standard Anki Overdrive Kit, you get two cars, some road pieces to construct simple road maps and a charging platform for the cars. It is all you need to start playing around with.  
Check the [driver-sdk](https://github.com/anki/drive-sdk).

Using a Bluetooth Low Energy (BLE) API you can connect and disconnect from Anki, change some settings and of course you can get some real-time information.

I found this [anki-drive-python-sdk](https://github.com/jacopotagliabue/anki-drive-python-sdk) that uses Python and node to get the real-time data using BLE

![](/images/wp/2021/03/end_flow.jpg)

Here is the info that I can get.

![](/images/wp/2021/03/anki_data.jpg)

**JSON**

|  |  |
| --- | --- |
| 1 | {'location': 17, 'piece': 36, 'offset': 67.5, 'speed': 390, 'self\_speed': 400, 'clockwise': 7, 'notification\_time': datetime.datetime(2018, 8, 25, 21, 9, 33, 359248), 'is\_clockwise': False} |

|  |  |
| --- | --- |
| 1 |  |

|  |  |
| --- | --- |
| 1 | {'location': 23, 'piece': 57, 'offset': 67.5, 'speed': 422, 'self\_speed': 400, 'clockwise': 71, 'notification\_time': datetime.datetime(2018, 8, 25, 21, 9, 32, 229689), 'is\_clockwise': True} |

Piece uniquely identify the type of road piece (curve, start, stop, intersection, straight), speed is the speed recorded by the vehicle, self\_speed is the “theoretical” speed as set by our command, offset identifies the “lane” (see a visual explanation below), and the location is an incremental integer (see a visual explanation below).

![](/images/wp/2021/03/offset.jpg)

![](/images/wp/2021/03/start_lanes.jpg)

![](/images/wp/2021/03/track-1024x468.png)

## Idea

A simple Raspberry PI demo where I can get the Anki Car data in real-time and send it to Kafka. I can explore the data after with some graphics or some data analyses.

You can check the “create\_track\_image.py” and create your track map.

![](/images/wp/2021/03/track-segments.png)

![](/images/wp/2021/03/circuit01.jpeg)

With the map you can start thinking in some analyses, E.g, can I make the car go faster? I can do some analyses in my track and determine where the car can speed up and where should slow down,

![](/images/wp/2021/03/circuit02.jpeg)

You can buy an extra Anki Collision Kit, which includes an intersection and try to create a Collision Prevention Algorithm.

![](/images/wp/2021/03/anki_x-1024x950.jpg)

Now we have a basic, but functional setup to run experiments and collect data from our small cars, but there are indeed a lot of interesting data questions we could try to answer.

- how can a vehicle learn the best “driving policy” given a track configuration?
- What will change when we introduce other vehicles? We could, for example, have them compete against each other, or we could use the second vehicle to learn cooperative behavior (e.g. avoid collision).
- Can we add Traffic Light. Unfortunately I don’t have this [hat](https://thepihut.com/collections/raspberry-pi-led-hats/products/pi-stop-educational-traffic-light-for-raspberry-pi).

![](/images/wp/2021/03/traffic_light.jpg)

- Can we condition the learning process on variables other than the track configuration?
- How smart can the vehicle be with the current sensors? As we saw already with position, sensors are pretty basic and won’t allow a fine-grained control: what can we do to be smarter with what we have (e.g. interpolate position?) and what can we easily add to give us more dimensions to play with (e.g. webcam with object recognition)?
- Anki Overdrive has the Supertrucks as well. What can we do differently with the truck?

And many more, this is not an exhaustive list.

## Similar ideas

<https://github.com/AnkInnovator>

<https://github.com/IBM/object-detection-anki-overdrive-cars>

<https://github.com/opcau/opcau.github.io>

## Link

<https://site.ieee.org/connected-vehicles/ieee-connected-vechicles/connected-vehicles/>

<https://www.digi.com/blog/post/what-is-connected-vehicle-technology-and-use-cases>

<https://www.synopsys.com/automotive/what-is-autonomous-car.html>

<https://github.com/anki/drive-sdk>

<https://github.com/jacopotagliabue/anki-drive-python-sdk>
