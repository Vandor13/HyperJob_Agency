from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from .models import Vacancy
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.http import HttpResponseForbidden


# Create your views here.
class AllVacancies(View):
    def get(self, request, *args, **kwargs):
        # george = User.objects.create_user("George 2", "george2@fake.com", "georgepassword")
        # cindy = User.objects.create_user("Cindy 2", "cindy2@fake.com", "cindypassword")
        # Vacancy.objects.create(author=george, description="Level 1 Manager")
        # Vacancy.objects.create(author=cindy, description="Level 2 Architect")
        vacancies = Vacancy.objects.values()
        for vacancy in vacancies:
            # print(resume)
            username = User.objects.get(id=vacancy["author_id"])
            vacancy["author"] = username
            # print(username)
        return render(request, 'vacancies.html', context={'vacancies': vacancies})


class CreateVacancy(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'create_vacancy.html')

    def post(self, request, *args, **kwargs):
        if request.user and request.user.is_staff:
            description = request.POST.get("description")
            Vacancy.objects.create(description=description, author=request.user)
            return redirect("/home")
        else:
            return HttpResponseForbidden('<h1>403 Forbidden</h1>', content_type='text/html')
