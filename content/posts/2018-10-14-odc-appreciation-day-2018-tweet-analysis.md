---
layout: post
title: 'ODC Appreciation Day 2018 : Tweet analysis'
date: '2018-10-14'
slug: odc-appreciation-day-2018-tweet-analysis
tags:
- Python
description: 'How’s the craic? 2018/10/14 Last Thursday was the Oracle Developer Community
  ODC Appreciation Day 2018 #ThanksODC I came across with the #ThanksODC idea Thursday
  afternoon and of course, I join with a'
image: wp/2018/10/oracle-developer-community.png
---

**How’s the craic?**  
2018/10/14

Last Thursday was the Oracle Developer Community ODC Appreciation Day 2018 [#ThanksODC](https://oracle-base.com/blog/2018/09/27/oracle-developer-community-odc-appreciation-day-2018-thanksodc/)

I came across with the #ThanksODC idea Thursday afternoon and of course, I join with a blog post as well. [Here](/odc-appreciation-day-2018-oracle-visual-builder-cloud-and-oracle-jet/)

And you can check the result of #ThanksODC [here](https://oracle-base.com/blog/2018/10/12/odc-appreciation-day-2018-its-a-wrap-thanksodc/)

Today I decided to do my tweets analysis here and see some nice insights.

**But just to clarify.**

- This is my blog, so views expressed here are my own and do not necessarily reflect the views of Oracle and I’m not contesting the result given by oracle-base.
- The idea here is just fun.
- I think I’m the only Brazilian and the only person in Dublin to participate. (Two points that I couldn’t validate)

You can check my old post to see an explanation about the idea and maths behind

> [Six Nations](/six-nations/)

**Let’s check the data.**

I run my script to get the tweets at 12/10/2018 14:00 Dublin time and I got 51 tweets.

13 tweets at 12/10 and 38 at 11/10.  
The first tweet at 11/10 was 08:14:18 and the last one was 23:31:44.  
The last tweet that I got was 12/10 at 12:31:34.

I found 46 links to a blog post  
I found 8 tweets with ODC Appreciation Day 2018

**Counting Terms**

Top 10

[(‘Appreciation’, 31), (‘ODC’, 27), (‘Day’, 25), (‘the’, 19), (‘to’, 17), (‘for’, 14), (‘I’, 11), (‘a’, 11), (‘and’, 10), (‘in’, 9)]

**without Stop-words**

Top 10

[(‘Appreciation’, 32), (‘ODC’, 28), (‘Day’, 26), (‘Oracle’, 9), (‘2018’, 9), (‘Wrap’, 6), (‘posts’, 6), (‘ORDS’, 5), (‘may’, 5), (‘blog’, 5)]

**Languages**

All tweets are in English, but I found six blogs in Spanish.

- <https://plsql-argentina.blogspot.com/2018/10/odc-appreciation-day-muchas-gracias-la.html>
- <https://descubriendooracle.blogspot.com/2018/10/odc-appreciation-day-2018-evangelizando.html?spref=tw>
- <http://oracleparatodos1.blogspot.com/2018/10/odc-appreciation-day-operaciones-online.html>
- <https://edelweissoraclebi.blogspot.com/2018/10/odc-appreciation-day-autonomous-data.html>
- <http://oracleparatodos1.blogspot.com/2018/10/odc-appreciation-day-operaciones-online.html>
- <http://dbaoraclesoporte.blogspot.com/2018/10/odc-apprecitaion-day-2018-sql-tuning.html>

Tweets 100% English  
Blog post 40 English 6 Spanish

**Sentiment Analysis**

Here the API gives a value between -1 and 1.  
-1 to negative, 0 to neutral and 1 to positive.

The result is 88% positive, 11% neutral and 1% negative.

**Retweets**

Top Retweets -> 12  
@oraclebase – ODC Appreciation Day 2018 : It’s a Wrap (#ThanksODC) : https://t.co/RYOeFzyHAs https://t.co/cQsj0N5xVB

**Likes**

Top Likes -> 28  
@HeliFromFinland – Oracle SQL Developer Data Modeler is my favourite tool #ThanksODC https://t.co/ZXr3GI2LXV

**Hashtag**

If we have a look at the most common hashtags, we need to consider that #ThanksODC will be in all tweets because I used as a filter, so we can exclude it from the list. This leaves us with:

2 #ThanksOTN  
2 #oow18  
1 #oracle  
1 #SOASuite  
1 #ThanksOracleBase  
1 #OrclDB  
1 #ThanksTim  
1 #oracleace  
1 #ODCAppreciationDay  
1 #ThanksOTNOTN/ODC  
1 #orclepm  
1 #orclbi  
1 #Terraform  
1 #ThanksTim  
1 #plsql  
1 #sq  
1 #SeeYouAtOpenWorld  
1 #ACED

number of hashtags per tweet

1 tweet with 4 hashtags  
4 tweet with 3 hashtags  
3 tweet with 2 hashtags

number of @

8 @oracleace  
7 @oraclebase  
2 @OracleDevsLA  
2 @connor\_mc\_d  
1 @rickProdManager  
1 @odtug  
1 @OracleDevs  
1 @joelkallman  
1 @OraPubInc  
1 @oravirt  
1 @odevcommunity  
1 @floo\_bar  
1 @oracle  
1 @gwronald  
1 @dhamijarohit  
1 @wordpressdotcom  
1 @FTisiot

number of @ per tweet

2 tweet with 4 @  
3 tweet with 3 @  
1 tweet with 2 @

**Spelling mistakes**

Here I remove all hashtags and I found just one mistake and was “mornging”

**Source**

23 Twitter Web Client  
06 TweetDeck  
05 WordPress.com  
03 Twitter Lite  
03 Twitter for Android  
03 Twitter for iPhone  
01 IFTTT  
02 Tweetbot for Mac  
01 Hootsuite Inc.  
01 Twibble.io  
01 dlvr.it  
01 Tweetbot for iΟS  
01 Twitter Ads Composer

Number of tweets per user

4 LucasBednarek  
3 oraculix  
2 debralilley  
2 RobbieDatabee  
2 Makker\_nl  
2 kibeha  
2 oraclebase  
2 ZedDBA  
2 Igfasouza  
2 amitzil  
1 orana  
1 daanbakboord  
1 orclDBblogs  
1 ITProjectsToday  
1 EdelweissK  
1 signal006  
1 ritan2000  
1 Nikitas\_Xenakis  
1 mathiasmag  
1 simon\_haslam  
1 PeterRaganitsch  
1 HeliFromFinland  
1 gassenmj  
1 FranckPachot  
1 SvenWOracle  
1 opal\_EPM  
1 reguchi\_br  
1 rodrigojorgedba  
1 svilmune  
1 swesley\_perth  
1 dw\_pete  
1 oraesque  
1 RonEkins  
1 connor\_mc\_d  
1 Addidici  
1 dan\_ekb  
1 rittmanmead  
1 FTisiot

My preferred tweet:  
I really should go to sleep 💤, but I’m too busy reading everyone’s #ThanksODC blog posts
