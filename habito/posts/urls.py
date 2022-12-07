from django.contrib import admin
from django.urls import path, include

from posts import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
]
