from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User


from utils import condition

from .forms import user_register_form
from fhir_client import hemodonor_client as h_client

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
            list_of_users = User.objects.all()[2:]
            all_users = []
           
            for user_obj in list_of_users:
                donor_data = h_client.get_latest_measurements(user_obj.username)
                eligbility = condition(request.user.username, donor_data['weight'], donor_data['diastolic'], donor_data['systolic'], 
                                        donor_data['hemoglobin'], donor_data['gender'], donor_data['age'])

                all_users.append({'data' : user_obj, 'elig' : eligbility})
          

            context = {
                'users' : all_users,
            }
            return render(request, 'doctor_home.html', context)
        else:
            data = h_client.get_relevant_data(request.user.username)
            latest_measurements = h_client.get_latest_measurements(request.user.username)
            eligbility = condition(request.user.username, latest_measurements['weight'], latest_measurements['diastolic'], latest_measurements['systolic'], 
                                    latest_measurements['hemoglobin'], latest_measurements['gender'], latest_measurements['age'])

            context = {
                'user_data': data,
                'latest_measurements' : latest_measurements,
                'eligbility': eligbility
            }
            return render(request, 'donor_home.html', context)
    
def doctor_donor(request, donor_id):
    if not request.user.is_superuser:
        return redirect('../../home')

    data = h_client.get_relevant_data(donor_id)
    latest_measurements = h_client.get_latest_measurements(donor_id)
    eligbility = condition(request.user.username, latest_measurements['weight'], latest_measurements['diastolic'], latest_measurements['systolic'], 
                                    latest_measurements['hemoglobin'], latest_measurements['gender'], latest_measurements['age'])

    personal_info = User.objects.filter(username=donor_id).first()
    context = {
        'user_data': data,
        'latest_measurements' : latest_measurements,
        'personal_info' : personal_info,
        'eligbility': eligbility
    }
    return render(request, 'doctor_donor_view.html', context)

def donor_full_data(request):
    if not request.user.is_authenticated:
        return redirect('../login/')
    weight_data = h_client.get_measurement(request.user.username,'weight')
    systolic_data = h_client.get_measurement(request.user.username,'systolic')
    diastolic_data = h_client.get_measurement(request.user.username,'diastolic')
    hemoglobin_data = h_client.get_measurement(request.user.username,'hemoglobin')
    iteration = 0
    
    if len(weight_data) > len(systolic_data):
        iteration = len(weight_data) - len(systolic_data)
        for i in range(iteration):
            systolic_data.append("No data")
    if len(weight_data) > len(diastolic_data):
        iteration = len(weight_data) - len(diastolic_data)
        for i in range(iteration):
            diastolic_data.append("No data")
    if len(weight_data) > len(hemoglobin_data):
        iteration = len(weight_data) - len(hemoglobin_data)
        for i in range(iteration):
            hemoglobin_data.append("No data")
    
    if len(systolic_data) > len(weight_data):
        iteration = len(systolic_data) - len(weight_data)
        for i in range(iteration):
            weight_data.append("No data")
    if len(systolic_data) > len(diastolic_data):
        iteration = len(systolic_data) - len(diastolic_data)
        for i in range(iteration):
            diastolic_data.append("No data")
    if len(systolic_data) > len(hemoglobin_data):  
        iteration = len(systolic_data) - len(hemoglobin_data) 
        for i in range(iteration):
            hemoglobin_data.append("No data") 
    
    if len(diastolic_data) > len(weight_data):
        iteration = len(diastolic_data) - len(weight_data)
        for i in range(iteration):
            weight_data.append("No data")
    if len(diastolic_data) > len(systolic_data):
        iteration = len(diastolic_data) - len(systolic_data)
        for i in range(iteration):
            systolic_data.append("No data")
    if len(diastolic_data) > len(hemoglobin_data):
        iteration = len(diastolic_data) - len(hemoglobin_data)   
        for i in range(iteration):
            hemoglobin_data.append("No data") 
    
    if len(hemoglobin_data) > len(weight_data):
        iteration = len(hemoglobin_data) - len(weight_data)
        for i in range(iteration):
            weight_data.append("No data")
    if len(hemoglobin_data) > len(systolic_data):
        iteration = len(hemoglobin_data) - len(systolic_data)
        for i in range(iteration):
            systolic_data.append("No data")
    if len(hemoglobin_data) > len(diastolic_data):  
        iteration = len(hemoglobin_data) - len(diastolic_data) 
        for i in range(iteration):
            diastolic_data.append("No data") 
  
    data = []
    for i in range(len(weight_data)):
        data.append({'hg' : hemoglobin_data[i], 'sys': systolic_data[i], 'dia' : diastolic_data[i], 'weight' : weight_data[i]})

    context = {
        'weight_data': weight_data,
        'systolic_data' : systolic_data,
        'diastolic_data' : diastolic_data,
        'hemoglobin_data': hemoglobin_data,
        'all_data' : data
    }
    return render(request, 'donor_past_measurements.html', context)

def doctor_donor_full_data(request, donor_id):
    if not request.user.is_superuser:
        return redirect('../../home')
    weight_data = h_client.get_measurement(donor_id,'weight')
    systolic_data = h_client.get_measurement(donor_id,'systolic')
    diastolic_data = h_client.get_measurement(donor_id,'diastolic')
    hemoglobin_data = h_client.get_measurement(donor_id,'hemoglobin')
    iteration = 0
    
    if len(weight_data) > len(systolic_data):
        iteration = len(weight_data) - len(systolic_data)
        for i in range(iteration):
            systolic_data.append("No data")
    if len(weight_data) > len(diastolic_data):
        iteration = len(weight_data) - len(diastolic_data)
        for i in range(iteration):
            diastolic_data.append("No data")
    if len(weight_data) > len(hemoglobin_data):
        iteration = len(weight_data) - len(hemoglobin_data)
        for i in range(iteration):
            hemoglobin_data.append("No data")
    
    if len(systolic_data) > len(weight_data):
        iteration = len(systolic_data) - len(weight_data)
        for i in range(iteration):
            weight_data.append("No data")
    if len(systolic_data) > len(diastolic_data):
        iteration = len(systolic_data) - len(diastolic_data)
        for i in range(iteration):
            diastolic_data.append("No data")
    if len(systolic_data) > len(hemoglobin_data):  
        iteration = len(systolic_data) - len(hemoglobin_data) 
        for i in range(iteration):
            hemoglobin_data.append("No data") 
    
    if len(diastolic_data) > len(weight_data):
        iteration = len(diastolic_data) - len(weight_data)
        for i in range(iteration):
            weight_data.append("No data")
    if len(diastolic_data) > len(systolic_data):
        iteration = len(diastolic_data) - len(systolic_data)
        for i in range(iteration):
            systolic_data.append("No data")
    if len(diastolic_data) > len(hemoglobin_data):
        iteration = len(diastolic_data) - len(hemoglobin_data)   
        for i in range(iteration):
            hemoglobin_data.append("No data") 
    
    if len(hemoglobin_data) > len(weight_data):
        iteration = len(hemoglobin_data) - len(weight_data)
        for i in range(iteration):
            weight_data.append("No data")
    if len(hemoglobin_data) > len(systolic_data):
        iteration = len(hemoglobin_data) - len(systolic_data)
        for i in range(iteration):
            systolic_data.append("No data")
    if len(hemoglobin_data) > len(diastolic_data):  
        iteration = len(hemoglobin_data) - len(diastolic_data) 
        for i in range(iteration):
            diastolic_data.append("No data") 
  
    data = []
    for i in range(len(weight_data)):
        data.append({'hg' : hemoglobin_data[i], 'sys': systolic_data[i], 'dia' : diastolic_data[i], 'weight' : weight_data[i]})
    personal_info = User.objects.filter(username=donor_id).first()
    
    context = {
        'weight_data': weight_data,
        'systolic_data' : systolic_data,
        'diastolic_data' : diastolic_data,
        'hemoglobin_data': hemoglobin_data,
        'all_data' : data,
        'personal_info' : personal_info
    }
    return render(request, 'donor_past_measurements.html', context)
