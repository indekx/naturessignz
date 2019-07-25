from django.conf.urls import url
from appointments import views

urlpatterns = [
    url(r'^schedule/$', views.schedule_appointment, name='schedule_appointment'),
]