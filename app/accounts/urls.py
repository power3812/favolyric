from django.conf.urls import include
from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from accounts import views
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.top, name='top'),
    path('create', views.create, name='create'),
    path('login', views.login, name='login'),
    #path('logout', views.logout, name='logout'),
    path('auth/', include('social_django.urls', namespace='social')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #url(r'^logout/$', logout, {'template_name': 'index.html'}, name='logout'),
    ]
