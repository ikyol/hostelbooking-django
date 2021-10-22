from celery import shared_task
from book.celery import app
from django.core.mail import send_mail


@app.task
def send_success_email(user_email):
    send(user_email)


def send(user_email):
    send_mail('Добро пожаловать', "Вы успешно зарегистрировались!!! Congratulations!!!", 'Hostelbooking@gmail.com',
              [user_email, ],
              fail_silently=False)
