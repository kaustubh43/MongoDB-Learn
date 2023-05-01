# Update Document
>To update an existing document we can use the updateOne() or updateMany() methods.

>The first parameter is a query object to define which document or documents should be updated.

>The second parameter is an object defining the updated data.

First we need to find a post ```db.posts.find( { title: "Post Title 1" } )```

Let's update the likes to 2.
```db.posts.updateOne( { title: "Post Title 1" }, { $set: { likes: 2 } } ) ```

### Insert if not found
If you would like to insert the document if it is not found, you can use the upsert option.
```commandline
db.posts.updateOne( 
  { title: "Post Title 5" }, 
  {
    $set: 
      {
        title: "Post Title 5",
        body: "Body of post.",
        category: "Event",
        likes: 5,
        tags: ["news", "events"],
        date: Date()
      }
  }, 
  { upsert: true }
)
```

### Update many using updateMany()
Update likes on all documents by 1. For this we will use the $inc (increment) operator:
``db.posts.updateMany({}, { $inc: { likes: 1 } })``

### Update one specific: Increment Likes
```db.posts.updateOne( { title: "Post Title 1" }, { $inc: { likes: 1 } } ) ```
This updates a likes of specific post title by one