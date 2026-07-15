---
layout: post
title: Autonomous JSON Database with Java Records and JSON libs – part2
date: '2021-04-26'
slug: autonomous-json-database-with-java-records-and-json-libs-part2
tags:
- Autonomous
- JSON
- Java
description: How’s it going there? After I posted my blog about Autonomous JSON Database
  ADJ and Json libs, some people got to me asking and informing me that we can map
  directly to and from OSON (JSON type) witho
image: wp/2021/04/duke_json02.jpg
---

![](/images/wp/2021/04/ajd.jpg)

**How’s it going there?**

After I posted my blog about [Autonomous JSON Database ADJ and Json libs](/autonomous-json-database-with-java-records-and-json-libs/), some people got to me asking and informing me that we can map directly to and from OSON (JSON type) without having to parser or serialize JSON text, and for that, we can use the “*createDocumentFrom*” method. So I decide to explore this as well.

This is a kind of a continuation from my previous blog where I explored the “*createDocumentFromString*” method, and in this one, I’ll explore the “*createDocumentFrom*” method.

You can check the [Java Doc](http://oracle.github.io/soda-for-java/).

**Note**: my intention here is not to show that one way is better than the other or to indicate one lib as better than the other. but to show the possible options. And as I already demonstrated the result will be the same.

Oracle provides some [examples](https://github.com/oracle/json-in-db/tree/master/SodaExamples/src/main/java/emp), but the idea here is to see how we can use ADJ with Java Records and see all Libs possibilities, and about the topic, I found this [blog series](https://dev.to/cchacin/java-14-records-preview-37om) with a lot of explanations that I suggest you read before checking my examples.

Again I did the test with the most popular JSON libs; JSON-B, Jackson, and Gson.

![](/images/wp/2021/04/json.jpg)  
Picture1: most popular JSON libs

You can check and get the code in my [GitHub](https://github.com/igfasouza/Oracle_AJD_java14).

From the previous example, I just add a new Class Autonomous2 using the new method.

First I updated the yasson version from 1.0.6 to 1.0.8 and with that, I got rid of some [WARNING](https://github.com/quarkusio/quarkus/issues/10803)

|  |  |
| --- | --- |
| 1 2 3 4 5 6 | <dependency>      <groupId>org.eclipse</groupId>      <artifactId>yasson</artifactId>      <version>1.0.8</version>      <scope>test</scope>  </dependency> |

For **JSON-B** I changed the attribute’s names to add get in front.

|  |  |
| --- | --- |
| 1 2 3 4 | @JsonProperty("post code") [String](http://www.google.com/search?hl=en&q=allinurl%3Adocs.oracle.com+javase+docs+api+string) getPostCode,      @JsonProperty("country") [String](http://www.google.com/search?hl=en&q=allinurl%3Adocs.oracle.com+javase+docs+api+string) getCountry,      @JsonProperty("country abbreviation") [String](http://www.google.com/search?hl=en&q=allinurl%3Adocs.oracle.com+javase+docs+api+string) getCountryAbbreviation,      @JsonProperty("places") List<Places> getPlaces) { |

For **Jackson**, I ended up with an ugly switch/case method that I didn’t find a better way to populate the “gen” object.

|  |  |
| --- | --- |
| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 | switch(token) {      case START\_OBJECT:          genJackson.writeStartObject();          break;      case START\_ARRAY:          genJackson.writeStartArray();          break;      case END\_ARRAY:      case END\_OBJECT:          genJackson.writeEnd();          break;      case FIELD\_NAME:          genJackson.writeKey(((com.fasterxml.jackson.core.JsonParser) jacksonParser).currentName());          break;      case VALUE\_FALSE:          genJackson.write(false);          break;      case VALUE\_TRUE:          genJackson.write(true);          break;                      case VALUE\_NULL:          genJackson.writeNull();          break;      case VALUE\_NUMBER\_FLOAT:      case VALUE\_NUMBER\_INT:          genJackson.write(((com.fasterxml.jackson.core.JsonParser)jacksonParser).getDecimalValue());          break;      case VALUE\_STRING:          genJackson.write(((com.fasterxml.jackson.core.JsonParser)jacksonParser).getText());          break;      default:          throw new [IllegalStateException](http://www.google.com/search?hl=en&q=allinurl%3Adocs.oracle.com+javase+docs+api+illegalstateexception)(token.toString());      } |

I checked out the new [Quarkus 1.13.2.Final released – Oracle JDBC driver extension](https://quarkus.io/blog/quarkus-1-13-2-final-released/), bug fixes, and there’s no SODA support.

You can see everything about JDBC [here](https://quarkus.io/guides/datasource) and an example with Oracle [here](https://blogs.oracle.com/developers/configuring-the-oracle-jdbc-drivers-with-quarkus).

![](/images/wp/2021/04/duke_json02.jpg)  
Picture2: Java Duke serialization and deserialization

## Conclusion

- As I demonstrated, all options end up creating the same result.
- Use what is best for your case or whatever you feel more comfortable with.
- Java Records will likely need some JSON-B specification integration but that there is no technical blocker to make it work.
- I had fun and learned a lot about the differences between the JSON libs and how to combine them with Java Records

Don’t forget that now the always Free Oracle Autonomous JSON Database is available, so now is the Action time. Go ahead and try to play around with AJD and check out the Java Records examples.

## Links

<https://docs.oracle.com/en/database/oracle/simple-oracle-document-access/>

<https://github.com/oracle/json-in-db/tree/master/SodaExamples/src/main/java/emp>

<http://oracle.github.io/soda-for-java/>

<https://rmannibucau.metawerx.net/java-14-record-class-type-and-json-b.html>

<https://dev.to/cchacin/java-14-records-with-jakartaee-json-b-160n>

<https://go.oracle.com/LP=105252?elqCampaignId=276940&src1=:so:tw:or:dg:odv:::&SC=:so:tw:or:dg:odv:::&pcode=WWMK201107P00013>
