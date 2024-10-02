
from django.urls import path, include
from tracks.views import  home

urlpatterns = [
    path('home',home,name='tracks.home'),
]
