---
layout: post
title: Energy switch and smart home with Kafka
date: '2021-03-12'
slug: energy-switch-and-smart-home-with-kafka
tags:
- Kafka
- IoT
- Smart Home
description: How the hell are you? 2021/03/12 Smart devices are all of the everyday
  objects made intelligent with advanced computers, including AI and machine learning,
  and networked to form the internet of things
image: wp/2021/03/Lamp-switch3.jpg
---

![](/images/wp/2021/03/Lamp-switch3.jpg)

**How the hell are you?**  
2021/03/12

Smart devices are all of the everyday objects made intelligent with advanced computers, including AI and machine learning, and networked to form the internet of things (IoT).  
Not just computers and smartphones, but everything: clocks, speakers, lights, doorbells, cameras, windows, window blinds, hot water heaters, appliances, cooking utensils, you name it. And what if those devices could all communicate, send you information, and take your commands? And what if I could use Kafka to get this device’s real-time information?

![](/images/wp/2021/03/smart_home01.jpg)

Today I want to show a Raspberry PI Java Spring web app to simulate a Lamp switch using the TP-link smart bulb and smart plug. Once the device is on its start to collect the real-time energy consumption info and send to a Kafka topic.

I already did a blog about [TP-link smart plush](/smart-plug-tp-link/), but today I want to use a Java API that I found [here](https://github.com/CalicoCatalyst/hs-100) and [here](https://github.com/Phi-S/tplink_smartplug_HS110). I kind of did a mix of both.

I’m using a smart plug HS110 and smart bulb LB110

## code

|  |  |
| --- | --- |
| 1 2 3 4 5 | @RequestMapping(  value = "/process",  method = RequestMethod.POST,  consumes = "text/plain")  public void process(@RequestBody [String](http://www.google.com/search?hl=en&q=allinurl%3Adocs.oracle.com+javase+docs+api+string) payload) throws [Exception](http://www.google.com/search?hl=en&q=allinurl%3Adocs.oracle.com+javase+docs+api+exception) { |

|  |  |
| --- | --- |
| 1 2 3 4 5 6 7 8 | [System](http://www.google.com/search?hl=en&q=allinurl%3Adocs.oracle.com+javase+docs+api+system).out.println(payload);    if(payload.equals("true")){  plug.switchOn();  this.producer.sendMessage(plug.getEnergy());  }else {  plug.switchOff();  } |

|  |  |
| --- | --- |
| 1 | } |

For configure kafka just need add the settings on “application.yml”. Here I did with my [raspberry pi kafka cluster](/raspberry-pi-kafka-cluster/).

![](/images/wp/2021/03/01.jpg)

Disclaimer – I got the CSS from [here](https://codepen.io/designcouch/pen/dCBJr)

You can get the full code on my [GitHub](https://github.com/igfasouza/spring-switch).

And you can combine this with my [influxdb-and-grafana](/raspberry-pi-with-influxdb-and-grafana/) blog and add some nice visualization.

Smart Plug HS110

Smart Light lb110

![](/images/wp/2021/03/Screenshot-2021-03-10-at-19.05.32-1024x333.png)

I mentored a colleague in a similar [project](https://github.com/jod98/Oracle_Energy_Consumption_Project)
