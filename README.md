# Summary
感情で音楽推薦アプリ <br>

# Requirement
docker <br>
docker-compose <br>

# Usage
ルートディレクトリで実行 <br>
```bash
docker-compose -f docker-compose.prod.yml down -v
docker-compose -f docker-compose.prod.yml up -d --build
docker-compose -f docker-compose.prod.yml exec django python manage.py makemigrations
docker-compose -f docker-compose.prod.yml exec django python manage.py migrate
docker-compose -f docker-compose.prod.yml exec django python manage.py loaddata init_lyrics.json init_images.json init_artists.json
docker-compose -f docker-compose.prod.yml exec django python manage.py collectstatic --no-input --clear
```

ディレクトリ内で下記を実行し、localhost:1337/api/indexにアクセス <br>
