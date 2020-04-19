from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.utils.timezone import now

class Temperature (models.Model):

    temp = models.DecimalField(_('Temperature'), max_digits=4, decimal_places=1, blank=False)
    temp_taken_date_time = models.DateTimeField(_("measurement taken on/at"), default=now, blank=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    latitude = models.DecimalField(max_digits=19, decimal_places=16, null=True, blank=True)
    longitude = models.DecimalField(max_digits=19, decimal_places=16, null=True, blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    created_date_time = models.DateTimeField(_("created"), auto_now_add=True)