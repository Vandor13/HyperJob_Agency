from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View


# Create your views here.
class Menu(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'hyperjob/menu.html')
