from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^articles/$', views.blog_list, name='blog_list'),
    url(r'^create/$', views.create_article, name='create_article'),
]