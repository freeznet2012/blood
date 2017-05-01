"""mini URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include, url
from . import views
urlpatterns = [
        url(r'^index/$', views.index, name='search'),
   		url(r'^(?P<rrc_id>[0-9]+)/$', views.detail, name='detail'),


   		url(r'^profile/$', views.home, name='home'),

        url(r'^camps/$', views.camps, name='camps'),
        url(r'^(?P<camp_id>[0-9]+)/$', views.campdetail, name='campdetail'),
        url(r'^camps/edit/(?P<camp_id>[0-9]+)/$', views.campedit, name='campedit'),
        url(r'^camps/delete/(?P<camp_id>[0-9]+)/$', views.campdelete, name='campdelete'),
        url(r'^camps/create/$', views.campcreate, name='campcreate'),

        url(r'^donors/donor/(?P<donor_id>[0-9]+)/$', views.donordetail, name='campdetail'),
        url(r'^donors/$', views.donor, name='search'),





]
