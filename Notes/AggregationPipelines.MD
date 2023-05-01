### Aggregation Pipelines
Aggregation operations allow you to group, sort, perform calculations, analyze data, and much more.

Aggregation pipelines can have one or more "stages". The order of these stages are important. Each stage acts upon the results of the previous stage.

```commandline
db.posts.aggregate([
  // Stage 1: Only find documents that have more than 1 like
  {
    $match: { likes: { $gt: 1 } }
  },
  // Stage 2: Group documents by category and sum each categories likes
  {
    $group: { _id: "$category", totalLikes: { $sum: "$likes" } }
  }
])
```

### Aggregation ```$group```
This aggregation stage groups documents by the unique _id expression provided.

Don't confuse this _id expression with the _id ObjectId provided to each document.
```commandline
db.listingsAndReviews.aggregate(
    [ { $group : { _id : "$property_type" } } ]
)
```
This will return property type field

### Aggregation ```$limit```
This aggregation stage limits the number of documents passed to the next stage.

In this example, we are using the "sample_mflix" database loaded from our sample data in the Intro to Aggregations section
```db.movies.aggregate([ { $limit: 1 } ])```

This will return the 1 movie from the collection.