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
