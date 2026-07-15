---
layout: post
title: Colaboratory
date: '2018-12-02'
slug: colaboratory
tags:
- Python
description: How’s the craic? We all know that deep learning algorithms improve the
  accuracy of AI applications to a great extent. But this accuracy comes with requiring
  heavy computational processing units such a
image: wp/2018/03/jupyter.png
---

**How’s the craic?**

We all know that deep learning algorithms improve the accuracy of AI applications to a great extent. But this accuracy comes with requiring heavy computational processing units such as GPU for developing deep learning models. Many of the machine learning developers cannot afford GPU as they are very costly and find this as a roadblock for learning and developing Deep learning applications. To help the AI, machine learning developers Google has released a free cloud-based service Google Colaboratory – Jupyter notebook environment with free GPU processing capabilities with no strings attached for using this service. It is ready to use service which requires no set at all.

Any AI developers can use this free service to develop deep learning applications using popular AI libraries like Tensorflow, Pytorch, Keras, etc.

The Colaboratory is a new service that lets you edit and run IPython notebooks right from Google Drive for free! It’s similar to Databricks – give that a try if you’re looking for a better-supported way to run Spark in the cloud, launch clusters, and much more.

**Setting up colab:**

|  |  |
| --- | --- |
| 1 | Go to google drive → new item → More → colaboratory. |

This opens up a python Jupyter notebook in the browser.  
By default, the Jupyter notebook runs on Python 2.7 version and CPU processor. You can change the python version to Python 3.6 and processing capability to GPU by changing the settings as shown below:

|  |  |
| --- | --- |
| 1 | Go to Runtime → Change runtime type |

This opens up a Notebook settings pop-up where we can change Runtime Type to Python 3.6 and processing Hardware to GPU.  
And then your python environment with the processing power of GPU is ready to use.

Google has published some tutorials showing how to use Tensorflow and various other Google APIs and tools on Colaboratory. You can have a look and play around, but for fun, let’s check how to add Spark on this environment.

**Add Apache Spark on colab:**

Under the hood, there’s a full Ubuntu container running on Colaboratory and you’re given root access. This container seems to be recreated once the notebook is idle for a while (maybe a few hours). In any case, this means we can just install Java and Spark and run a local Spark session. Do that by running:

|  |  |
| --- | --- |
| 1 2 3 4 | apt-get install openjdk-8-jdk-headless -qq > /dev/null  wget -q http://apache.osuosl.org/spark/spark-2.2.1/spark-2.2.1-bin-hadoop2.7.tgz  tar xf spark-2.2.1-bin-hadoop2.7.tgz  pip install -q findspark |

Now that Spark is installed, we have to tell Colaboratory where to find it:

|  |  |
| --- | --- |
| 1 2 3 | import os  os.environ["JAVA\_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"  os.environ["SPARK\_HOME"] = "/content/spark-2.2.1-bin-hadoop2.7" |

Finally (only three steps!), start Spark with:

|  |  |
| --- | --- |
| 1 2 3 4 | import findspark  findspark.init()  from pyspark.sql import SparkSession  spark = SparkSession.builder.master("local[\*]").getOrCreate() |

And That’s all – Spark is now running in local mode on a free cloud instance. It’s not very powerful, but it’s a really easy way to get familiar with Spark without installing it locally.

You can have a look in my [post](/jupyter-notebook/) about Jupyter-Notebook for more examples.

**Important things to remember:**

- The supported browsers are Chrome and Firefox.
- Currently, only Python is supported.
- We can you use up to 12 hours of processing time in one go.
