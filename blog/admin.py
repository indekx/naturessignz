from django.contrib import admin
from blog.models import Article

# Register your models here.
class ArticlesAdmin(admin.ModelAdmin):
    display = [
        ('Description', 
           {'fields': 
               ['title', 'date', 
               'content', 'detail'
               ]
           }),
      ]

    class Meta:
        model = Article


admin.site.register(Article, ArticlesAdmin)