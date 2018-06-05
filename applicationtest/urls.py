from django.conf.urls import url
from applicationtest import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url('register/', views.register, name='register'),
    url('alter/', views.alter, name='alter'),
    url('login/', views.login, name='login'),
    url('logout/', views.logout, name='logout'),
    url('sync/', views.sync, name='sync'),
]