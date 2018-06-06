from django.shortcuts import render
from applicationtest.models import Newuser, Alteruser

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
        request.session['has_logged_in'] = True
        return render(request, 'applicationtest/dashboard.html')

def alter(request):
    if request.method == "GET":
        return render(request, 'applicationtest/alter.html')
    else:
        newuser = Alteruser()
        newuser.username = request.POST.get("username")
        newuser.password = request.POST.get("password")
        newuser.first_name = request.POST.get("firstname")
        newuser.last_name = request.POST.get("lastname")
        newuser.email = request.POST.get("email")
        newuser.save()
        request.session['has_logged_in'] = True
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

def sync(request):
    alter_user_list = Alteruser.objects.all()
    for u in alter_user_list:
        if not Newuser.objects.filter(username=u.username).exists():
            new_newuser = Newuser()
            new_newuser.username = u.username
            new_newuser.password = u.password
            new_newuser.email = u.email
            new_newuser.first_name = u.first_name
            new_newuser.last_name = u.last_name
            new_newuser.save()
    new_user_list = Newuser.objects.all()
    for u in new_user_list:
        if not Alteruser.objects.filter(username=u.username).exists():
            new_alteruser = Alteruser()
            new_alteruser.username = u.username
            new_alteruser.password = u.password
            new_alteruser.email = u.email
            new_alteruser.first_name = u.first_name
            new_alteruser.last_name = u.last_name
            new_alteruser.save()
    return render(request, 'applicationtest/synced.html')
