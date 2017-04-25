from __future__ import unicode_literals

from django.db import models

# Create your models here.
class urls(models.Model):
    Url_corta = models.CharField(max_length=500)
    Url_larga = models.CharField(max_length=500)
