from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin

admin.autodiscover()

# Root patterns
urlpatterns = patterns('',
    url(r'^redactor/upload/$', 'redactor.views.upload', name='redactor-upload'),
    url(r'^redactor/images/$', 'redactor.views.images', name='redactor-images'),
)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
