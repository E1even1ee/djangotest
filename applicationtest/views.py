from django.shortcuts import render
from applicationtest.models import Newuser

# Create your views here.
def home(request):
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
        return render(request, 'applicationtest/home.html')

def login(request):
    if request.method == "GET":
        return render(request, 'applicationtest/login.html')
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = Newuser.objects.get(username=username)
        if password == user.password:
            return render(request, 'applicationtest/home.html')
        else:
            request.method = "GET"
            return render(request, 'applicationtest/login.html')