### Find Data:
>There are 2 methods to find and select data from a MongoDB collection, find() and findOne().
To select data from a collection in MongoDB, we can use the find() method.
>
>This method accepts a query object. If left empty, all documents will be returned.
> 
>>find() Method:
>> 
>>To select data from a collection in MongoDB, we can use the find() method. 
>>This method accepts a query object. If left empty, all documents will be returned.
>>>```db.posts.find()```
> 
>> findOne() Method
>> To select only one document, we can use the findOne() method.
>> This method accepts a query object. If left empty, it will return the first document it finds.
>>> ```db.posts.findOne()```

### Querying the Data
> To query, or filter, data we can include a query in our find() or findOne() methods.
>
> ```db.posts.find( {email: "kaustubhajgaonkar43@gmail.com"} )```