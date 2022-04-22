from http.client import NOT_IMPLEMENTED
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from HSDP_project.utils import get_latest_measurements

from utils import get_relevant_data
from .forms import user_register_form
from .models import donor_data


def register(request):
    if request.method == 'POST':
        form = user_register_form(request.POST)
        if form.is_valid:
            form.save()
            username = form.cleaned_data.get('uname')
            messages.success(request, f'Account created for {username}!')
            return redirect('home/')
    else:
        form = user_register_form()
    return render(request, 'register.html', {'form':form})

# TODO
def home(request):

    if request.method == 'GET':
        if not request.user.is_authenticated:
            return redirect('../login/')

        if request.user.username == 'doctor':
            donors = donor_data.objects.all()
            context = {
                'donors' : donors
            }
            return render(request, 'doctor_home.html', context)
        else:
            data = get_relevant_data(request.user.username)
            latest_measurements = get_latest_measurements(request.user.username)
            context = {
                'user_data': data,
                'latest_measurements' : latest_measurements
            }
            return render(request, 'donor_home.html', context)
    