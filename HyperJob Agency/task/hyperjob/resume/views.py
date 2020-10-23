from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .models import Resume
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.shortcuts import redirect
from django.http import HttpResponseForbidden


# Create your views here.
class Menu(View):
    def get(self, request, *args, **kwargs):
        # print("Tschikidi")
        return render(request, 'menu.html')


class AllResumes(View):
    def get(self, request, *args, **kwargs):
        # george = User.objects.create_user("George Newman", "georgenewman@fake.com", "georgepassword")
        # cindy = User.objects.create_user("Cindy Code", "cindycoder@fake.com", "cindypassword")
        # Resume.objects.create(author=george, description="Lead Designer")
        # Resume.objects.create(author=cindy, description="Programmer")
        resumes = Resume.objects.values()
        for resume in resumes:
            # print(resume)
            username = User.objects.get(id=resume["author_id"])
            resume["author"]=username
            # print(username)
        print(resumes)
        return render(request, 'resumes.html', context={'resumes': resumes})


class HyperjobSignupView(CreateView):
    form_class = UserCreationForm
    success_url = 'login'
    template_name = 'signup.html'


class HyperjobLoginView(LoginView):
    form_class = AuthenticationForm
    redirect_authenticated_user = False
    template_name = 'login.html'


class Profile(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            current_user = request.user
            if current_user.is_staff:
                return redirect("/vacancy/new")
            else:
                return redirect("/resume/new")
            # return render(request, 'profile.html', context={"is_staff": str(current_user.is_staff)})
        else:
            return redirect("/login")


class CreateResume(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'create_resume.html')

    def post(self, request, *args, **kwargs):
        print(request.user)
        if request.user and request.user.is_authenticated and not request.user.is_staff:
            description = request.POST.get("description")
            Resume.objects.create(description=description, author=request.user)
            return redirect("/home")
        else:
            return HttpResponseForbidden('<h1>403 Forbidden</h1>', content_type='text/html')
