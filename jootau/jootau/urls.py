from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from Event import views #, subscription

from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jootau.views.home', name='home'),
    # url(r'^jootau/', include('jootau.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
	url(r'^/?$', 'Event.views.Home'),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^event/',include('Event.urls',namespace="event")),
	url(r'^accounts/', include('allauth.urls')),
    url(r'^accounts/profile/', views.profile_page, name="profile"),
    # url(r'^load-subscription/', subscription.load_subscription, name="subscription"),
)

urlpatterns += patterns('django.views.static',
	(r'^%s(?P<path>.*)' % settings.MEDIA_URL, 'serve', {'document_root': settings.MEDIA_ROOT})
)
