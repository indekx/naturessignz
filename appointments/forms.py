from django import forms
from appointments import models


class BookAppointment(forms.ModelForm):
    class Meta:
        model = models.BookAppointment
        fields = [
            'title',
            'full_name',
            'email',
            'gender',
            'age',
            'symptoms',
            'date',
         ]
        
    login_url = '/login/'
