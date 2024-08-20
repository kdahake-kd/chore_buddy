
# from django.core.mail import send_mail
# from django.conf import settings

# def send_task_reminder(task):
#     subject = f'Reminder: {task.title} is pending'
#     message = f'Dear {task.assigned_to.username},\n\nYou have a pending task: {task.title}. Please complete it by {task.deadline}.\n\nThanks,\nChore Buddy Team'
#     recipient_list = [task.assigned_to.email]
#     send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list)





# from firebase_admin import messaging

# def send_push_notification(token, title, body):
#     message = messaging.Message(
#         notification=messaging.Notification(
#             title=title,
#             body=body,
#         ),
#         token=token,
#     )
#     response = messaging.send(message)
#     print('Successfully sent message:', response)


from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from .models import Task

def send_task_notification(task):
    subject = f"Reminder: Task '{task.title}' is pending"
    html_message = render_to_string('task_notification_email.html', {'task': task})
    plain_message = strip_tags(html_message)
    from_email = settings.DEFAULT_FROM_EMAIL
    to = task.assigned_to.email
    
    send_mail(subject, plain_message, from_email, [to], html_message=html_message)


from push_notifications.models import GCMDevice

def send_push_notification(task):
    devices = GCMDevice.objects.filter(user=task.assigned_to)
    devices.send_message(f"Reminder: Task '{task.title}' is pending", extra={"task_id": task.id})


