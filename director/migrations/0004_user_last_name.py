# Generated by Django 4.2.1 on 2023-06-09 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('director', '0003_remove_user_surname_remove_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]