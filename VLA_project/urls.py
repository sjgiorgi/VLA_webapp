from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
admin.autodiscover()
from . import views

urlpatterns = patterns('',
    url(r'^$', 'VLA_project.views.home', name='home'),
    url(r'^VLA/', include('VLA.urls')),
    url(r'^vla/', include('VLA.urls')),
    url(r'^help/', include('tutor.urls')),
    url(r'^student/', include('student.urls')),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
