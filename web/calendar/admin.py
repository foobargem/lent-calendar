from django.contrib import admin
from .models import Version, Event


class VersionAdmin(admin.ModelAdmin):
        pass
admin.site.register(Version, VersionAdmin)

class EventAdmin(admin.ModelAdmin):
        pass
admin.site.register(Event, EventAdmin)

