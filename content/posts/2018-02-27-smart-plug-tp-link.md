---
layout: post
title: Smart Plug TP-Link
date: '2018-02-27'
slug: smart-plug-tp-link
tags:
- Python
description: How’s the form? A smart device is an electronic device, generally connected
  to other devices or networks via different wireless protocols such as Bluetooth,
  NFC, Wi-Fi, 3G, etc., that can operate to s
image: wp/2018/02/PXL_20210104_122903391.jpg
---

![](/images/wp/2018/02/PXL_20210104_122903391-1024x768.jpg)

**How’s the form?**

A smart device is an electronic device, generally connected to other devices or networks via different wireless protocols such as Bluetooth, NFC, Wi-Fi, 3G, etc., that can operate to some extent interactively and autonomously.

A smart plug gives you several degrees of added control over just about any electrical appliance in your home. For one thing, it gives you remote access to switch a device on and off. Some you can also program to do so on a set schedule. Many models go a step further to give you in-depth insights about the way you use specific devices and the power they consume.

While many people buy smart plugs for their own convenience, there are plenty of ways they can make the world a better place, as well. The main one is by limiting energy waste. Sure, some models simply allow you to turn a device on or off without physically unplugging it, but others allow you to closely monitor your power usage and make positive changes toward conservation.

I have two models from TP-Link:

HS100  
<https://www.tp-link.com/uk/products/details/cat-5258_HS100.html>

HS110  
<https://www.tp-link.com/uk/products/details/cat-5258_HS110.html>

I found on Google this APIs for Python and Node-Js

Python  
<https://github.com/GadgetReactor/pyHS100>

Example-1:

|  |  |
| --- | --- |
| 1 2 3 | from pyHS100 import Discover  for dev in Discover.discover().values():  print(dev) |

Example-2:

|  |  |
| --- | --- |
| 1 2 3 4 5 | from pyHS100 import SmartPlug, SmartBulb  from pprint import pformat as pf    plug = SmartPlug("192.168.XXX.XXX")  print("Current consumption: %s" % plug.get\_emeter\_realtime()) |

Node-js  
<https://github.com/plasticrake/tplink-smarthome-api>

Example:

|  |  |
| --- | --- |
| 1 2 3 4 5 6 7 8 9 10 11 12 13 | const { Client } = require('tplink-smarthome-api');    const client = new Client();  const plug = client.getDevice({host: '192.168.XXX.XXX'}).then((device)=&gt;{  device.getSysInfo().then(console.log);  device.setPowerState(true);  });    // Look for devices, log to console, and turn them on  client.startDiscovery().on('device-new', (device) =&gt; {  device.getSysInfo().then(console.log);  device.setPowerState(true);  }); |

I manage to turn on or turn off my smart plug from a Tweet.  
https://www.instagram.com/p/BZEimj0guBH/?taken-by=igfasouza
