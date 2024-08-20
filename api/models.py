
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# from django.dispatch import receiver
# from api.notifications import send_task_reminder




class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_tasks')
    deadline = models.DateField(null=True, blank=True)
    priority = models.CharField(max_length=10, choices=(('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')))
    completed = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    progress = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


class CalendarEvent(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='calendar_events')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"{self.task.title} ({self.start_time} - {self.end_time})"





from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Task
# from api.notifications import send_task_notification, send_push_notification
from api.notifications import send_task_notification,send_push_notification

@receiver(post_save, sender=Task)
def task_saved(sender, instance, **kwargs):
    if not instance.completed:
        send_task_notification(instance)
        send_push_notification(instance)





# # @receiver(post_save, sender=Task)
# # def task_notification(sender, instance, created, **kwargs):
# #     if created or not instance.completed:
# #         send_task_reminder(instance)


# # # models.py

# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .notifications import send_task_reminder, send_push_notification

# @receiver(post_save, sender=Task)
# def task_notification(sender, instance, created, **kwargs):
#     if created or not instance.completed:
#         send_task_reminder(instance)
#         user_fcm_token = instance.assigned_to.profile.fcm_token
#         send_push_notification(user_fcm_token, f'Reminder: {instance.title}', f'You have a pending task: {instance.title}')


# # models.py

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     fcm_token = models.CharField(max_length=255, blank=True, null=True)

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#     instance.profile.save()




