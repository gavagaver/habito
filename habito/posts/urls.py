from django.contrib import admin
from django.urls import path, include

from posts import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/<str:username>/', views.profile, name='profile'),
]
