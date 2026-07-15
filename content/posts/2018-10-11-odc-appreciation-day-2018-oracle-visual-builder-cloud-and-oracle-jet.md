---
layout: post
title: 'ODC Appreciation Day 2018: Oracle Visual Builder Cloud and Oracle JET'
date: '2018-10-11'
slug: odc-appreciation-day-2018-oracle-visual-builder-cloud-and-oracle-jet
tags:
- Oracle
- Oracle JET
- VBCS
description: 'How’s it going horse? 2018/10/11 Today it’s #ThanksODC day and I decide
  to join the idea with a post about VBCS (Oracle Visual Builder Cloud). This post
  idea is going to be divided into three parts; A'
image: wp/2018/10/oracle-developer-community.png
---

![](/images/wp/2018/10/oracle-developer-community.png)

**How’s it going horse?**  
2018/10/11

Today it’s [#ThanksODC](https://oracle-base.com/blog/2018/09/27/oracle-developer-community-odc-appreciation-day-2018-thanksodc/) day and I decide to join the idea with a post about VBCS (Oracle Visual Builder Cloud).

This post idea is going to be divided into three parts;

1. A VBCS step by step Dublin Bus app
2. Oracle JET step by step Dublin Bus app
3. A Comparison of the two projects

## Let’s start.

**Create a Mobile Application**

1. In the web browser, log in to Oracle Visual Builder Cloud Service.
2. On the Visual Applications page, click the New button.

![](/images/wp/2018/10/01-300x48.png)

3. In the Create Application dialog box, enter DublinBus in the Application Name field and Tutorial application in the Description field.
4. The Application ID text field is automatically populated as you type based on the value you enter in Application Name.
5. Click Finish.
6. Click + Mobile Application (or click the + sign at the top of the tab).
7. In the Application name field add DublinBus and in the Navigation Style choose none.

![](/images/wp/2018/10/pic01-300x156.jpg)

8. Go to Service Connections and create a new one, choose “Define by endpoint”

   In the field, URL add **https://data.smartdublin.ie/cgi-bin/rtpi/realtimebusinformation**  
   click next;  
   Go to request and URL Parameters add one query parameters:  
   name: stopid, type: string, default Value: 1071, check as required and click in test and send  
   copy to response body.
9. Create a variable “stopid” as string.
10. Add an input data go in data and change to stopid.
11. Add a button and change the label to “search”.
12. Add a table and choose to add data:  
    choose Service Connections and choose the get for you rest API

    ![](/images/wp/2018/10/pic02-300x178.jpg)

    click on next and choose: route, Duetime and origin for Primary key;  
    next and finish.
13. Create a variable bus and change the type for Array Data Provider.
14. Select the table and go on tab data and change for the variable bus.
15. click on the button search and create an event

    Add “Call REST Endpoint” and choose the get rest API;  
    Add “Reset Variables” and choose bus;  
    Add “Assign Variables” and on the Variables assign the REST to bus;

    ![](/images/wp/2018/10/pic03-300x139.jpg)

> Oracle Visual Builder Cloud Service[#VBCS](https://twitter.com/hashtag/VBCS?src=hash&ref_src=twsrc%5Etfw) [#oracle](https://twitter.com/hashtag/oracle?src=hash&ref_src=twsrc%5Etfw) DublinBus mobile app [pic.twitter.com/5x3fUwlc0S](https://t.co/5x3fUwlc0S)
>
> — Igor Souza (@Igfasouza) [October 11, 2018](https://twitter.com/Igfasouza/status/1050473427402969090?ref_src=twsrc%5Etfw)

I put everything in my [Github](https://github.com/igfasouza/vbcs_dublinbus), so you can get the code and play with.
