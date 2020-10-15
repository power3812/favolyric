for jsonfile in /docker-entrypoint-initdb.d/lyrics/result/*/*.json
do
    mongoimport -u root -p MongoDB2019! --db music --collection lyrics --file "$jsonfile" --jsonArray
done

mongod --auth
