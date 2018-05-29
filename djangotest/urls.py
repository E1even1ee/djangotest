from django.conf.urls import include, url
from django.contrib import admin
urlpatterns = [
    #url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^polls/', include('polls.urls')),
    url(r'^applicationtest/', include('applicationtest.urls')),
    url(r'^admin/', admin.site.urls),
]

