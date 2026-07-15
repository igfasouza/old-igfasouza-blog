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

|  |  |
| --- | --- |
| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 | package example.micronaut;    import java.util.HashMap;  import java.util.Map;    import javax.validation.Valid;    import io.micronaut.http.MediaType;  import io.micronaut.http.annotation.Body;  import io.micronaut.http.annotation.Consumes;  import io.micronaut.http.annotation.Controller;  import io.micronaut.http.annotation.Get;  import io.micronaut.http.annotation.Post;  import io.micronaut.views.View;  import rpi.sensehat.api.SenseHat;  import rpi.sensehat.api.dto.Color;    @Controller("/display")  public class LedController {            SenseHat senseHat = new SenseHat();        @[View](http://www.google.com/search?hl=en&q=allinurl%3Adocs.oracle.com+javase+docs+api+view)("led")      @Get("/create")      public Map<[String](http://www.google.com/search?hl=en&q=allinurl%3Adocs.oracle.com+javase+docs+api+string), Object> create() {          senseHat.ledMatrix.clear();          return createModelWithBlankValues();      }        @[View](http://www.google.com/search?hl=en&q=allinurl%3Adocs.oracle.com+javase+docs+api+view)("led")      @Consumes(MediaType.APPLICATION\_FORM\_URLENCODED)      @Post("/save")      public Map<[String](http://www.google.com/search?hl=en&q=allinurl%3Adocs.oracle.com+javase+docs+api+string), Object> save(@Valid @Body CommandLedSave cmd) {          if(cmd != null) {              if(cmd.getLeds() != null && !cmd.getLeds().equals("")) {                  [String](http://www.google.com/search?hl=en&q=allinurl%3Adocs.oracle.com+javase+docs+api+string) possitions[] = cmd.getLeds().split(",");                  [Color](http://www.google.com/search?hl=en&q=allinurl%3Adocs.oracle.com+javase+docs+api+color)[] pixels = createLedMatrix();                  int i = 0;                  int x = 0;                  int y = 0;                  while (i < possitions.length){                      x = [Integer](http://www.google.com/search?hl=en&q=allinurl%3Adocs.oracle.com+javase+docs+api+integer).parseInt(possitions[i++]);                      y = [Integer](http://www.google.com/search?hl=en&q=allinurl%3Adocs.oracle.com+javase+docs+api+integer).parseInt(possitions[i++]);                      if(x != 0) {                          x = x\*8;                      }                      pixels[x+y] = [Color](http://www.google.com/search?hl=en&q=allinurl%3Adocs.oracle.com+javase+docs+api+color).RED;                                        }                  senseHat.ledMatrix.setPixels(pixels);              }else {                  senseHat.ledMatrix.clear();              }          }            final Map<[String](http://www.google.com/search?hl=en&q=allinurl%3Adocs.oracle.com+javase+docs+api+string), Object> model = new HashMap<>();          model.put("leds", cmd.getLeds());          return model;      }        private Map<[String](http://www.google.com/search?hl=en&q=allinurl%3Adocs.oracle.com+javase+docs+api+string), Object> createModelWithBlankValues() {          final Map<[String](http://www.google.com/search?hl=en&q=allinurl%3Adocs.oracle.com+javase+docs+api+string), Object> model = new HashMap<>();          model.put("title", "");          return model;      }            private [Color](http://www.google.com/search?hl=en&q=allinurl%3Adocs.oracle.com+javase+docs+api+color)[] createLedMatrix() {          [Color](http://www.google.com/search?hl=en&q=allinurl%3Adocs.oracle.com+javase+docs+api+color) off = [Color](http://www.google.com/search?hl=en&q=allinurl%3Adocs.oracle.com+javase+docs+api+color).of(0, 0, 0);          [Color](http://www.google.com/search?hl=en&q=allinurl%3Adocs.oracle.com+javase+docs+api+color)[] pixels = new [Color](http://www.google.com/search?hl=en&q=allinurl%3Adocs.oracle.com+javase+docs+api+color)[64];          for (int i = 0; i < pixels.length; i++) {              pixels[i] = off;          }          return pixels;      }    } |

led.vm

|  |  |
| --- | --- |
| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 | <!DOCTYPE html>  <[html](http://december.com/html/4/element/html.html)>  <[head](http://december.com/html/4/element/head.html)>      <[meta](http://december.com/html/4/element/meta.html) charset="UTF-8">      <[title](http://december.com/html/4/element/title.html)>Micronaut Velocity Sensehat</[title](http://december.com/html/4/element/title.html)>     <[style](http://december.com/html/4/element/style.html)>      body {    background-color: #888889;    color: white;    font-family: sans-serif;  }    h1 {    text-align: center;    font-size: 3em;  }    .base {    display: inline-block;    border: 10px groove gray;     border-right: 10px ridge gray;    border-bottom: 10px ridge gray;    padding: 10px;    background-color: #BBBBBB;    position: absolute;    text-align: center;  }    .matrix {    width: 250px;    height: 240px;    background-color: black;    border: 5px ridge gray;    border-bottom: 5px groove gray;    border-left: 5px groove gray;  }    .led {    cursor:pointer;    display: inline-block;    margin: 5px;    margin-bottom: 0px;    width: 20px;    height: 20px;    border-radius: 10px;    background-color: red;    -webkit-box-shadow: 0px 0px 15px 5px rgba(255, 0, 0, .75);    -moz-box-shadow: 0px 0px 15px 5px rgba(255, 0, 0, .75);    box-shadow: 0px 0px 15px 5px rgba(255, 0, 0, .75);  }    .off{    background-color: #222222;     -webkit-box-shadow: 0px 0px 0px 0px rgba(255, 255, 190, .75);    -moz-box-shadow: 0px 0px 0px 0px rgba(255, 255, 190, .75);    box-shadow: 0px 0px 0px 0px rgba(255, 255, 190, .75);  }    </[style](http://december.com/html/4/element/style.html)>    <[script](http://december.com/html/4/element/script.html)>  function newLine(mat){    var matrix = document.getElementById("matrix");    var line = new Array();    for (var i = 0; i < 8; i++){      var led = document.createElement("div");      led.onclick = function(){onOff(this, mat)};      led.className = "led off";      matrix.appendChild(led);      line[i] = led;    }    return line;  }    function start(mat) {    for (var i = 0; i < 8; i++)      mat[i] = newLine(mat);    return mat;  }    function onOff (led, mat) {    if (led.className == "led off")      led.className = "led";    else       led.className = "led off";          getCoords(mat);    document.getElementById("form\_display").submit();  }    function getCoords (mat) {    var coords = new Array();     for ( var i = 0; i < mat.length; i++)       for ( var j = 0; j < mat[i].length; j++)         if (mat[i][j].className == "led") {          coords.push(i);          coords.push(j);        }    document.getElementById("leds").value = coords;  }    function write (mat,arr) {    var i = 0;    while (i < arr.length){      mat[arr[i++]][arr[i++]].className = "led";    }  }    window.onload = function() {      var mat = new Array();      var mat\_final = start(mat);            var leds = document.getElementById("leds").value;      if (typeof leds !== 'undefined' && leds) {          write(mat\_final,leds.split(","));      }  }    </[script](http://december.com/html/4/element/script.html)>    </[head](http://december.com/html/4/element/head.html)>  <[body](http://december.com/html/4/element/body.html)>  <[h1](http://december.com/html/4/element/h1.html)>Led Display</[h1](http://december.com/html/4/element/h1.html)>  <[form](http://december.com/html/4/element/form.html) action="/display/save" method="post" id="form\_display">        <[input](http://december.com/html/4/element/input.html) type="hidden" id="leds" name="leds" value="$leds" />      <[div](http://december.com/html/4/element/div.html) id="base" class="base">          <[div](http://december.com/html/4/element/div.html) id="matrix" class="matrix"></[div](http://december.com/html/4/element/div.html)>      </[div](http://december.com/html/4/element/div.html)>        </[form](http://december.com/html/4/element/form.html)>    </[body](http://december.com/html/4/element/body.html)>  </[html](http://december.com/html/4/element/html.html)> |

Disclaimer – I got the CSS from [here](https://codepen.io/djan/pen/FIkxC)

You can get the full code on my [GitHub](https://github.com/igfasouza/micronaut-velocity-8x8-led-matrix-sense-hat).

## Links

<https://micronaut.io/>

<https://micronaut-projects.github.io/micronaut-views/latest/guide/>

<http://velocity.apache.org/>

<https://github.com/cinci/rpi-sense-hat-java>
