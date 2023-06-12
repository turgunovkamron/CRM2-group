from django.conf import settings
from django.core.mail import send_mail


def send_email(OTP, email):
    title = 'Hello'
    message = f'One Time Password {OTP}'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [f'{email}']

    send_mail(title, message, from_email, recipient_list)
