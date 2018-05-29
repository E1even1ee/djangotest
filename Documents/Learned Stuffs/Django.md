# Django
## Basic Structure
```
-djangoproject
	-djangoproject
		_init_.py
		settings.py
		urls.py
		wsgi.py
	-application_1
		-migrations
		_init_.py
		admin.py
		models.py
		tests.py
		urls.py
		views.py
	-statics
		-images
		-css
		-javascript
	-templates
		-application_1
			index.html
			login.html
			register.html
	manage.py
```
```
$ python manage.py runserver
```
/djangoproject/djangoproject/urls.py
```
from django.conf.urls import include, url  
from django.contrib import admin

urlpatterns = [   
    url(r'^application_1/', include('application_1.urls')),  
    url(r'^admin/', admin.site.urls),  
]
```
/djangoproject/application_1/urls.py
```
from django.conf.urls import url  
from . import views  
  
urlpatterns = [  
	url(r'^$', views.index, name='index')
]
```
/djangoproject/application_1/views.py
```
def index(request):
	my_dict = {'Whatever Key': 'Contents value'}
    return render(request, 'application_1/index.html', context=my_dict)
```
Within index.html, you can use **{{'Whatever Key'}}** to access the value
### Set template path
/djangoproject/djangoproject/settings.py
```
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")  
STATIC_DIR = os.path.join(BASE_DIR, "static")

TEMPLATES = [  
    {  
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  
        'DIRS': [TEMPLATES_DIR],
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
### Static contents quick access
```
STATIC_URL = '/static/'
STATICFILES_DIRS = [
	STATIC_DIR,
]
```
Within HTML
```
<img src="{% static "images/***.jpg" %}">
<link rel="stylesheet" href={% static "css/mystyle.css"%}/>
```
## Model
### Two methods to process schema
#### 1. Using CMD
```
python manage.py migrate
python manage.py makemigrations application_1
python manage.py migrate
```
#### 2. Press Ctrl+Alt+r
```
migrate
makemigrations application_1
migrate
```
### Create model
/djangoproject/application_1/models.py
```
from django.db import models

class Topic(models.Model):
	top_name = models.CharField(max_length=264, unique=True)
	def __str__(self):
		return self.top_name
```
Running in shell CMD
```
python manage.py shell
from application_1.models import Topic
print(Topic.objects.all())

t = Topic(top_name="ABC")
t.save()
print(Topic.objects.all())
```
djangoproject/application_1/admin.py
```
from application_1 import Topic
admin.site.register(Topic)
```
### MTV Pattern
### Django Forms

### Questions
#### Question 1 `__str__` or `__unicode__`?
Should I care about the __unicode__ thing and what's this function for
```
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __unicode__(self):
        return u'%s  %s' % (self.first_name, self.last_name)
```
#### Question 2 migrate and makemigrations
Why the schema in the database could not be changed when running **makemigrations**, and I have to drop the table and create it again via **migrate**
