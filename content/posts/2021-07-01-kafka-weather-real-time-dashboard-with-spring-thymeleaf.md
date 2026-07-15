---
layout: post
title: Kafka weather real time dashboard with Spring & Thymeleaf
date: '2021-07-01'
slug: kafka-weather-real-time-dashboard-with-spring-thymeleaf
tags:
- Java
- Kafka
- Raspberry PI
description: How goes the battle? This post is another part of my Kafka weather station
  use case idea. I want to show how I created an app using Spring Boot and Thymeleaf
  to show a real-time dashboard with Sense H
image: wp/2021/07/spring_kafka.jpg
---

![](/images/wp/2021/07/spring_kafka.jpg)

**How goes the battle?**

This post is another part of my Kafka weather station use case [idea](/kafka-weather-station/).

I want to show how I created an app using Spring Boot and Thymeleaf to show a real-time dashboard with Sense Hat temperature data that I read from a Kafka topic. This is another blog about Java on Raspberry PI.

![](/images/wp/2021/07/weather_dashboard01.png)  
Picture 1: The highlighted part of the diagram that this post is focused on.

You can check my [Kafka Producer](/kafka-producer-consumer-overview/) blog and [Kafka at the edge](/kafka-at-the-edge-with-raspberry-pi/) blog, where I explain the Sense Hat producer with Micronaut.

![](/images/wp/2021/07/Kafka_weather_dashboard01.png)  
Picture 2: end-to-end flow

## Idea

A Spring Boot web application where I use Thymeleaf to display a real-time dashboard to show Temperature values that I read from a Kafka topic. I use a Websocket to update the data on the page and Spring Kafka to read the Kafka data.  
The Data came from a Raspberry PI using the Sense Hat.

![](/images/wp/2021/07/spring_weather01.png)  
Picture 3: I added a REST interface for and a @PostConstruct method producing a message

The program is using Spring-Kafka integration and I add a Kafka producer to get the Sense Hat data and I add a REST interface as well to be able to add some data for testing or if I don’t have the Sense Hat running.

## Code

First things first; configuration. There are two ways to configure our Producer and Consumer.  
Option 1: Using application.properties or application.yml  
Option 2: Java class with @Configuration

I’m using option 2 in this example.

|  |  |
| --- | --- |
| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 | @EnableKafka  @Configuration  public class KafkaConsumerConfig {        @Value("$\{kafka.bootstrapserver}")      public [String](http://www.google.com/search?hl=en&q=allinurl%3Adocs.oracle.com+javase+docs+api+string) bootstrapServer;        @Bean      public Map<[String](http://www.google.com/search?hl=en&q=allinurl%3Adocs.oracle.com+javase+docs+api+string),Object> consumerConfigs(){          Map<[String](http://www.google.com/search?hl=en&q=allinurl%3Adocs.oracle.com+javase+docs+api+string),Object> props=new HashMap<[String](http://www.google.com/search?hl=en&q=allinurl%3Adocs.oracle.com+javase+docs+api+string),Object>();          props.put(ConsumerConfig.BOOTSTRAP\_SERVERS\_CONFIG, bootstrapServer);          props.put(ConsumerConfig.KEY\_DESERIALIZER\_CLASS\_CONFIG, StringDeserializer.class);          props.put(ConsumerConfig.VALUE\_DESERIALIZER\_CLASS\_CONFIG, StringDeserializer.class);          props.put(ConsumerConfig.GROUP\_ID\_CONFIG, "temp-groupid.group");          props.put(ConsumerConfig.AUTO\_OFFSET\_RESET\_CONFIG, "latest");            return props;      }        @Bean      public ConsumerFactory<[String](http://www.google.com/search?hl=en&q=allinurl%3Adocs.oracle.com+javase+docs+api+string), String> consumerFactory(){          return new DefaultKafkaConsumerFactory<>(consumerConfigs());      }        @Bean      public KafkaListenerContainerFactory<ConcurrentMessageListenerContainer<[String](http://www.google.com/search?hl=en&q=allinurl%3Adocs.oracle.com+javase+docs+api+string),String>> kafkaListenerContainerFactory(){          ConcurrentKafkaListenerContainerFactory<[String](http://www.google.com/search?hl=en&q=allinurl%3Adocs.oracle.com+javase+docs+api+string), String> factory=new ConcurrentKafkaListenerContainerFactory();          factory.setConsumerFactory(consumerFactory());          return factory;        }  } |

The idea is to use this just to consume, but I added a REST interface for producing a message and a @PostConstruct method in the service to produce Sense Hat data, to be able to test if I don’t have the Sense Hat producer.

I’m using this [Java Wrapper for Raspberry Pi Sense Hat](https://github.com/cinci/rpi-sense-hat-java)

|  |  |
| --- | --- |
| 1 2 3 4 5 6 7 | <dependency>              <groupId>sensehat</groupId>              <artifactId>sensehat</artifactId>              <version>1.0.0</version>              <scope>system</scope>              <systemPath>$\{basedir}/lib/java-executor-1.0-SNAPSHOT.jar</systemPath>          </dependency> |

|  |  |
| --- | --- |
| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 | @PostConstruct      public void init() {          if (senseHat.equals("true")) {              SenseHat senseHat = new SenseHat();              new [Thread](http://www.google.com/search?hl=en&q=allinurl%3Adocs.oracle.com+javase+docs+api+thread)(() -> {                  while (true) {                      sendMessage([Float](http://www.google.com/search?hl=en&q=allinurl%3Adocs.oracle.com+javase+docs+api+float).toString(senseHat.environmentalSensor.getTemperature()));                      try {                          [Thread](http://www.google.com/search?hl=en&q=allinurl%3Adocs.oracle.com+javase+docs+api+thread).sleep(5000);                      } catch ([InterruptedException](http://www.google.com/search?hl=en&q=allinurl%3Adocs.oracle.com+javase+docs+api+interruptedexception) e) {                          e.printStackTrace();                      }                  }              }).start();          }      } |

And I have *kafka.sensehat=true* properties to enable or disable the Sense Hat producer

You can get the full code on my [GitHub](https://github.com/igfasouza/Kafka-Spring-dashboard).

![](/images/wp/2021/07/Screenshot-2021-05-31-at-16.25.44.png)  
Picture 4: The end result

## Kafka

|  |  |
| --- | --- |
| 1 | ./bin/zookeeper-server-start.sh ./config/zookeeper.properties |

|  |  |
| --- | --- |
| 1 | ./bin/kafka-server-start.sh ./config/server.properties |

|  |  |
| --- | --- |
| 1 | ./bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic temperature |

## Links

</what-is-kafka/>

</sense-hat/>

</kafka-weather-station/>

</websockets-vs-server-sent-events/>

</kafka-support-in-spring/>

<https://github.com/igfasouza/Kafka-weather-station>
