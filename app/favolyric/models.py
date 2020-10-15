from django.db import models
from django_mysql.models import QuerySet

# Create your models here.

class Views(models.Model):
    lyric_id = models.CharField(max_length = 255, db_index = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = QuerySet.as_manager()
