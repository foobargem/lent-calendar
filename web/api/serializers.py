from rest_framework import serializers
from calendar.models import Version, Event


class VersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Version
        fields = ('code', 'desc')


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'name', 'date_string', 'season',
                  'verse_title', 'verse_content',
                  'percentage_of_season')


