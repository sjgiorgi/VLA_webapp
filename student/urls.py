from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from . import views

urlpatterns = patterns('',
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^profile/(?P<user_name_url>\w+)/$', views.profile, name='profile'),
)
