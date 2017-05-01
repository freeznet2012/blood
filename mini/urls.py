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
from account import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('home.urls')),
	url(r'^rrc/', include('rrc.urls')),
    url(r'^donor/', include('donor.urls')),
    url(r'^request/', include('request.urls')),
    url(r'^camp/', include('camp.urls')),
    url(r'^accounts/', include('account.urls')),
 #   url(r'^account/register/donor', views.register_donor, name='register_donor'),
    url(r'^account/register/rrc', views.register_rrc, name='register_rrc'),
    url(r'^account/', include('account.urls')),

]
