﻿## 30/05/2018
### Summary
I solved the url reverse problem, under help of Charley, which helps me to have a deep insight of the environment of template. I also developed style of my page using bootstrap 3.3.7. Then I got enrolled in another front end development course on EY learning and I'll keep doing research on web.
I started to read legislation reference Alex gave to me, which is **DIV 40** 1-230, 880 and **DIV 43** 1-70 and I'll keep an online document to log my reading.

**New way of url reverse**
```
<a href="{{ url('login') }}"><button class="btn btn-primary btn-block form-container">Login</button></a>
```
**Yesterday Problem Solved**
Create a new file named "jinja.py" under /djangotest/djangotest
```
from django.contrib.staticfiles.storage import staticfiles_storage  
from django.core.urlresolvers import reverse  
from jinja2 import Environment  
  
def environment(**options):  
    env = Environment(**options)  
    env.globals.update({  
        'static': staticfiles_storage.url,  
        'url': reverse,  
    })  
    return env
```
Change the settings.py
YOU have to keep both jinja2 template and Django template as the administration needs to use Django templates
```
TEMPLATES = [  
    {  
        'BACKEND': 'django.template.backends.jinja2.Jinja2',  
        'DIRS': [JINJA_DIR],  
        'APP_DIRS': True,  
        'OPTIONS': {  
            'environment': 'djangotest.jinja.environment'  
        }  
    },  
    {  
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  
        'DIRS': [],  
        'APP_DIRS': True,  
        'OPTIONS': {  
            'context_processors': [  
                'django.template.context_processors.debug',  
                'django.template.context_processors.request',  
                'django.contrib.auth.context_processors.auth',  
                'django.contrib.messages.context_processors.messages',  
            ],  
        },  
    },  
]
```
### Using Bootstrap 3.3.7 to style
```
<!DOCTYPE html>  
<html lang="en">  
<head>  
 <meta charset="UTF-8">  
 <title>REGISTER PAGE</title>  
 <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">  
  
  <!-- Optional theme -->  
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">  
  
  <!-- Latest compiled and minified JavaScript -->  
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>  
  
 <link rel="stylesheet" href="{{ static('css/applicationtest/login.css')}}">  
</head>  
<body>  
 <br> <br> <br> 
 <h2 class="page-title">REGISTER</h2>  
 <br> 
 <form action="register.html" method="post">  
 <div class="form-container">  
     <input type="hidden" name="csrfmiddlewaretoken" value="{{ csrf_token }}">  
     <div class="form-group">  
         <input type="text" class="form-control" placeholder="Enter Username" name="username" required>  
     </div> 
     <div class="form-group">  
         <input type="password" class="form-control" placeholder="Enter Password" name="password" required>  
     </div> 
     <div class="form-group">  
         <input type="text" class="form-control" placeholder="Enter First Name" name="firstname">  
     </div> 
     <div class="form-group">  
         <input type="text" class="form-control" placeholder="Enter Last Name" name="lastname">  
     </div> 
     <div class="form-group">  
         <input type="text" class="form-control" placeholder="Enter Email" name="email">  
     </div> 
     <div class="form-group">  
         <button class="btn btn-primary btn-block" type="submit">Register</button>  
     </div> 
 </div> 
 </form>
 <a href="{{ url('login') }}"><button class="btn btn-primary btn-block form-container">Login</button></a>  
</body>  
</html>
```
