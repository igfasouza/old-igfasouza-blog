---
layout: post
title: Micronaut Velocity with Raspberry PI
date: '2020-09-29'
slug: micronaut-velocity-with-raspberry-pi
tags:
- Java
- Micronaut
- Raspberry PI
description: How’s the lad? This post is to show how I created a Micronaut Velocity
  demo with a Raspberry PI. This is another blog about Java on Raspberry PI. Micronaut
  is a JVM-based framework for building lightw
image: wp/2020/09/raspberry_micronaut.jpg
---

![](/images/wp/2020/09/raspberry_micronaut.jpg)

**How’s the lad?**

This post is to show how I created a Micronaut Velocity demo with a Raspberry PI. This is another blog about Java on Raspberry PI.

Micronaut is a JVM-based framework for building lightweight, modular applications. Developed by OCI, the same company that created Grails, Micronaut is the latest framework designed to make creating microservices quick and easy.

One of the most exciting features of Micronaut is its compile time dependency injection mechanism. Most frameworks use reflection and proxies to perform dependency injection at runtime. Micronaut, however, builds its dependency injection data at compile time. The result is a faster application startup and smaller memory footprints.

Although Micronaut is primarily designed around message encoding/decoding there are occasions where it is convenient to render a view on the server-side. The views module provides support for view rendering on the server-side and does so by rendering views on the I/O thread pool in order to avoid blocking the Netty event loop.

<https://micronaut-projects.github.io/micronaut-views/latest/guide/>

Velocity is a Java-based template engine. It permits anyone to use a simple yet powerful template language to reference objects defined in Java code.

<http://velocity.apache.org/>

You can check my blog post about sense hat [here](/sense-hat/)

## Idea

I started with the idea to do something similar with my [Quarkus Qute 7 segment display demo](/quarkus-qute-with-raspberry-pi/), using Micronaut, but I pivoted a little bit. I end up with a Micronaut Vecolcity interface that provides a way to control the 8×8 Led Matrix from SenseHat.

![](/images/wp/2020/09/IMG-20200928-WA0001.jpg)

I used this [Java wrapper for Sense Hat](https://github.com/cinci/rpi-sense-hat-java)

## Code

LedController.java

```java
package example.micronaut;
import java.util.HashMap;
import java.util.Map;
import javax.validation.Valid;
import io.micronaut.http.MediaType;
import io.micronaut.http.annotation.Body;
import io.micronaut.http.annotation.Consumes;
import io.micronaut.http.annotation.Controller;
import io.micronaut.http.annotation.Get;
import io.micronaut.http.annotation.Post;
import io.micronaut.views.View;
import rpi.sensehat.api.SenseHat;
import rpi.sensehat.api.dto.Color;
@Controller("/display")
public class LedController {

    SenseHat senseHat = new SenseHat();
    @View("led")
    @Get("/create")
    public Map<String, Object> create() {
        senseHat.ledMatrix.clear();
        return createModelWithBlankValues();
    }
    @View("led")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Post("/save")
    public Map<String, Object> save(@Valid @Body CommandLedSave cmd) {
        if(cmd != null) {
            if(cmd.getLeds() != null && !cmd.getLeds().equals("")) {
                String possitions[] = cmd.getLeds().split(",");
                Color[] pixels = createLedMatrix();
                int i = 0;
                int x = 0;
                int y = 0;
                while (i < possitions.length){
                    x = Integer.parseInt(possitions[i++]);
                    y = Integer.parseInt(possitions[i++]);
                    if(x != 0) {
                        x = x*8;
                    }
                    pixels[x+y] = Color.RED;

                }
                senseHat.ledMatrix.setPixels(pixels);
            }else {
                senseHat.ledMatrix.clear();
            }
        }
        final Map<String, Object> model = new HashMap<>();
        model.put("leds", cmd.getLeds());
        return model;
    }
    private Map<String, Object> createModelWithBlankValues() {
        final Map<String, Object> model = new HashMap<>();
        model.put("title", "");
        return model;
    }

    private Color[] createLedMatrix() {
        Color off = Color.of(0, 0, 0);
        Color[] pixels = new Color[64];
        for (int i = 0; i < pixels.length; i++) {
            pixels[i] = off;
        }
        return pixels;
    }
}
```

led.vm

```html
<!DOCTYPE html>
<[html](http://december.com/html/4/element/html.html)>
<[head](http://december.com/html/4/element/head.html)>
    <[meta](http://december.com/html/4/element/meta.html) charset="UTF-8">
    <[title](http://december.com/html/4/element/title.html)>Micronaut Velocity Sensehat</[title](http://december.com/html/4/element/title.html)>
 <[style](http://december.com/html/4/element/style.html)>
    body {
  background-color: #888889;
  color: white;
  font-family: sans-serif;
}
h1 {
  text-align: center;
  font-size: 3em;
}
.base {
  display: inline-block;
  border: 10px groove gray;
  border-right: 10px ridge gray;
  border-bottom: 10px ridge gray;
  padding: 10px;
  background-color: #BBBBBB;
  position: absolute;
  text-align: center;
}
.matrix {
  width: 250px;
  height: 240px;
  background-color: black;
  border: 5px ridge gray;
  border-bottom: 5px groove gray;
  border-left: 5px groove gray;
}
.led {
  cursor:pointer;
  display: inline-block;
  margin: 5px;
  margin-bottom: 0px;
  width: 20px;
  height: 20px;
  border-radius: 10px;
  background-color: red;
  -webkit-box-shadow: 0px 0px 15px 5px rgba(255, 0, 0, .75);
  -moz-box-shadow: 0px 0px 15px 5px rgba(255, 0, 0, .75);
  box-shadow: 0px 0px 15px 5px rgba(255, 0, 0, .75);
}
.off{
  background-color: #222222;
   -webkit-box-shadow: 0px 0px 0px 0px rgba(255, 255, 190, .75);
  -moz-box-shadow: 0px 0px 0px 0px rgba(255, 255, 190, .75);
  box-shadow: 0px 0px 0px 0px rgba(255, 255, 190, .75);
}
  </[style](http://december.com/html/4/element/style.html)>
<[script](http://december.com/html/4/element/script.html)>
function newLine(mat){
  var matrix = document.getElementById("matrix");
  var line = new Array();
  for (var i = 0; i < 8; i++){
   var led = document.createElement("div");
   led.onclick = function(){onOff(this, mat)};
   led.className = "led off";
   matrix.appendChild(led);
   line[i] = led;
 }
 return line;
}
function start(mat) {
 for (var i = 0; i < 8; i++)
   mat[i] = newLine(mat);
 return mat;
}
function onOff (led, mat) {
 if (led.className == "led off")
   led.className = "led";
 else
   led.className = "led off";

 getCoords(mat);
 document.getElementById("form_display").submit();
}
function getCoords (mat) {
 var coords = new Array();
 for ( var i = 0; i < mat.length; i++)
   for ( var j = 0; j < mat[i].length; j++)
     if (mat[i][j].className == "led") {
       coords.push(i);
       coords.push(j);
     }
 document.getElementById("leds").value = coords;
}
function write (mat,arr) {
 var i = 0;
 while (i < arr.length){
   mat[arr[i++]][arr[i++]].className = "led";
 }
}
window.onload = function() {
    var mat = new Array();
    var mat_final = start(mat);

    var leds = document.getElementById("leds").value;
    if (typeof leds !== 'undefined' && leds) {
        write(mat_final,leds.split(","));
    }
}
</[script](http://december.com/html/4/element/script.html)>
</[head](http://december.com/html/4/element/head.html)>
<[body](http://december.com/html/4/element/body.html)>
<[h1](http://december.com/html/4/element/h1.html)>Led Display</[h1](http://december.com/html/4/element/h1.html)>
<[form](http://december.com/html/4/element/form.html) action="/display/save" method="post" id="form_display">
    <[input](http://december.com/html/4/element/input.html) type="hidden" id="leds" name="leds" value="$leds" />
    <[div](http://december.com/html/4/element/div.html) id="base" class="base">
        <[div](http://december.com/html/4/element/div.html) id="matrix" class="matrix"></[div](http://december.com/html/4/element/div.html)>
    </[div](http://december.com/html/4/element/div.html)>

</[form](http://december.com/html/4/element/form.html)>
</[body](http://december.com/html/4/element/body.html)>
</[html](http://december.com/html/4/element/html.html)>
```

Disclaimer – I got the CSS from [here](https://codepen.io/djan/pen/FIkxC)

You can get the full code on my [GitHub](https://github.com/igfasouza/micronaut-velocity-8x8-led-matrix-sense-hat).

## Links

<https://micronaut.io/>

<https://micronaut-projects.github.io/micronaut-views/latest/guide/>

<http://velocity.apache.org/>

<https://github.com/cinci/rpi-sense-hat-java>
