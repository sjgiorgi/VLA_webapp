from django.conf.urls import patterns, url
from VLA import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/$', views.about, name='about'),
        url(r'^add_course/$', views.add_course, name="add_course"),
        url(r'^course/(?P<course_name_url>\w+)/$', views.course, name='course'),
        url(r'^course/(?P<course_name_url>\w+)/lab/(?P<lab_name_url>\w+)/$', views.lab, name='lab'),
        url(r'^register/$', views.register, name='register'),
        url(r'^login/$', views.user_login, name='login'),
        url(r'^restricted/$', views.restricted, name='restricted'),
        url(r'^logout/$', views.user_logout, name='logout'),
        url(r'^help/$', views.help, name='help'),
        
        url(r'^course/(?P<course_name_url>\w+)/lab/(?P<lab_name_url>\w+)/theory/(?P<theory_name_url>\w+)/$', views.theory, name='theory'),
        url(r'^course/(?P<course_name_url>\w+)/lab/(?P<lab_name_url>\w+)/pretest/(?P<pretest_name_url>\w+)/$', views.pretest, name='pretest'),
        url(r'^course/(?P<course_name_url>\w+)/lab/(?P<lab_name_url>\w+)/prelab/(?P<prelab_name_url>\w+)$', views.prelab, name='prelab'),
        url(r'^course/(?P<course_name_url>\w+)/lab/(?P<lab_name_url>\w+)/prelabtest/(?P<prelabtest_name_url>\w+)$', views.prelabtest, name='prelabtest'),
        url(r'^course/(?P<course_name_url>\w+)/lab/(?P<lab_name_url>\w+)/hardware/(?P<hardware_name_url>\w+)$', views.hardware, name='hardware'),
        url(r'^course/(?P<course_name_url>\w+)/lab/(?P<lab_name_url>\w+)/results/(?P<results_name_url>\w+)$', views.results, name='results'),
        url(r'^course/(?P<course_name_url>\w+)/lab/(?P<lab_name_url>\w+)/resultsquestions/(?P<resultsquestions_name_url>\w+)$', views.resultsquestions, name='resultsquestions'),
        )