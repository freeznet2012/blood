from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [

        url(r'^register/donor', views.register_donor, name='register_donor'),
        url(r'^register/rrc', views.register_rrc, name='register_rrc'),
        url(r'^register/', views.register, name='register'),
		url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
	    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
	    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    	url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    	url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    	url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
	]