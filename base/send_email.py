from django.core.mail import send_mail


def send_email():
    subject = 'Hello'
    message = f'Sekretniy kod (OTP) 43256789'
    from_email = 'djangoproject32@gmail.com'
    recipient_list = ['kamronbekturgunov8@gmail.com']

    send_mail(subject, message, from_email, recipient_list)


