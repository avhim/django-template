from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task(bind=True)
def send_notification_mail(self, msg, target_mail="e.avhim@gmail.com"):
    mail_subject = "Заявка с сайта"
    send_mail(
        subject=mail_subject,
        message=msg,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[target_mail],
        fail_silently=False,
    )
    return f'Email was send to {target_mail}'

def amocrm_webhook(self):
    pass
