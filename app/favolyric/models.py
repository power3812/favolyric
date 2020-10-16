from django.db import models
from django_mysql.models import QuerySet

# Create your models here.

class Views(models.Model):
    id = models.AutoField(primary_key = True)
    lyric_id = models.CharField(max_length = 255, db_index = True)
    created_at = models.DateTimeField(auto_now_add=True, db_index = True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = QuerySet.as_manager()

    class Meta:
        unique_together=(("lyric_id", "created_at"))
