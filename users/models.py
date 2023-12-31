from django.db import models
from django.contrib.auth.models import User, AbstractUser


class WTSUser(AbstractUser):
    company = models.ForeignKey('Company', null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.username


class Company(models.Model):
    name = models.CharField(max_length=256)
    phone = models.CharField(max_length=64, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=256, null=True, blank=True)
    url = models.URLField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'companies'

    def __str__(self):
        return self.name
