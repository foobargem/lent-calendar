from django.conf.urls import url

from . import views 

urlpatterns = [
    url(r'^latest-version/$', views.latest_version, name="calendar_latest_version"),
    url(r'^events/(?P<code>[0-9]{4}.[0-9]{2})/$', views.events, name="calendar_events"),

    url(r'^$', views.index, name="calendar_index"),
    url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/$',
                views.detail, name="calendar_detail"),

]
