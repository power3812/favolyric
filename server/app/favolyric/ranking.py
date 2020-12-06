from datetime import timedelta
from django.db import connection, transaction
from .models import Views
from redis import Redis

cursor = connection.cursor()
sql = 'select count(id) as view_count, lyric_id from favolyric_views \
where now() > created_at and DATE_ADD(NOW(), INTERVAL - 1 DAY) < created_at \
group by lyric_id order by view_count desc limit 10;'
cursor.execute(sql)
rows = cursor.fetchall()

redis = Redis(host='redis', port=6379, password='redis2019!', db=0)

if rows != None:
    view_data = list(rows)
else:
    view_data = rows
print(view_data)
dict = {}
for data in view_data:
    dict[data[1]] = data[0]

redis.zadd('ranking', dict)
a = list(redis.zrangebyscore('ranking', '-inf', '+inf'))
print(a[0].decode())
