from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Activation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=True)

TEMP_UNIT_CHOICES = (('C', 'Celsius'), ('F', 'Fahrenheit'))

class ExtraInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    temp_unit = models.CharField(_('temperature unit'), max_length=1, choices=TEMP_UNIT_CHOICES, blank=False)
    latitude = models.DecimalField(max_digits=19, decimal_places=16, null=True)
    longitude = models.DecimalField(max_digits=19, decimal_places=16, null=True)
    ip_address = models.GenericIPAddressField(null=True)