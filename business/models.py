from random import choices

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


#Affiliate Program Model
LEVELS = (
    ('', 'select'),
    ('Manufacturer', 'Manufacturer'),
    ('Wholesaler', 'Wholesaler'),
)

class BecomeAnAffiliate(models.Model):
    
    first_name = models.CharField(blank=False, max_length=60)
    last_name = models.CharField(blank=False, max_length=60)
    email = models.EmailField(blank=False)
    job_title = models.CharField(blank=False, max_length=50)
    contact_phone_number = models.CharField(blank=False, max_length=15)
    tell_us_about_you = models.CharField(choices=LEVELS, default='select', blank=False, max_length=50)
    company_name = models.CharField(max_length=100, blank=True)
    contact_address = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=70, blank=True)
    state = models.CharField(max_length=70, blank=True)
    country = models.CharField(max_length=120, blank=True)
    website = models.CharField(max_length=100, blank=False)

