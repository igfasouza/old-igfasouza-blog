---
layout: post
title: Raspberry Christmas Hat
date: '2020-12-24'
slug: raspberry-christmas-hat
tags:
- Java
- Pi4J
- Raspberry PI
description: What’s the story Rory? Today I want to show some Christmas project ideas
  using Hats. Yes, another blog about Raspberry PI. Thanks to their GPIO headers,
  most Pi computers can connect to devices called
image: wp/2020/12/Christmas-hat.jpg
---

![](/images/wp/2020/12/Christmas-hat.jpg)

**What’s the story Rory?**

Today I want to show some Christmas project ideas using Hats. Yes, another blog about Raspberry PI.

Thanks to their GPIO headers, most Pi computers can connect to devices called HATs, which stands for Hardware Attached on Top.

Theses are the Hats that I have and they came from [ThePiHut](https://thepihut.com/)

**Christmas Tree Programmable Kit** – [Link](https://thepihut.com/products/christmas-tree-programmable-kit)

I think this hat comes in 3 different sets, one just with white LEDs, one with just red LEDs and one with mixed white and red LEDs and you can find the Pre-soldered version as well.  
From the [Python API](https://github.com/modmypi/Programmable-Xmas-Tree/blob/master/christmastree.py) you can get the GPIO numbers to use with PI4j

> Raspberry pi projects …. [pic.twitter.com/D2RbQ2Ak9D](https://t.co/D2RbQ2Ak9D)
>
> — Igor Souza (@Igfasouza) [October 30, 2019](https://twitter.com/Igfasouza/status/1189459356208816128?ref_src=twsrc%5Etfw)

**SnowPi** – [Link](https://thepihut.com/blogs/raspberry-pi-tutorials/ryanteck-snowpi-gpio-zero-guide)

The SnowPi is a discontinued item, but you can find it in ThePiHut.  
From the [Python API](https://github.com/penguintutor/snowman/blob/master/snowman.py) you can get the GPIO numbers to use with PI4j

> SnowPI [@ThePiHut](https://twitter.com/ThePiHut?ref_src=twsrc%5Etfw) [@Raspberry\_Pi](https://twitter.com/Raspberry_Pi?ref_src=twsrc%5Etfw) [pic.twitter.com/9tC4G11P9J](https://t.co/9tC4G11P9J)
>
> — Igor Souza (@Igfasouza) [August 4, 2019](https://twitter.com/Igfasouza/status/1158031446537310208?ref_src=twsrc%5Etfw)

During 2020 there was another successful Kickstarter project for the SnowPi RGB. This is a new version of the Snowman. There is no soldering required and it now has color NeoPixels instead of single color LEDs.

**3D Xmas Tree for Raspberry Pi** – [Link](https://thepihut.com/products/3d-xmas-tree-for-raspberry-pi)

After a while, they release an [RGB version](https://thepihut.com/products/3d-rgb-xmas-tree-for-raspberry-pi) as well. Like all the others you can find the Pre-soldered version as well.  
From the code sample, you can get the GPIO numbers to use with PI4j

> [pic.twitter.com/yvk3Ff3HNg](https://t.co/yvk3Ff3HNg)
>
> — Igor Souza (@Igfasouza) [December 4, 2017](https://twitter.com/Igfasouza/status/937832903580487682?ref_src=twsrc%5Etfw)

**Raspberry Pi Christmas Tree Star** – [Link](https://thepihut.com/products/raspberry-pi-christmas-tree-star)

From the [Python API](https://github.com/modmypi/Programmable-Christmas-Star/blob/master/star.py) you can get the GPIO numbers to use with PI4j

![](/images/wp/2020/12/EpEses6XUAcgqQx-225x300.jpg)

The idea here is that all hats are just boards with some LEDs, and this makes the project like an electronics project for blinking LEDs.  
We can use the PWM idea, “Pulse Width Modulation” that I already explained [here](/raspberry-pi-servo-java-duke-robot/), but let me explain from the LEDs perspective.

From [Wikipedia](https://en.wikipedia.org/wiki/Pulse-width_modulation)

> The term duty cycle describes the proportion of ‘on’ time to the regular interval or ‘period’ of time; a low duty cycle corresponds to low power because the power is off for most of the time. Duty cycle is expressed in percent, 100% being fully on. When a digital signal is on half of the time and off the other half of the time, the digital signal has a duty cycle of 50% and resembles a “square” wave. When a digital signal spends more time in the on state than the off state, it has a duty cycle of >50%. When a digital signal spends more time in the off state than the on state, it has a duty cycle of <50%. Here is a pictorial that illustrates these three scenarios.

![](/images/wp/2020/12/Duty_Cycle_Examples.png)

You can find examples and samples for all Hats in Python, but because I support the [#JavaOnRaspberryPi](https://twitter.com/hashtag/JavaOnRaspberryPi) idea, let’s see how to use them with Java.  
Remember to use the hashtag #JavaOnRaspberryPi on Twitter to show the world Raspberry Pi with Java.

**PI4J**  
You can check my post to start with [PI4J](/7-segment-display/) but for these hats what you need to understand is the [Pwm Example](https://github.com/Pi4J/pi4j/blob/master/pi4j-example/src/main/java/PwmExample.java)

|  |  |
| --- | --- |
| 1 2 3 | com.pi4j.wiringpi.Gpio.pwmSetMode(com.pi4j.wiringpi.Gpio.PWM\_MODE\_MS);  com.pi4j.wiringpi.Gpio.pwmSetRange(100);  com.pi4j.wiringpi.Gpio.pwmSetClock(500); |

The idea is that “setPwm()” can be 0, to turn off, 100, to turn on and any value between 0 and 100 to create a fade.

|  |  |
| --- | --- |
| 1 2 3 | setPwm(0)  setPwm(100)  setPwm(value); |

Now you can not just turn on and off, but you can also pulse, blink and add a fade effect.

Here is my forest project from 2018.

> [View this post on Instagram](https://www.instagram.com/p/B6eH44WBFoV/?utm_source=ig_embed&utm_campaign=loading)
>
> [A post shared by igfasouza (@igfasouza)](https://www.instagram.com/p/B6eH44WBFoV/?utm_source=ig_embed&utm_campaign=loading)

Of course, you can do some Christmas ideas with any other hat.

**Sensehat** </sense-hat/>

You can create your Christmas tree using my [Micronaut example](/micronaut-velocity-with-raspberry-pi/). [GitHub](https://github.com/igfasouza/micronaut-velocity-8x8-led-matrix-sense-hat/blob/master/src/main/java/example/micronaut/LedController.java) Or just using [this](https://github.com/cinci/rpi-sense-hat-java).

![](/images/wp/2020/12/PXL_20201223_210745306-300x226.jpg)

![](/images/wp/2020/12/PXL_20201223_210803055-300x260.jpg)

**E-ink display**

![](/images/wp/2020/12/PXL_20201221_1607435032.jpg)

I know that [4tronix](https://shop.4tronix.co.uk/) has some Christmas Micro Bit hats and people did some hack around to use with a Raspberry PI, But If you know any other Christmas Hat, please let me know in the comments.

![](/images/wp/2020/12/Screenshot-2020-12-24-at-12.18.52.png)

As a good developer, I always get confused about Christmas and Halloween as 25 Dec is equal to 31 Oct

**PumpkinPi** <https://thepihut.com/products/halloween-pumpkinpi-for-raspberry-pi>

> Christmas and Halloween
>
> 25 Dec = 31 Oct[@ThePiHut](https://twitter.com/ThePiHut?ref_src=twsrc%5Etfw) [pic.twitter.com/6Tnecmmowp](https://t.co/6Tnecmmowp)
>
> — Igor Souza (@Igfasouza) [November 6, 2019](https://twitter.com/Igfasouza/status/1192185981757263873?ref_src=twsrc%5Etfw)

Some other Christmas ideas  
<https://www.raspberrypi.org/blog/tag/christmas/>
