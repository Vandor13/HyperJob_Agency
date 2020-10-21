from django.contrib import admin
from django.urls import path
from .views import Menu

urlpatterns = [
    path('', Menu.as_view()),
    ]