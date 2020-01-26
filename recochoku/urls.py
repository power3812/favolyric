
from django.urls import path
from . import views

app_name = 'recochoku'

urlpatterns = [
        path('',views.input, name='input'),
        path('result/',views.response, name='response')        
    ]