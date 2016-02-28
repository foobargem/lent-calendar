import datetime
from rest_framework import viewsets
from rest_framework.response import Response
from calendar.models import Version, Event
from .serializers import VersionSerializer, EventSerializer


class VersionViewSet(viewsets.ViewSet):

    def latest(self, request, format=None):
        year = request.GET.get("year", datetime.date.today().year)
        latest_version = Version.objects.filter(code__startswith=year) \
                                .order_by("-code").first()
        serializer = VersionSerializer(latest_version, many=False)
        return Response(serializer.data)


class EventViewSet(viewsets.ViewSet):

    def list(self, request, code, format=None):
        version = Version.objects.get(code=code)
        events = version.event_set.order_by("date")
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    def detail(self, request, year, month, day, format=None):
        date = datetime.date(int(year), int(month), int(day))
        event = Event.objects.get(date=date)
        serializer = EventSerializer(event, many=False)
        return Response(serializer.data)

