## 05/06/2018
### Summary
I built an automatic synchronization of two tables with clicking the button, and then I did some research on Celery, which is a preferred option to handle multi threading of Django. After all the steps of configuration and debugging, it works pretty well.
### Celery Setup
Mostly I followed instruction on **https://realpython.com/asynchronous-tasks-with-django-and-celery/**, except the scheduler.
#### Required version
- Python 2.7.15
- Django 1.8
- Celery 3.1.25
- Redis 2.10.6
- Kombu 3.0.37
#### Configuration
/djangotest/djangotest/celery.py
```python
from __future__ import absolute_import  
import os  
from celery import Celery  
from django.conf import settings  
  
# set the default Django settings module for the 'celery' program.  
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangotest.settings')  
app = Celery('djangotest')  
  
# Using a string here means the worker will not have to  
# pickle the object when using Windows.  
app.config_from_object('django.conf:settings')  
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)  
  
@app.task(bind=True)  
def debug_task(self):  
    print('Request: {0!r}'.format(self.request))
```
/djangotest/djangotest/settings.py
```python
# CELERY STUFF  
BROKER_URL = 'redis://localhost:6379'  
CELERY_RESULT_BACKEND = 'redis://localhost:6379'  
CELERY_ACCEPT_CONTENT = ['application/json']  
CELERY_TASK_SERIALIZER = 'json'  
CELERY_RESULT_SERIALIZER = 'json'  
CELERY_TIMEZONE = 'UTC'  
CELERY_IMPORTS = ("applicationtest.tasks")  
  
from datetime import timedelta  
  
CELERYBEAT_SCHEDULE = {  
    'Sync-every-30-seconds': {  
        'task': 'backgroundSync',  
  'schedule': timedelta(seconds=30),  
  },  
}
```
#### Adding Task
/djangotest/applicationtest/tasks.py
```python
from views import Alteruser, Newuser  
from djangotest.celery import app  
  
@app.task(name='backgroundSync')  
def backgroundSync():  
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
```
#### Use Redis as a Celery "Broker"
Install the Redis from Official website and install redis package in environment
Turn to your terminal, in a new terminal window, fire up the server:
```shell
$ redis-server
```
To test it:
```shell
$ redis-cli ping
> PONG
```
#### RUN IT
**Run them together!**
As the worker open up thread and the beat is in charge of sending pulse command
```
$ celery -A djangotest worker -l info
...
[INFO/MainProcess] Connected to redis://localhost:6379//
[INFO/MainProcess] mingle: searching for neighbors
[INFO/MainProcess] mingle: all alone
```
```
$ celery -A djangotest beat -l info
...
[INFO/MainProcess] beat: Starting...
```
