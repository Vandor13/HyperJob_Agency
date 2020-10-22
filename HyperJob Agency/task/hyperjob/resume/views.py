from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .models import Resume
from django.contrib.auth.models import User


# Create your views here.
class Menu(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'hyperjob/menu.html')


class AllResumes(View):
    def get(self, request, *args, **kwargs):
        # george = User.objects.create_user("George Newman", "georgenewman@fake.com", "georgepassword")
        # cindy = User.objects.create_user("Cindy Code", "cindycoder@fake.com", "cindypassword")
        # Resume.objects.create(author=george, description="Lead Designer")
        # Resume.objects.create(author=cindy, description="Programmer")
        resumes = Resume.objects.values()
        for resume in resumes:
            #print(resume)
            username = User.objects.get(id=resume["author_id"])
            resume["author"]=username
            #print(username)
        print(resumes)
        return render(request, 'hyperjob/resumes.html', context={'resumes': resumes})
