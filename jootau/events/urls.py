from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^/?$', views.event_list, name="event_list"),
    url(r'^create/?$', views.entry_form, name="form"),
    url(r'^subscribe/?$', views.subscription, name="subscribe"),
    url(r'^(?P<event_id>.*?)/?$', views.event_page, name='detail'),
]
