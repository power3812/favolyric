var user = {
  user: "root",
  pwd: "MongoDB2019!",
  roles: [
    {
      role: "dbOwner",
      db: "music"
    }
  ]
};

db.createUser(user);
db.createCollection('lyrics');
db.lyrics.createIndex({title: 1, artist: 1}, {unique: true, dropDups: true});
