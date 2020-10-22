from django.contrib import admin
from django.urls import path
from .views import Menu, AllResumes

urlpatterns = [
    path('', Menu.as_view()),
    path('resumes/', AllResumes.as_view())
    ]