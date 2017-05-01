from django.contrib import admin
from django.conf.urls import include, url
from . import views
urlpatterns = [
        url(r'^index/', views.index, name='index'),
   		url(r'^(?P<camp_id>[0-9]+)/$', views.detail, name='detail'),
]