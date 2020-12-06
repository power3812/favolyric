from redis import Redis
from .ranking import Ranking
from .models import Views

ranking = Ranking(Redis(), 'viewranking')
sql = 'select count(id) as view_count, lyric_id from favolyric_views \
where now() > created_at and DATE_ADD(NOW(), INTERVAL - 1 DAY) < created_at \
group by lyric_id order by view desc limit 10;'

view_data = Views.objects.raw(sql)
for data in view_data:
    ranking.push(data['lyric_id'], data['view_count'])

l1 = ranking.gen_list()
print(l1)
