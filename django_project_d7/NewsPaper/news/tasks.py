from celery import shared_task
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives


@shared_task
def task_new_post_message(preview, pk, title, subscribers):
    html_content = render_to_string(
        'post_created_email.html',
        {
            'text': preview,
            'link': f'{settings.SITE_URL}/post/{pk}'
        }
    )

    msg = EmailMultiAlternatives(subject=title,
                                 body='',
                                 from_email=settings.DEFAULT_FROM_EMAIL,
                                 to=[subscribers])

    msg.attach_alternative(html_content, "text/html")
    msg.send()
