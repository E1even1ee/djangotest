﻿## 29/05/2018
### Summary
I set up the very first application and created a separate user model on the database. Then I implemented the registration and login functionality, which helped me go through jinja2 templates on how to use url reverse and handle parameters. I also implemented the session to keep user login status. 
### MTV
#### Model trustful steps:
Add application into settings.py Installed_App
Create models in models.py
**admin.site.register(NewModels)** into application/admin.py
python manage.py migrate
Then check database synchronization
#### View URL patterns
Add application url into project urls.py
```
urlpatterns = [
	url(r'^polls/', include('polls.urls')),  
    url(r'^applicationtest/', include('applicationtest.urls')),
    url(r'^admin/', admin.site.urls),  
]
```
### Registration and Log in
```
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
```
#### Using href with Jinja2 template
```
<button><a href="{{ '/applicationtest/login' }}">Login</a></button>
<button onclick="location.href='http://127.0.0.1:8000/applicationtest/login'">Login</button>
```
**Why url_for cannot be working?**

#### Session Implementation
```
def home(request):  
    if request.session.get('has_logged_in', False):  
        return render(request, 'applicationtest/dashboard.html')  
    else:  
        return render(request, 'applicationtest/home.html')

def logout(request):  
    del request.session['has_logged_in']  
    return render(request, 'applicationtest/home.html')
```