### Deletion of Documents

#### deleteOne(): Deleting one document
The deleteOne() method will delete the first document that matches the query provided.
```db.posts.deleteOne({ title: "Post Title 5" })```

#### deleteMany(): Deleting many documents with the query provided
```db.posts.deleteMany({ category: "Technology" })```

