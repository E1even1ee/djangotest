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