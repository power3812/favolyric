from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from accounts import views
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.urls import include, path
from .views import *

app_name = 'favolyric'

urlpatterns = [
    path('index/',views.index, name='index'),
    path('result/',views.result, name='result'),
]
