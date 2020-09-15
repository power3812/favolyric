from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from accounts import views
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    path('create', views.create_account, name='accounts/create.html'),
    path('login', views.account_login, name='accounts/login.html'),
    #url(r'^logout/$', logout, {'template_name': 'index.html'}, name='logout'),
    ]
