from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    display = [
        ('Description', 
           {'fields': 
               ['title', 'image', 
               'description', 'detail'
               ]
           }),
      ]

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)






