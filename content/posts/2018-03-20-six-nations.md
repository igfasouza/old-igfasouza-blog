---
layout: post
title: Six Nations
date: '2018-03-20'
slug: six-nations
tags:
- Python
- twitter
description: How heya? Introduction A long time I came collecting Twitter data with
  the idea to sell this in the future or something similar. so I decided to do some
  kind of basic data analyses. I have been thinki
image: wp/2018/03/sixnation.jpg
---

![](/images/wp/2018/03/sixnation.jpg)

**How heya?**

**Introduction**

A long time I came collecting Twitter data with the idea to sell this in the future or something similar. so I decided to do some kind of basic data analyses.  
I have been thinking in do something like this for a while.  
The idea in this post is not to be technical and show all code details, but just tell the story around the data.  
Everything is based on the fact that you can find the codes to do this easily on Google.  
The go here is doing some kind of basic data analyses in a json file with tweets sample.

**Twitter**

For those of you unfamiliar with Twitter, it’s a social network where people post short, 140-character, status messages called tweets. Because tweets are sent out continuously, Twitter is a great way to figure out how people feel about current events.

**Creating a Twitter App**

First, we need to access our Twitter account and create an app. The website to do this is <https://apps.twitter.com>

**The Twitter Streaming API**

In order to make it easy to work with real-time tweets, Twitter provides the [Twitter Streaming API](https://dev.twitter.com/streaming/overview).  
There are a variety of clients for the Twitter Streaming API across all major programming languages. For Python, there are quite a few, which you can find [here](https://dev.twitter.com/resources/twitter-libraries). The most popular is [tweepy](https://github.com/tweepy/tweepy), which allows you to connect to the streaming API and handle errors properly.

**User Case**

I used the Tweepy API to download all the tweets containing the string #rbs6nations during the Saturday, last championship day. Obviously, not all the tweets about the event contained the hashtag and this API get just a part of all tweets that contain the hashtag, but this is a good baseline. The time frame for the download was from around 12:15 PM to 7:15 PM GMT, that is from about 15 minutes before the first match to about 15 minutes after the last match was over. In the end, about 20,000 tweets have been downloaded in JSON format, making about 78Mb of data. This was enough to have some performance problem with my Raspberry Pi Zero. I think is a good size to observe something possibly interesting.

**Six Nations**

As the name suggests, six teams are involved in the competition: England, Ireland, Wales, Scotland, France and Italy. [Six Nations Championship](http://en.wikipedia.org/wiki/Six_Nations_Championship).

**Extracting information**

There are a few fields that will be interesting to us:

- The user’s location (status.user.location). This is the location the user who created the tweet wrote in their biography.
- The screen name of the user (status.user.screen\_name).
- The text of the tweet (status.text).
- The unique id that Twitter assigned to the tweet (status.id\_str).
- When the tweet was sent (status.created\_at).
- How many times the tweet has been retweeted (status.retweet\_count).
- The tweet’s coordinates (status.coordinates). The geographic coordinates from where the tweet was sent.

**Counting Terms**

The first exploratory analysis that we can perform is a simple word count. In this way, we can observe what are the terms most commonly used in the dataset.  
We can easily split the tweets into a list of terms.  
Split by space.

This is the list of top 10 most frequent terms

[(‘ireland’, 3163), (‘england’, 2584), (‘on’, 2271), (‘…’, 2068), (‘day’, 1479), (‘france’, 1380), (‘win’, 1338), (to, 1253), (Grand, 1221), (‘and’, 1180)]

**Stop-Words**

In every language, some words are particularly common. While their use in the language is crucial, they don’t usually convey a particular meaning, especially if taken out of context. This is the case of articles, conjunctions, some adverbs, etc. which are commonly called stop-words. In the example above, we can see three common stop-words “to”, “and” and “on”. Stop-word removal is one important step that should be considered during the pre-processing stages. You can easily find a list of Stop-word for almost all languages in the world.

After removing the list of stop-words, we have a new result:

[(‘ireland’, 3163), (‘england’, 2584), (‘wales’, 2271), (‘day’, 1479), (‘Grand’, 1380), (‘win’, 1338), (‘rugby’, 1253), (‘points’, 1221), (‘title’, 1180), (‘#x2618;’, 1154)]

The #x2618; is an emoji text-based symbol that represents the Irish “Shamrock”. ☘

If we have a look at the most common hashtags, we need to consider that #rbs6nations will be in all tweets becouse I used as a filter, so we can exclude it from the list. This leave us with:

[(‘#engvirl’, 1701), (‘#walvfran’, 927), (‘#rugby’, 880), (‘#itavsco’, 692), (‘#ireland’, 686), (‘#’champions’, 554), (‘#ireland’, 508), (‘#rbs’, 500), (‘#6nation’, 446), (‘#england’, 406)]

We can observe that the most common hashtags, apart from #rugby, are related to the individual matches. In particular England v Ireland has received the highest number of mentions, probably being the last match of the day.

**Detect languages**

Here the idea is to try to detect which language is used in the tweet.

I divide by language and found some Irish. Italian and French tweets.  
Something interesting to notice is that a fair amount of tweets also contained terms in French.  
Apparently, the API did not recognize anything in Welsh and Scottish.

**Co-occurrences**

Sometimes we are interested in the terms that occur together. This is mainly because the context gives us a better insight about the meaning of a term, supporting applications such as word disambiguation or semantic similarity.

I build a co-occurrence matrix such that com [x ][y] contains the number of times the term x has been seen in the same tweet as the term y:

The results:

[((‘6’, ‘nations’), 845), ((‘champions’, ‘ireland’), 760), ((‘nations’, ‘rbs’), 742), ((‘day’, ‘ireland’), 731), ((‘grand’, ‘slam’), 674)]

We could also look for a specific term and extract its most frequent co-occurrences.

The outcome for “ireland”:

[(‘champions’, 756), (‘day’, 727), (‘nations’, 659), (‘england’, 654), (‘2018’, 638), (‘6’, 613), (‘rbs’, 585), (‘ireland’, 559), (‘#x2618;’, 526), (‘game’, 522), (‘win’, 377), (‘grand’, 377), (‘slam’, 377), (’26’, 360), (‘points’, 356), (‘wales’, 355), (‘ire’, 355), (‘title’, 346), (’15’, 301), (‘turn’, 295)]

The outcome for “rugby”:

[(‘day’, 476), (‘game’, 160), (‘ireland’, 143), (‘england’, 132), (‘great’, 105), (‘today’, 104), (‘best’, 97), (‘well’, 90), (‘ever’, 89), (‘incredible’, 87), (‘amazing’, 84), (‘done’, 82), (‘amp’, 71), (‘games’, 66), (‘points’, 64), (‘monumental’, 58), (‘strap’, 56), (‘world’, 55), (‘team’, 55), (‘wales’, 53)]

**Sentiment Analysis**

In order to add another layer to your analysis, you can perform sentiment analysis of the tweets.  
Here the API gives a value between -1 and 1.  
-1 to negative, 0 to neutral and 1 to positive.

The result is 68% positive, 12% neutral and 20% negative.

**Retweet**

Using the status.retweet\_count I was able to create a list of the top 10 re-tweets and get the first one.  
I decide to not put here the first one because was an advertisement for an alcoholic beverage. I let you guess.

And with status.coordinates I get the location of the first one:  
Some of the tweets don’t contain the coordinates because the user can mark as I don’t want to give the location, so I get the most retweeted with location and with Google maps, I discovered that the location was London stadium. This Tweet came from an Android mobile.

**Extract key phrases**

Extract the keywords or phrases which conveys the gist of the meaning of the tweet.

The result was:  
‘Rugby’, ‘Championship’ and ‘Nations’.

**Code**

[Here](http://nbviewer.jupyter.org/gist/karishmadudani/9c5500e124b8e515650c348b42b1d9dc) you can find a Jupyter notebook with almost everything that you need to do something similar.  
You can have a look at [my post](/jupyter-notebook/) to start your jupyter environment

**Under the Hood**

- All codes that I used for this post I found on Google and I basically just make small changes to fit my scenario.
- Just with a little bit of patience, I was able to build some insights about the Six Nations.
- I had the idea to do this blog post on Ireland Storm Emma weekend, but I had problems with energy and internet.
- I did everything using a Raspberry PI Zero and I had performance problems because of the size of the Json file.
- I use [Microsoft cognitive API](https://docs.microsoft.com/en-us/azure/cognitive-services/text-analytics/quickstarts/python) example to do the Sentiment Analysis, Detect languages and to Extract key phrases.
- There are several similar blog post like this with same and/or differences scenarios.

**Conclusion**

Here I showed a simple example of Text Mining on Twitter, using some realistic data taken during a sports event. Using just Google examples, we have downloaded some data using the streaming API, pre-processed the data in JSON format and extracted some interesting terms and hashtags from the tweets.

I also introduced the concept of Counting Terms, Detect Languages, Co-occurrence, Stop-words, Sentiment Analysis, and create some interesting insight.

Now I challenge you to do something similar to your scenario.  
I might accept my challenge and do something like this again. I really liked to do this.  
I might add all code on the GitHub and create a Jupyter notebook as well.  
I might make the jsons file available. Because of the size, I don’t know a place for free hosting!
