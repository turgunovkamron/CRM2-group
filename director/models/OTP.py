from django.db import models


class OTP(models.Model):
    key = models.CharField(max_length=1024)
    email = models.CharField(max_length=50)

    is_conf = models.BooleanField(default=False)
    is_expire = models.BooleanField(default=False)
    tries = models.IntegerField(default=0)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.tries >= 3:
            self.is_expire = True
        return super(OTP, self).save(*args, **kwargs)
