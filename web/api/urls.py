from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .viewsets import VersionViewSet, EventViewSet

urlpatterns = [

    url(r'^latest-version/$',
            VersionViewSet.as_view({ 'get': 'latest' }),
            name="api_version_latest"),

    url(r'^(?P<code>[0-9]{4}.[0-9]{2})/events/$', 
            EventViewSet.as_view({ 'get': 'list' }),
            name="api_event_list"),

    url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/event/$',
            EventViewSet.as_view({ 'get': 'detail' }),
            name="api_event_detail"),

]

urlpatterns = format_suffix_patterns(urlpatterns)
