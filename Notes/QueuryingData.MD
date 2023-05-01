### Querying the Data:
To query, or filter, data we can include a query in our find() or findOne() methods.
```db.posts.find( {category: "News"} )```

### Projection
Both find methods accept a second parameter called projection.
This parameter is an object that describes which fields to include in the results.

```db.posts.find({}, {title: 1, date: 1})```

We use a 1 to include a field and 0 to exclude a field.
```db.posts.find({}, {_id: 0, title: 1, date: 1})```

Let's exclude the date category field. All other fields will be included in the results.
```db.posts.find({}, {category: 0})```

We will get an error if we try to specify both 0 and 1 in the same object.
```commandline
db.posts.find({}, {title: 1, date: 0})
```
You cannot do the above step since the projection has 1 and 0 in the same object
