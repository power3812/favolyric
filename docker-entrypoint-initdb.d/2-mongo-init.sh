mongoimport -u root -p MongoDB2019! --db music --collection lyrics --file /docker-entrypoint-initdb.d/lyrics.json --jsonArray
mongod --auth
