# Generated by Django 4.2.1 on 2023-06-07 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('director', '0002_remove_otp_phone_otp_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='surname',
        ),
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
