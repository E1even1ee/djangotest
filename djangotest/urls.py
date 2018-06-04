from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    #url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^polls/', include('polls.urls')),
    url(r'^applicationtest/', include('applicationtest.urls')),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
