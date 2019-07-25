from django.contrib import admin
from .models import BookAppointment

# Register your models here.
class BookAppointmentAdmin(admin.ModelAdmin):
    display = [
        ('Description', 
           {'fields': 
               ['title', 'full_name', 
               'gender', 'date',
               'symptoms'
               ]
           }),
      ]

    class Meta:
        model = BookAppointment


admin.site.register(BookAppointment, BookAppointmentAdmin)






