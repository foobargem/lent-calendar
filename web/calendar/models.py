from __future__ import unicode_literals

from django.db import models


class Version(models.Model):
    code = models.CharField(max_length=255)
    desc = models.TextField()

    def __unicode__(self):
        return self.code


class Event(models.Model):
    season = models.CharField(max_length=255, default="")
    name = models.CharField(max_length=255)
    date = models.DateField()
    verse_title = models.CharField(max_length=255, default="")
    verse_content = models.TextField(default="")
    version = models.ForeignKey('Version', default=1)

    def __unicode__(self):
        return "%s [%s] - %s" % (self.name, self.date, self.verse_title)

    def percentage_of_season(self):
        events = Event.objects.filter(season=self.season)
        index = map(lambda x: x.date, events).index(self.date) + 1
        return int((float(index) / events.count()) * 100)

    def date_string(self):
        return self.date.strftime("%Y / %m / %d")

