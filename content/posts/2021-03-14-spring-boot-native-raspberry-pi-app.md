---
layout: post
title: Spring Boot Native Raspberry PI app
date: '2021-03-14'
slug: spring-boot-native-raspberry-pi-app
tags:
- Java
- Spring Boot
- Raspberry PI
description: Story Horse? All good in the hood? 2021/03/14 Happy PI day with another
  blog about Raspberry PI, It’s kind of a continuation from my previous blog. Control
  your house lights in a smart way and check o
image: wp/2021/03/spring-native-pi.jpg
---

![](/images/wp/2021/03/spring-native-pi.jpg)

**Story Horse? All good in the hood?**  
2021/03/14

Happy PI day with another blog about Raspberry PI, It’s kind of a continuation from my previous [blog](/energy-switch-and-smart-home-with-kafka/).  
Control your house lights in a smart way and check out your energy consumption.

Spring just [announced](https://spring.io/blog/2021/03/11/announcing-spring-native-beta) that they’ve launched the beta release of [Spring Native](https://github.com/spring-projects-experimental/spring-native) and its availability on [start.spring.io](https://start.spring.io/).

I saw this on Friday just after I published my blog about a [Spring web app to simulate a lamp switch using the TP-link smart bulb and smart plug.](/energy-switch-and-smart-home-with-kafka/)

So today I decided to just get my demo and make it native. Check it out on my [GitHub](https://github.com/igfasouza/spring-switch).

Just need to install GraalVM on Raspberry PI, and you can follow it [here](https://github.com/dongjinleekr/graalvm-ce-deb).

Just use the GraalVm Docker [image](https://www.graalvm.org/docs/getting-started/container-images/)

![](/images/wp/2021/03/spring-native.jpg)

Today is PI Day and Mother’s Day, and nothing cooler than having a blog about both at the same time.

![](/images/wp/2021/03/PXL_20210314_1144183732-1024x851.jpg)  
Raspberry PI motherboard – Happy Mother’s Day and Pi Day all.

I want to add an honorable mention here for my friend [Rodrigo Rodrigues](https://www.linkedin.com/in/%F0%9F%91%A8%E2%80%8D%F0%9F%92%BB-%F0%9F%87%AE%F0%9F%87%AA-rodrigo-rodrigues-a08aab15/) that helped me to activate this and gave me moral support to make this blog.

Check out his similar example [here](https://github.com/rodrigorodrigues/spring-native-crud-mongodb).

## Links

<https://www.graalvm.org/docs/getting-started/container-images/>

<https://github.com/dongjinleekr/graalvm-ce-deb>

<https://github.com/marketplace/actions/setup-graalvm-ce>

<https://hub.docker.com/_/openjdk>

<https://medium.com/agorapulse-stories/how-to-deploy-java-application-with-docker-and-graalvm-464629d95dbd>

<https://medium.com/graalvm/updates-on-class-initialization-in-graalvm-native-image-generation-c61faca461f7>
