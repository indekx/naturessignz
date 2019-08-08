from django import forms
from blog import models


class AddArticle(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = [
            'title',
            'slug',
            'content',
            'detail',
         ]
        
    login_url = '/login/'

