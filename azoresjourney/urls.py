"""azoresjourney URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from main import views
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^$', views.index),
    url(r'^pt/$', views.indexPT),
    url(r'^en/$', views.indexEN),
    url(r'^pt/article/(\d{1,4})/$', views.articlesPT),
    url(r'^pt/history/$', views.historyMainPT),
    url(r'^pt/history/island/(\d{1,4})/$', views.historyIslandPT),
    url(r'^pt/history/city/(\d{1,4})/$', views.historyCityPT),
    url(r'^pt/history/location/(\d{1,4})/$', views.historyLocationPT),
    url(r'^pt/search/article/$', views.searchArticlePT),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'media'}),
    url(r'^pt/events/$', views.eventPT),
    url(r'^pt/search/events/$', views.searchEventPT),
    url(r'^pt/event/(\d{1,4})/$', views.eventShowPT),
]
