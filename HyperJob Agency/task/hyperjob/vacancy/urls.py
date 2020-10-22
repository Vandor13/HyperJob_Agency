from django.contrib import admin
from django.urls import path
from .views import AllVacancies

urlpatterns = [
    path('vacancies/', AllVacancies.as_view())
    ]