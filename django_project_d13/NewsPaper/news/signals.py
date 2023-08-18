from django.dispatch import receiver
from django.db.models.signals import m2m_changed
from .tasks import task_new_post_message

from .models import *


@receiver(m2m_changed, sender=PostCategory)
def notify_about_new_post(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        categories = instance.categories.all()
        subscribers_emails = []

        for cat in categories:
            subscribers = Subscriber.objects.filter(category=cat)
            subscribers_emails = [subs.user.email for subs in subscribers]

        task_new_post_message.delay(instance.preview(), instance.pk, instance.title, subscribers_emails)
