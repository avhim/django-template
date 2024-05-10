from celery import shared_task
from celery.utils.log import get_task_logger
from django.core.mail import send_mail
from django.conf import settings


from .amocrm import amocrm_send_lead

logger = get_task_logger(__name__)


@shared_task(bind=True)
def send_notification_mail(target_mail="unklerufus@gmail.com", msg=None):
    send_mail(
        subject="Заявка с сайта",
        message=msg,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[target_mail],
        fail_silently=False,
    )
    return f'Email was send to {target_mail}'

@shared_task(bind=True)
def send_amocrm(msg=None):
    amocrm_send_lead(msg)
    return f'Lead was send to amocrm'
