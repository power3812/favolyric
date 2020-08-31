
from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from accounts import views
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'favolyric'

urlpatterns = [
    path('',views.input, name='input'),
    path('result/',views.response, name='response'),
    ]
