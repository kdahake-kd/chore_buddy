from django.contrib import admin
from api.models import Task,CalendarEvent
# Register your models here.
admin.site.register(Task)
admin.site.register(CalendarEvent)
