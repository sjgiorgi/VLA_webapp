from django.conf.urls import patterns, url
from VLA import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/$', views.about, name='about'),
        url(r'^add_course/$', views.add_course, name="add_course"),
        url(r'^course/(?P<course_name_url>\w+)/$', views.course, name='course'),
        url(r'^course/(?P<course_name_url>\w+)/(?P<lab_name_url>\w+)/$', views.lab, name='lab'),
        url(r'^register/$', views.register, name='register'),
        url(r'^login/$', views.user_login, name='login'),
        url(r'^restricted/$', views.restricted, name='restricted'),
        url(r'^logout/$', views.user_logout, name='logout'),
        url(r'^help/$', views.help, name='help'),
        
        url(r'^help/(?P<vocab_topic_name_url>\w+)/$', views.vocab_topic, name='vocab_topic'),
        url(r'^help/definition/(?P<definition_name_url>\w+)/$', views.definition, name='definition'),
        url(r'^suggest_definition/$', views.suggest_definition, name='suggest_definition'),
        
        
        url(r'^course/(?P<course_name_url>\w+)/(?P<lab_name_url>\w+)/theory/(?P<theory_name_url>\w+)/$', views.theory, name='theory'),
        url(r'^course/(?P<course_name_url>\w+)/(?P<lab_name_url>\w+)/theorytest/(?P<theorytest_name_url>\w+)/$', views.theorytest, name='theorytest'),
        url(r'^course/(?P<course_name_url>\w+)/(?P<lab_name_url>\w+)/simulation/(?P<simulation_name_url>\w+)/$', views.simulation, name='simulation'),
        url(r'^course/(?P<course_name_url>\w+)/(?P<lab_name_url>\w+)/simulationtest/(?P<simulationtest_name_url>\w+)/$', views.simulationtest, name='simulationtest'),
        url(r'^course/(?P<course_name_url>\w+)/(?P<lab_name_url>\w+)/hardware/(?P<hardware_name_url>\w+)/$', views.hardware, name='hardware'),
        url(r'^course/(?P<course_name_url>\w+)/(?P<lab_name_url>\w+)/results/(?P<results_name_url>\w+)/$', views.results, name='results'),
        url(r'^course/(?P<course_name_url>\w+)/(?P<lab_name_url>\w+)/resultsquestions/(?P<resultsquestions_name_url>\w+)/$', views.resultsquestions, name='resultsquestions'),
        )