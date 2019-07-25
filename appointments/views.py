from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from requests.api import request
from . import forms
from .models import BookAppointment

# Google reCaptcha dependencies
import urllib
import json
from django.contrib import messages


def appointments(request):
    return render(request, 'appointments/appointments.html')

@login_required(login_url='/accounts/login/')
def schedule_appointment(request):
    if request.method == 'POST':
        form = forms.BookAppointment(request.POST)
        if form.is_valid():

            ''' reCAPTCHA Validation Begins '''
            recaptcha_response = response.POST.get('g-recaptcha-response')
            values = {
                'secret_key': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req =  urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())
            ''' reCAPTCHA Validation Ends '''

            if result['success']:
                # Save data
                form_instance_create = form.save(commit=False)
                form_instance_create.user = request.user
                form_instance_create.save()
                messages.success(request, 'Appointment was successfully scheduled!')   
            else:
                messages.error(request, 'reCaptcha validation failed, please retry.')
            
            return redirect('schdule_appointment')
    else:
        form = forms.BookAppointment()

    return render(request, 'appointments/schedule_appointment.html',  {'form': form})