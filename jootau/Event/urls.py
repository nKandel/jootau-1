from django.conf.urls import url
from Event import views


urlpatterns = [
		url(r'^/?$', views.event_list, name = "event_list"),
		url(r'^create/?$',views.EntryForm,name="form"),
		url(r'^subscribe/?$',views.Subscription,name="subscribe"),
		url(r'^(?P<event_id>.*?)/?$', views.event_page, name='detail'),
	]