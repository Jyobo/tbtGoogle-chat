from django.conf.urls import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('chat.views',
    url(r'^/$', 'base'),
    url(r'^/messages/$', 'messages'),
    # Examples:
    # url(r'^$', 'Google.views.home', name='home'),
    # url(r'^Google/', include('Google.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    )