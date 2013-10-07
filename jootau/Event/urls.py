from django.conf.urls import patterns, url, include
from Event import views


urlpatterns = patterns('',
		url(r'^/?$', views.event_list, name = "event_list"),
		url(r'^create/?$',views.EntryForm,name="form"),
		url(r'^subscribe/?$',views.Subscription,name="subscribe"),
		url(r'^(?P<event_id>.*?)/?$', views.event_page, name='detail'),

		
	)