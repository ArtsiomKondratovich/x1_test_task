from django.contrib.auth.models import AbstractUser, User
from django.db import models


# Create your models here.


class ShortUrlModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    long_url = models.URLField()
    short_url = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.user} + {self.id}'

    class Meta:
        verbose_name = 'База URL'
