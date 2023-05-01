> ### Insert Documents
>> Two ways to insert documents into MongoDB
>>To insert a single document: 
>>
##### First Method: Single Documents using ```InsertOne()```
```commandline
db.posts.insertOne({ email: "kaustubhajgaonkar43@gmail.com",
 subject: "This is a test subject" , > message: "This is a test message",
 date: Date() }) 
```
#### Second Method: Multiple Documents using ```InsertMany()```
```commandline
db.posts.insertMany([
{ email: "test1@gmail.com",
subject: "This is a test subject 1",
message: "This is a test message 1",
date: Date() },
{ email: "test2@gmail.com",
subject: "This is a test subject 2",
message: "This is a test message 2",
date: Date() },
{ email: "test3@gmail.com",
subject: "This is a test subject 3",
message: "This is a test message 3",
date: Date() }
])
```