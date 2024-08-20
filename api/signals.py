from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Task, CalendarEvent

@receiver(post_save, sender=Task)
def create_or_update_calendar_event(sender, instance, created, **kwargs):
    if created:
        CalendarEvent.objects.create(task=instance, start_time=instance.deadline, end_time=instance.deadline)
    else:
        calendar_event = CalendarEvent.objects.filter(task=instance).first()
        if calendar_event:
            calendar_event.start_time = instance.deadline
            calendar_event.end_time = instance.deadline
            calendar_event.save()



