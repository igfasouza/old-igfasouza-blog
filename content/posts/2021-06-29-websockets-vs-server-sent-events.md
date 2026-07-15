---
layout: post
title: WebSockets VS Server Sent Events
date: '2021-06-29'
slug: websockets-vs-server-sent-events
tags:
- Java
description: 'What’s up? This blog post compares two similar technologies: WebSockets
  (WS) VS Server-Sent Events (SSEs) and is a collection of links, videos and blogs
  that I found mixed with my opinion. Table of co'
image: wp/2021/06/ws_sse01.jpg
---

![](/old-igfasouza-blog/images/wp/2021/06/ws_sse01.jpg)

**What’s up?**

This blog post compares two similar technologies: WebSockets (WS) VS Server-Sent Events (SSEs) and is a collection of links, videos and blogs that I found mixed with my opinion.

Table of contents

1. HTTP/1.1 vs HTTP/2  
2. What is WebSockets  
3. What is Server-Sent Events  
4. Differences  
5. Similarities  
6. Book  
7. Conclusion  
7. Links

## 1. HTTP/1.1 vs HTTP/2

HTTP stands for hypertext transfer protocol, and it is the basis for almost all web applications. More specifically, HTTP is the method computers and servers use to request and send information.

The first usable version of HTTP was created in 1997. Because it went through several stages of development, this first version of HTTP was called HTTP/1.1. This version is still in use on the web. In 2015, a new version of HTTP called HTTP/2 was created.

HTTP/1.1 is an old protocol, it loads requests one by one over a single TCP connection or in parallel over multiple TCP connections to decrease loading times while requiring more resources. As time goes by and web pages become more advanced, the limitations of this protocol are starting to show. This is why HTTP/2 was made, it aims to tackle the limitations set by HTTP/1.1 and be more future-proof.

With HTTP/2, multiple requests can be sent over the same TCP connection with responses arriving out of order. HTTP/2 is a binary protocol, removing security issues and error-proneness that come with text-based protocols. It is backward compatible with earlier versions of the protocol and is compatible with almost all browsers. HTTP/2 also avoids the round trip to the server by having the server intuitively send resources that will be required to render the page. All these advantages eliminate the need for developers to write best practice workarounds to deal with the limitations of older versions of the protocol, they decrease loading times and improve the website infrastructure. This on top of full backward compatibility makes the choice between HTTP/1.1 and HTTP/2 for Server-sent events a no-brainer.

**What is HTTP/3?**

HTTP/3 is the next proposed version of the HTTP protocol. HTTP/3 does not have wide adoption on the web yet, but it is growing in usage. The key difference between HTTP/3 and previous versions of the protocol is that HTTP/3 runs over QUIC instead of TCP. QUIC is a faster and more secure transport layer protocol that is designed for the needs of the modern Internet.

## 2. What is WebSockets

WebSocket is a connection-based communication protocol that is part of the HTML5 specification. The protocol can be applied in web browsers and web servers for enabling the creation of bidirectional connections between client and server named WebSockets. This way, data can be transferred from one to the other and vice versa in real-time. The client and server sides of an application can talk to each other without interruptions since the connection remains open after a server response.

A specific feature of SSEs is that they’re mono-directional, which means that data communication only happens one way, in this case from the server to the client.

## 3. What is Server-Sent Events

The name Server-Sent Events is mostly self-explanatory: it’s a technology standard that allows server-to-client streaming of text-based event data over an HTTP connection. The idea is to have the browser receive data automatically from the server without explicitly having to poll for it.

## 4. Differences

The major difference between WS and SSE is that WS is bidirectional (allowing communication between the client and the server) while SSEs are mono-directional (only allowing the client to receive data from the server).

![](/old-igfasouza-blog/images/wp/2021/06/sse_ws1.jpg)  
Picture 1: The difference between WS and SSE

Another notable difference is the browser compatibility of the two technologies. In this regard, WS has received more attention (and appreciation) than SSEs. More browsers support WS natively than SSEs.

SSEs come with a set of features that WS lack by design, such as automatic reconnection, event IDs and sending arbitrary events. On the other hand, WS can detect a dropped client connection, whereas SSEs first need to send a message before detecting the same issue.

Although WS uses an initial HTTP connection, this connection is updated after a TCP handshake after which data is sent through the WS protocol. This is a more complex protocol than the SSE protocol. Because they’re bidirectional, WS requires more development effort than SSEs, which only need to send an HTTP message with a specific header, whereas a WS needs to establish and maintain a TCP socket communication, as well as a listener socket on the server-side.

![](/old-igfasouza-blog/images/wp/2021/06/Screenshot-2021-06-29-at-11.48.31.png)  
Table 1: The difference between WS and SSE

## 5. Similarities

Both WebSockets and SSEs make use of HTTP connections, however, the main similarity between both is that they push data from the client to the server, a process also known as “server push”.

**Note**: my intention here is not to show that one way is better than the other or to indicate one lib as better than the other. but to show the possible options.

## 6. Books

Data Push Apps with HTML5 SSE by Darren Cook

## 7. Conclusion

They’re not competing technologies, nor is one better than the other. The popularity of WS over SSEs can be explained by the fact that WS has received more attention and appreciation than SSEs, and it’s a fact that more browsers support it natively than they support SSEs.

In the end, whether you should be using WebSockets or SSEs depends on your use case.

## 8. Links

<https://www.digitalocean.com/community/tutorials/http-1-1-vs-http-2-what-s-the-difference>

<https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol>

<https://developer.ibm.com/technologies/web-development/articles/wa-http-server-push-with-websocket-sse/>

<https://en.wikipedia.org/wiki/WebSocket>

<https://en.wikipedia.org/wiki/Server-sent_events>

<https://www.asyncapi.com/blog/websocket-part1>

<https://www.asyncapi.com/blog/websocket-part2>
