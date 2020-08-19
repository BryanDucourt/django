from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from login import views

urlpatterns = [
    path('/login', views.login),
    path('/register', views.register),
]