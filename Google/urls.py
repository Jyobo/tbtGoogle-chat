from django.conf.urls import *
from chat.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('chat.views',
	('^hello/$', hello),
    ('^$', base),
    (r'^login/$', login_user),
    (r'^messages/$', messages),
    (r'^accounts/', include('registration.backends.default.urls')),
    # Examples:
    # url(r'^$', 'Google.views.home', name='home'),
    # url(r'^Google/', include('Google.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    )
