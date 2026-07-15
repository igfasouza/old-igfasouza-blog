---
layout: post
title: Jupyter Notebook
date: '2018-03-09'
slug: jupyter-notebook
tags:
- Python
- Jupyter
description: How’s it going there? Jupyter Notebook is a popular application that
  enables you to edit, run and share Python code into a web view. It allows you to
  modify and re-execute parts of your code in a very
image: wp/2018/03/jupyter.png
---

![](/old-igfasouza-blog/images/wp/2018/03/jupyter.png)

**How’s it going there?**

[Jupyter Notebook](http://jupyter.org/) is a popular application that enables you to edit, run and share Python code into a web view. It allows you to modify and re-execute parts of your code in a very flexible way. That’s why Jupyter is a great tool to test and prototype programs.

[Apache Spark](http://spark.apache.org/) is a fast and powerful framework that provides an API to perform massively distributed processing over resilient sets of data.

Get Started with Spark and Jupyter together.

Install Spark

visit the [Spark downloads page](http://spark.apache.org/downloads.html). Select the latest Spark release, a prebuilt package for Hadoop, and download it directly.  
Unzip it and move it to your /opt folder:

```bash
$ tar -xzf spark-1.2.0-bin-hadoop2.4.tgz
$ mv spark-1.2.0-bin-hadoop2.4 /opt/spark-1.2.0
```

Create a symbolic link:

```bash
$ ln -s /opt/spark-1.2.0 /opt/spark
```

This way, you will be able to download and use multiple Spark versions.

Finally, tell your bash (or zsh, etc.) where to find Spark. To do so, configure your $PATH variables by adding the following lines in your ~/.bashrc (or~/.zshrc) file:

```bash
$ export SPARK_HOME=/opt/spark
$ export PATH=$SPARK_HOME/bin:$PATH
```

Install Jupyter

```bash
$ pip install jupyter
```

You can run a regular jupyter notebook by typing:

```bash
$ jupyter notebook
```

There are two ways to get PySpark available in a Jupyter Notebook:

1 – Configure PySpark driver to use Jupyter Notebook: running pyspark will automatically open a Jupyter Notebook  
2 – Load a regular Jupyter Notebook and load PySpark using findSpark package

**Option 1:**

Update PySpark driver environment variables: add these lines to your~/.bashrc (or ~/.zshrc) file.

```bash
$ export PYSPARK_DRIVER_PYTHON=jupyter
$ export PYSPARK_DRIVER_PYTHON_OPTS='notebook'
```

Restart your terminal and launch PySpark again:

```bash
$ pyspark
```

Now, this command should start a Jupyter Notebook in your web browser. Create a new notebook by clicking on ‘New’ > ‘Notebooks Python [default]’.

**Option 2:**

Use findSpark package to make a Spark Context available in your code.

findSpark package is not specific to Jupyter Notebook, you can use this trick in your favorite IDE too.  
To install findspark:

```bash
$ pip install findspark
```

Launch a regular Jupyter Notebook:

```bash
$ jupyter notebook
```

In your python code you need to add:

```
import findspark
findspark.init(“/path_to_spark”)
```

Now you can try out and see. I hope this guide will help you easily get started with Jupyter and Spark

Here is a python code example to test:

```python
import findspark
findspark.init(“/opt/spark-1.4.1-bin-hadoop2.6/”)
import pyspark
import random
sc = pyspark.SparkContext(appName="Pi")
num_samples = 100000000
def inside(p):
 x, y = random.random(), random.random()
 return x*x + y*y < 1
count = sc.parallelize(range(0, num_samples)).filter(inside).count()
pi = 4 * count / num_samples
print(pi)
sc.stop()
```

[Apache Toree](https://toree.incubator.apache.org/) is a kernel for the Jupyter Notebook platform providing interactive access to Apache Spark.

Install Toree.

```bash
$ sudo pip install toree
```

Configure

Set SPARK\_HOME to point to the directory where you downloaded and expanded the Spark binaries.

```bash
$ SPARK_HOME=$HOME/Downloads/spark-x.x.x-bin-hadoopx.x
$ jupyter toree install \
  --spark_home=$SPARK_HOME
```

Start notebook.

```bash
$ jupyter notebook
```

Test

Point browser to http://localhost:8888.  
Then open a new notebook using New > Toree.

Test notebook with simple Spark Scala code.

```
sc.parallelize(1 to 100).
  filter(x => x % 2 == 0).
  map(x => x * x).
  take(10)
```

Here you can use tab for auto-complete.

To run Jupyter with R  
Install IRkernel

```bash
$ conda install -c r ipython-notebook r-irkernel
```

You can now open R and Install some necessary packages used by R kernel on ipython notebook

```
install.packages(c('rzmq','repr','IRkernel','IRdisplay'), repos = 'http://irkernel.github.io/', type = 'source')
```

After the packages are successfully downloaded and installed.  
Type this and quit

```
IRkernel::installspec()
quit()
```

Start the notebook and check new -> R

You can install Jupyter on Raspberry Pi

```bash
$ apt-get install python3-matplotlib
$ apt-get install python3-scipy
$ pip3 install --upgrade pip
$ reboot
$ sudo pip3 install jupyter
```

To start

```bash
$ jupyter-notebook
```

Simple Python example:

```
import pyspark
sc = pyspark.SparkContext('local[*]')
# do something to prove it works
rdd = sc.parallelize(range(1000))
rdd.takeSample(False, 5)
```

Simple R example:

```
library(SparkR)
as <- sparkR.session("local[*]")
# do something to prove it works
df <- as.DataFrame(iris)
head(filter(df, df$Petal_Width > 0.2))
```

Simple Scala example:

```
[val](http://scala-lang.org) rdd = sc.parallelize(0 to 999)
rdd.takeSample([false](http://scala-lang.org), 5)
```

Use the pre-configured SparkContext in variable sc.

**Links**

Apache Torre  
<https://github.com/asimjalis/apache-toree-quickstart>

R on Jupyter  
<https://discuss.analyticsvidhya.com/t/how-to-run-r-on-jupyter-ipython-notebooks/5512/2>
