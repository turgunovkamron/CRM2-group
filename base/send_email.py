from django.core.mail import send_mail


def send_email(OTP, email):
    subject = 'Hello'
    message = f'Sekretniy kod (OTP) {OTP}'
    from_email = 'djangoproject32@gmail.com'
    recipient_list = [f'{email}']

    send_mail(subject, message, from_email, recipient_list)


