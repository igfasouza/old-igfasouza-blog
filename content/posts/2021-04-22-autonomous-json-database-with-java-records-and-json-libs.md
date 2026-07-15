---
layout: post
title: Autonomous JSON Database with Java Records and JSON libs
date: '2021-04-22'
slug: autonomous-json-database-with-java-records-and-json-libs
tags:
- Autonomous
- JSON
- Java
description: How heya? Since I saw the launching of the Autonomous JSON Database (AJD)
  I was wondering if it is possible to use Java Records and how it would be the Serializing
  and Deserializing JSON part. Picture
image: wp/2021/04/duke_json01.jpg
---

![](/old-igfasouza-blog/images/wp/2021/04/ajd.jpg)

**How heya?**

Since I saw the [launching of the Autonomous JSON Database](https://blogs.oracle.com/jsondb/autonomous-json-database) (AJD) I was wondering if it is possible to use Java Records and how it would be the Serializing and Deserializing JSON part.

![](/old-igfasouza-blog/images/wp/2021/04/create_ajdgif.gif)  
Picture1: Simplified animation showing basic steps to create an AJD instance

Recently Oracle [announced the Free AJD](https://blogs.oracle.com/developers/oracle-cloud-adds-free-apex-and-json-services) and I decided to put my test in a blog. You can check the AJD details [here](https://www.oracle.com/autonomous-database/autonomous-json-database/).

Everything started here, when I saw [this documentation](https://docs.oracle.com/en/database/oracle/simple-oracle-document-access/java/adsda/using-soda-java.html#GUID-EF1551B4-A06A-42CB-B472-D692AF1D9CDC) to get started and I saw that to create a new document you should send a string.

```
// Create a JSON document.
OracleDocument doc = db.createDocumentFromString("{ "name" : "Alexander" }");
```

Then I was thinking what is the best way to Serialize and Deserialize an Object to JSON and if it is possible to use Java Records?

JDK 14 introduces records, which are a new kind of type declaration. Like an enum, a record is a restricted form of a class. It’s ideal for “plain data carriers,” classes that contain data not meant to be altered, and only the most fundamental methods such as constructors and accessors. The important difference between class and record is that a record aims to eliminate all the boilerplate code needed to set and get the data from an instance. Records transfer this responsibility to the Java compiler which generates the constructor, field getters, hashCode() and equals() as well toString() methods.

Yes, it is possible to use Records, but the most important thing here is how to Serialize and Deserialize an Object to JSON?  
And for that, we need to check what are the JSON libs options?

![](/old-igfasouza-blog/images/wp/2021/04/json.jpg)  
Picture2: most popular JSON libs

In actuality, plenty of libraries already exist that can format objects into JSON. So I decided to create a test and compare the most popular JSON libs; JSON-B, Jackson, and Gson.

[JSON-B](https://jakarta.ee/specifications/jsonb/) is a Jakarta EE specification that provides an API for transforming JSON to Java objects (and back again).

[FasterXML Jackson](https://github.com/FasterXML/jackson) is not an implementation of the JSON-B specification but provides similar mapping functionality between JSON and Java objects. The detailed mapping behavior of Jackson and JSON-B implementations differs.

[Gson](https://github.com/google/gson) is a Java library that can be used to convert Java Objects into their JSON representation. It can also be used to convert a JSON string to an equivalent Java object. Gson can work with arbitrary Java objects including pre-existing objects that you do not have a source code of.

![](/old-igfasouza-blog/images/wp/2021/04/micropofile-1024x380.jpg)  
Picture3: Jakarta EE VS Microprofile

I did search for the Microprofile JSON specification and I didn’t find anything specific, and it looks like they follow the JSOB-B idea. (If you know something here, please leave a comment)

Before the release of JSON-B (which arrived as part of Java EE 8), JSON-P was Java EE’s standardized way to interact with JSON. [JSON-P](https://openliberty.io/docs/21.0.0.3/json-p-b.html) is a lower-level API that provides two models (streaming and object) for JSON processing and transformation.

[Eclipse Yasson](https://eclipse-ee4j.github.io/yasson/) is the reference implementation

```xml
<dependency>
    <groupId>org.eclipse</groupId>
    <artifactId>yasson</artifactId>
    <version>1.0.6</version>
    <scope>test</scope>
</dependency>
```

I just add the maven dependency and I had to add the ***@JsonbCreator*** annotation on the Location constructor

There are other implementations as well;

- [Wildfly](https://www.wildfly.org/) (23.0.0.Final)
- [Payara](https://www.payara.fish/) (5.2021.1)
- [OpenLiberty](https://openliberty.io/) (21.0.0.3)
- [Quarkus](https://quarkus.io/) (1.13.2.Final)
- [Helidon](https://helidon.io/#/) (2.2.2)

**For Jackson**

```xml
<dependency>
    <groupId>com.fasterxml.jackson.core</groupId>
    <artifactId>jackson-databind</artifactId>
    <version>2.12.0</version>
</dependency>
```

I just add

```
final ObjectMapper mapper = new ObjectMapper()
      .enable(SerializationFeature.INDENT_OUTPUT);
```

**For Gson**

```xml
<dependency>
       <groupId>com.google.code.gson</groupId>
       <artifactId>gson</artifactId>
       <version>2.3.1</version>
   </dependency>
```

I just override the to String method.

```java
@Override
public String toString() {
Gson gson = new Gson();
       return gson.toJson(this);
}
```

You can check and get the code in my [GitHub](https://github.com/igfasouza/Oracle_AJD_java14).

The main point in the code is that these lines give the same result.

```
OracleDocument doc = db.createDocumentFromString(la.toString());
OracleDocument doc = db.createDocumentFromString(laAPI.toString());
OracleDocument doc = db.createDocumentFromString(laJackson.toString());
OracleDocument doc = db.createDocumentFromString(jsonb.toString());
```

I also added a test where I compare the objects and the JSON to validate that they are equal.

![](/old-igfasouza-blog/images/wp/2021/04/duke_json01.jpg)  
Picture4: Java Duke serialization and deserialization

I saw that [Quarkus](https://quarkus.io/blog/quarkus-1-13-2-final-released/) released the Oracle JDBC driver extension recently, and people started to ask what is special about this extension and if this extension supports SODA or not?

I don’t have implementation details of this extension and I didn’t have time to test, but on Quarkus you can choose between JSON-B or Jackson and as I demonstrated in my test it will work and will generate the same result. (let me know in the comments if you did any tests and if there is a difference?)

```xml
<dependency>
    <groupId>io.quarkus</groupId>
    <artifactId>quarkus-resteasy-jackson</artifactId>
</dependency>
<dependency>
    <groupId>io.quarkus</groupId>
    <artifactId>quarkus-resteasy-jsonb</artifactId>
</dependency>
```

If you getting confused and not knowing which implementation you are using you can find out which implementation is used, it is sufficient to inspect the package name of the following class:

```
JsonbBuilder.create().getClass()
```

## Conclusions

We can use records to serialize and deserialize JSON.  
We can use any JSON lib API and the result will be the same.

## Links

<http://oracle.github.io/soda-for-java/>

<https://docs.oracle.com/en/cloud/paas/autonomous-json-database/ajdug/java-application.html#GUID-6B2610C1-120C-46F0-876C-E7D871CEC267>

<https://docs.oracle.com/cd/E56351_01/doc.30/e58124/soda_for_java.htm#ADSDA144>

<https://docs.oracle.com/en/java/javase/14/language/records.html>

<https://javaee.github.io/jsonb-spec/users-guide.html>

<https://javaee.github.io/jsonp/>

<https://blogs.oracle.com/datawarehousing/autonomous-database-newsletter-august-20-2020>
