from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('welcome/', views.welcome),
    path('login/', views.login),
  
    path('register/', views.register),
]
