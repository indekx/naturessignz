from django.conf.urls import url
from articles import views

urlpatterns = [
    url(r'^article_list/$', views.blog_list, name='blog_list'),
    url(r'^create/$', views.create_article, name='create_article'),
]