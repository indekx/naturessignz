import uuid

from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models import Q, query, signals
from django.db.models.signals import pre_save
from django.forms import ModelForm
# Create your models here.
from django.urls import reverse
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy

# Python file used for 'unique slug generation' is called here.
from baseapp.utils import unique_slug_gen

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
         
class Product(models.Model):
    BEAUTY = 'BTY'
    PERSONAL_CARE = 'PER_CARE'
    MEDICINE_AND_TREATMENT = 'MED_TREAT'
    NATURAL_AND_ORGANIC = 'N&O'
    SUPPLEMENT_AND_VITAMINS = 'SUPP_AND_VIT'

    CAT_CHOICES = (
        ( '', 'select' ),
        (BEAUTY, 'Beauty'),
        (PERSONAL_CARE, 'Personal Care'),
        (MEDICINE_AND_TREATMENT, 'Medicine & Treatment'),
        (NATURAL_AND_ORGANIC, 'Natural & Organic'),
        (SUPPLEMENT_AND_VITAMINS, 'Supplements & Vitamins'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=None, on_delete=models.CASCADE)
    title = models.CharField(max_length=60)
    category = models.CharField(choices=CAT_CHOICES, default='select', max_length=20, )
    image = models.ImageField(null=False, blank=False)
    width = models.IntegerField(default=232)
    height = models.IntegerField(default=250)
    slug = models.SlugField(default='page-slug', blank=True, unique=True)
    description = models.CharField(max_length=160, null=False, blank=False)
    detail = models.TextField(null=False, blank=False, max_length=2500)
    is_favourite = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    objects = ProductManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={"slug": self.slug})

    class META:
        ordering = ['-timestamp']

# Here is the Pre_save receiver function and statement.
def pre_save_receiver_product_model(sender, instance, *args, **kwargs):
    if instance.slug == 'page-slug' or instance.slug == '':
        instance.slug = unique_slug_gen(instance)

# The Pre_save Connect for product model
pre_save.connect(pre_save_receiver_product_model, sender=Product)
