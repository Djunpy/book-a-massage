from celery import shared_task
from django.core.mail import send_mail

from .models import Booking, Comment
from django_website.settings import EMAIL_HOST_USER

@shared_task
def send_feedback_email_task(booking_id):
    """Задача отправки email - при успешной записи к массажисту."""
    instance = Booking.objects.get(id=booking_id)

    email = instance.email
    username = instance.username
    the_date = instance.the_date
    the_time = instance.the_time
    subject = f'Запись к массажисту'
    message = f'Добрый день, {username} вы забронировали время массажа на {the_date} в {the_time}'
    mail_send = send_mail(subject,
                          message,
                          EMAIL_HOST_USER,
                          [email])
    return mail_send


@shared_task
def send_comment_task(comment_id):
    instance = Comment.objects.get(id=comment_id)
    email = instance.email
    name = instance.name
    massage = instance.massage
    subject = f'Вы оставили комментарий к записи {massage.name}'
    message = f'Спасибо за комментарий, нам важно ваш фитбек!'
    mail_send = send_mail(subject,
                          message,
                          EMAIL_HOST_USER,
                          [email])
    return mail_send