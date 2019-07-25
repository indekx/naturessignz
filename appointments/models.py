from random import choices

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

class BookAppointment(models.Model):
    # Title Hint
    TITLE = (
        ( '', 'select' ),
        ('SIR', 'Sir'),
        ('MR', 'Mr'),
        ('MRS', 'Mrs'),
        ('MS', 'Ms'),
        ('NONE', 'None'),
    )

    GENDER = (
        ('', 'choose'),
        ('M', 'Male'),
        ('F', 'Female'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=None, on_delete=models.CASCADE)
    title = models.CharField(choices=TITLE, default='select', blank=False, max_length=20)
    full_name = models.CharField(blank=False, max_length=60)
    email = models.EmailField(blank=False)
    gender = models.CharField(choices=GENDER, default='chose', blank=False, max_length=10)
    age = models.IntegerField()
    symptoms = models.TextField(null=False, blank=False, max_length=500)
    date = models.DateField(blank=False)


