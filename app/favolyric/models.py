from django.db import models
from django_mysql.models import QuerySet

# Create your models here.

class Lyrics(models.Model):
    id             = models.AutoField(primary_key = True)
    title          = models.CharField(max_length = 255, db_index = True)
    artist_id      = models.IntegerField(db_index = True)
    image_id       = models.IntegerField(db_index = True)
    itunes_link    = models.CharField(max_length = 255, db_index = True)
    happy          = models.FloatField(db_index = True)
    sad            = models.FloatField(db_index = True)
    angry          = models.FloatField(db_index = True)
    disgust        = models.FloatField(db_index = True)
    surprise       = models.FloatField(db_index = True)
    fear           = models.FloatField(db_index = True)
    created_at     = models.DateTimeField(auto_now_add = True, null = True)
    updated_at     = models.DateTimeField(auto_now = True, null = True)

    objects = QuerySet.as_manager()

    class Meta:
        unique_together=(("title", "artist_id"))

class Artists(models.Model):
    id         = models.AutoField(primary_key = True)
    name       = models.CharField(max_length = 255, db_index = True, unique = True)
    created_at = models.DateTimeField(auto_now_add = True, null = True)
    updated_at = models.DateTimeField(auto_now = True, null = True)

    objects = QuerySet.as_manager()

class Images(models.Model):
    id         = models.AutoField(primary_key = True)
    url        = models.CharField(max_length = 255, db_index = True, unique = True)
    created_at = models.DateTimeField(auto_now_add = True, null = True)
    updated_at = models.DateTimeField(auto_now = True, null = True)

    objects = QuerySet.as_manager()

class Views(models.Model):
    id         = models.AutoField(primary_key = True)
    lyric_id   = models.IntegerField(db_index = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = QuerySet.as_manager()

    class Meta:
        unique_together=(("lyric_id", "created_at"))
