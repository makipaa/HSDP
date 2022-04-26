from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User

from hemodonor_condition import condition
from .forms import user_register_form
from fhir_client import hemodonor_client as h_client
import datetime

def register(request):
    if request.method == 'POST':
        form = user_register_form(request.POST)
        if form.is_valid:
            form.save()
            username = form.cleaned_data.get('uname')
            messages.success(request, f'Account created for {username}!')
            return redirect('/home/')
    else:
        form = user_register_form()
    return render(request, 'register.html', {'form':form})

def home(request):

    if request.method == 'GET':
        # Unauthenticated user is trying to access home page, redirect to login page
        if not request.user.is_authenticated:
            return redirect('../login/')

        if request.user.username == 'doctor':
            # Exclude admin and doctor from this list
            list_of_users = User.objects.all()[3:]
     
            all_users = []
            t1 = datetime.datetime.now()
            for user_obj in list_of_users:
                donor_data = h_client.get_latest_measurements(user_obj.username)
                 # TODO Replace the dummy values
                #eligbility = condition(10, donor_data['age'], donor_data['weight'], 60, donor_data['hemoglobin'], donor_data['gender'])
                all_users.append({'data' : user_obj, 'elig' : 0})
            t2 = datetime.datetime.now()
            print((t2-t1).total_seconds())
            context = {
                'users' : all_users,
            }
            return render(request, 'doctor_home.html', context)
        else:
            data = h_client.get_relevant_data(request.user.username)
            latest_measurements = h_client.get_latest_measurements(request.user.username)
            context = {
                'user_data': data,
                'latest_measurements' : latest_measurements
            }
            return render(request, 'donor_home.html', context)
    
def doctor_donor(request, donor_id):
    if not request.user.is_superuser:
        return redirect('../../home')
    data = h_client.get_relevant_data(donor_id)
    latest_measurements = h_client.get_latest_measurements(donor_id)
    personal_info = User.objects.filter(username=donor_id).first()
    context = {
        'user_data': data,
        'latest_measurements' : latest_measurements,
        'personal_info' : personal_info
    }
    return render(request, 'doctor_donor_view.html', context)