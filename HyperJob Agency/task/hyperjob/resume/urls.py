from django.contrib import admin
from django.urls import path
from .views import Menu, AllResumes, HyperjobSignupView, HyperjobLoginView, Profile, CreateResume
from django.views.generic import RedirectView

urlpatterns = [
    path('', Menu.as_view()),
    path('menu/', Menu.as_view()),
    path('resumes/', AllResumes.as_view()),
    path('signup', HyperjobSignupView.as_view()),
    path('login', HyperjobLoginView.as_view()),
    path('login/', RedirectView.as_view(url='/login')),
    path('signup/', RedirectView.as_view(url='/signup')),
    path('home/', Profile.as_view()),
    path('resume/new', CreateResume.as_view()),
    ]
