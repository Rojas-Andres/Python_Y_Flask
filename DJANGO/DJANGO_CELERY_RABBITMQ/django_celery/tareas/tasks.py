from celery import shared_task
from django.core.mail import send_mail
# from django_celery.celery import shared_task
from django.contrib.auth.models import User 
from django_celery import settings

#Se ejecuta como tarea
@shared_task
def send_emails_users():
    asunto = 'Mensaje de prueba'
    mensaje = "Bienvenido, esto es un mensaje de prueba CELERY, RABBITMQ Y DJANGO"
    users = User.objects.all()
    for i in users:
        send_mail(asunto, mensaje, settings.EMAIL_HOST_USER, [i.email] ,fail_silently=False)
    return 'Exitoso'
