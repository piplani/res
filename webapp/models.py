# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .validators import validate_file_extension
from django.db import models

# Create your models here.


class data(models.Model):
    file = models.FileField(validators=[validate_file_extension])
    email = models.EmailField()

    def __str__(self):
        return str(self.id) + ":" + str(self.email)


class status(models.Model):
    status_id = models.IntegerField()
    status = models.BooleanField(default=False)
    activity_score = models.CharField(default='', max_length=10)
    potency = models.CharField(default='', max_length=10)
    efficacy = models.CharField(default='', max_length=10)

    def __str__(self):
        return str(self.status_id)