from django.conf.urls import url
from business import views

urlpatterns = [
    url(r'^affilaite_member/$', views.become_an_affiliate, name='become_an_affiliate'),
    url(r'^new_distributor/$', views.become_distributor, name='become_distributor'),
]
