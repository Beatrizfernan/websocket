# mqttapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('publish/', views.publish, name='publish'),
    path('subscribe/', views.subscribe, name='subscribe'),
]
