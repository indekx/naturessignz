import uuid

from django.conf import settings
from django.conf.global_settings import AUTH_USER_MODEL
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models import Q, query, signals
from django.db.models.signals import pre_save
from django.forms import ModelForm
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import ugettext_lazy


class ProductQSet(models.QuerySet):
    def search(self, query=None):
        qset = self
        if query is not None:
            or_lookup = (
                Q(title__icontains=query) |
                Q(category__icontains=query) |
                Q(description__icontains=query)
               )
            qset = qset.filter(or_lookup).distinct()
        return qset

class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQSet(self.model, using=self._db)
    
    def search(self, query=None):
        return self.get_queryset().search(query=query)


class Item(models.Model):
    CAT_CHOICES = (
        ( '', 'select' ),
        ('BEAUTY', 'Beauty'),
        ('PERSONAL_CARE', 'Personal Care'),
        ('MEDICINE_AND_TREATMENT', 'Medicine & Treatment'),
        ('NATURAL_AND_ORGANIC', 'Natural & Organic'),
        ('SUPPLEMENT_AND_VITAMINS', 'Supplements & Vitamins'),
    )    

    LABEL_CHOICES = (
        ('', 'select'),
        ('P', 'primary'),
        ('S', 'secondary'),
        ('D', 'danger'),
    )
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(blank=False, default=None, null=False)
    price = models.FloatField(blank=False, null=False, default=None)
    category = models.CharField(choices=CAT_CHOICES, default='select', max_length=20)
    width = models.IntegerField(default=232)
    height = models.IntegerField(default=250)
    label = models.CharField(choices=LABEL_CHOICES, max_length=15, default='select')
    description = models.CharField(blank=True, max_length=150)
    detail = models.TextField(blank=True, max_length=2500)
    slug = models.SlugField()

    def __str__(self):
        return self.title

class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    ordered = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()

    def __str__(self):
        return self.user.username
