from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class URL_Table(models.Model):
    long_url = models.URLField(max_length=500)
    custom_name = models.CharField(max_length=50, unique=True)
    # google.com    - Rishabh
    # facebook.com  - Rishabh -> not unique custom_name
    created_date = models.DateField(auto_now_add=True)
    visit_count = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'URL Tables'


class Country(models.Model):
    table = models.ForeignKey('URL_Table', null=True,
                              on_delete=models.CASCADE,
                              )

    country_name = models.CharField(max_length=50)
    country_count = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Country Data'

    def __str__(self):
        return f'{self.country_name}-{self.country_count}'


class Device(models.Model):
    table = models.ForeignKey('URL_Table', null=True,
                              on_delete=models.CASCADE,
                              )

    device_name = models.CharField(max_length=50)
    device_count = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Device Data'

    def __str__(self):
        return f'{self.device_name}-{self.device_count}'


# http://api.ipstack.com/{ipaddress}?access_key=bcfe38a0465bd0cf6319ddf96efdd0e9&format=1
