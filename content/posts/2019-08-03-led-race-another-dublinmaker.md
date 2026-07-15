---
layout: post
title: Led Race – Another DublinMaker
date: '2019-08-03'
slug: led-race-another-dublinmaker
tags:
- Maker
- Python
- Raspberry PI
description: Hey you! Last week 20th July was the Dublin Maker 2019. So, let’s start
  with an explanation about what is Dublin Maker. Dublin Maker is a free to attend,
  community run event, which was held on Saturda
image: wp/2019/08/IMG_20190721_084104.jpg
---

![](/images/wp/2019/08/IMG_20190721_084104-768x1024.jpg)

**Hey you!**

Last week 20th July was the [Dublin Maker](http://www.dublinmaker.ie/) 2019.

So, let’s start with an explanation about what is Dublin Maker.

Dublin Maker is a free to attend, community run event, which was held on Saturday, July 20th, 2019 in Merrion Square. Dublin Maker takes the form of a “show and tells” experience where inventors/makers sourced through an open call, to have an opportunity to showcase their creations in a carnival atmosphere. It is a family friendly showcase of invention, creativity and resourcefulness, and a celebration of the maker movement. It’s a place where people show what they are making and share what they are learning.

If you have science interested kids, or you’re a kid yourself, this is a great event with lots of interesting open people and things that at least some of them you’ll probably not get the chance to see again.

I have been attending the event for a long time now, and today I want to explain the project that I presented this year. [The Open Led Race](https://create.arduino.cc/projecthub/gbarbarov/open-led-race-a0331a). Back in March I was on holidays and I saw one tweet from Arduino about the project and I said to myself, it’s exactly what I’m going to show on Dublin Maker.

My first concern was about using an arcade button, because the idea is to let a lot of kids to play, I was afraid that they would break the button fast and I need to replace fast as well because a lot of people came to see the project.  
After few days looking at the instructions and the components I had the idea to change the arcade button to MakeyMakey and because of that I decided to create the idea using a Raspberry PI to simplify the idea.

Apparent I’m the first one to do it.

![](/images/wp/2019/08/20190721_231703-840x1024.jpg)

The project is really simple. I’m using the WS2813 led strip and using the [API](https://github.com/jgarff/rpi_ws281x) that I found on the internet.

[Python library wrapping](https://github.com/rpi-ws281x/rpi-ws281x-python) for the rpi-ws281x library

You can check my [GitHub](https://github.com/igfasouza/Open_Led_Race_pi) to see the full code.

It’s basically a Python code that runs on the Raspberry Pi that controls the Led Strip and the MakeyMakey that I used to simulate one keyboard. Every click I move the led 3 positions forward.  
The makeymakey part is just one aluminium foil and play-doh.

I used the GPIO 10 (pin 19) and 18 (pin 12) for LED\_PIN and LED\_DMA and GPIO 9 (pin 6) for Ground.

![](/images/wp/2019/08/20190801_181128-1024x768.jpg)

I created a simple version of the Led Race, but there are lots of space for improvement.

I came with some ideas that one day I’ll implement;

- Add a monitor where I can show a timer and the best lap timer;
- I can show a speedometer or something like the number of push per second;
- I can display the best lap overall;
- four players put for cars at the same time;

Other ideas are some things that I saw on the Open Led Races Arduino web site and the comments, like;

- Add velocity;
- Add some physics when the car goes up, more push is needed, or increase the speed when going down;
- Add a second Led Strip and then the car can go left and right and they can leave some kind of weapons on the track, and the car gets stuck there if hits for fill push;

> [#DublinMaker](https://twitter.com/hashtag/DublinMaker?src=hash&ref_src=twsrc%5Etfw)[#OpenLedRace](https://twitter.com/hashtag/OpenLedRace?src=hash&ref_src=twsrc%5Etfw) with Raspbery and Makeymakey[@openledrace](https://twitter.com/openledrace?ref_src=twsrc%5Etfw)[@Raspberry\_Pi](https://twitter.com/Raspberry_Pi?ref_src=twsrc%5Etfw)[@makeymakey](https://twitter.com/makeymakey?ref_src=twsrc%5Etfw) [pic.twitter.com/FVz0W6acMs](https://t.co/FVz0W6acMs)
>
> — Igor Souza (@Igfasouza) [July 20, 2019](https://twitter.com/Igfasouza/status/1152694837638041607?ref_src=twsrc%5Etfw)

> Tomorrow[#DublinMaker](https://twitter.com/hashtag/DublinMaker?src=hash&ref_src=twsrc%5Etfw) "Led Race" with [#RaspberryPi](https://twitter.com/hashtag/RaspberryPi?src=hash&ref_src=twsrc%5Etfw) and [#makeymakey](https://twitter.com/hashtag/makeymakey?src=hash&ref_src=twsrc%5Etfw)[@Raspberry\_Pi](https://twitter.com/Raspberry_Pi?ref_src=twsrc%5Etfw) [@makeymakey](https://twitter.com/makeymakey?ref_src=twsrc%5Etfw) [@DublinMaker](https://twitter.com/DublinMaker?ref_src=twsrc%5Etfw) [pic.twitter.com/SsItKdbqgx](https://t.co/SsItKdbqgx)
>
> — Igor Souza (@Igfasouza) [July 19, 2019](https://twitter.com/Igfasouza/status/1152313986152587264?ref_src=twsrc%5Etfw)

I want to add here a big thanks to [Elaine Akemi](https://www.linkedin.com/in/elaineakemi/) who helped me with the project. She is also my official partner of Hackathons and events, and she was with me in the last two Dublin Maker editions.
