from django.conf.urls import url
from applicationtest import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url('register/', views.register, name='register'),
    url('login/', views.login, name='login'),
    url('logout/', views.logout, name='logout')
]