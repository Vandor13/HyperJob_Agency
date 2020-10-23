from django.contrib import admin
from django.urls import path
from .views import AllVacancies, CreateVacancy

urlpatterns = [
    path('vacancies/', AllVacancies.as_view()),
    path('vacancy/new', CreateVacancy.as_view()),
    ]