from django.conf.urls import include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from events import views  # , subscription


admin.autodiscover()


urlpatterns = [
    # Examples:
    # url(r'^$', 'jootau.views.home', name='home'),
    # url(r'^jootau/', include('jootau.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^/?$', views.home),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^event/', include('events.urls', namespace="event")),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^accounts/profile/', views.profile_page, name="profile"),
    # url(r'^load-subscription/', subscription.load_subscription, name="subscription"),
]
