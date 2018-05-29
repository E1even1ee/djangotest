from django.shortcuts import render
from applicationtest.models import Newuser
from django.http import HttpResponse
from django.core.urlresolvers import reverse

# Create your views here.
def home(request):
    if request.session.get('has_logged_in', False):
        return render(request, 'applicationtest/dashboard.html')
    else:
        return render(request, 'applicationtest/home.html')

def register(request):
    if request.method == "GET":
        return render(request, 'applicationtest/register.html')
    else:
        newuser = Newuser()
        newuser.username = request.POST.get("username")
        newuser.password = request.POST.get("password")
        newuser.first_name = request.POST.get("firstname")
        newuser.last_name = request.POST.get("lastname")
        newuser.email = request.POST.get("email")
        newuser.save()
        return render(request, 'applicationtest/dashboard.html')

def login(request):
    if request.method == "GET":
        return render(request, 'applicationtest/login.html')
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = Newuser.objects.get(username=username)
        if password == user.password:
            request.session['has_logged_in'] = True
            return render(request, 'applicationtest/dashboard.html')
        else:
            request.method = "GET"
            return render(request, 'applicationtest/home.html')

def logout(request):
    del request.session['has_logged_in']
    return render(request, 'applicationtest/home.html')