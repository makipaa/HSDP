from http.client import NOT_IMPLEMENTED
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from utils import current_user
from utils import validate_user
from django.contrib import messages
from utils import patient_data

def login(request):
    return render(request, 'login.html')


def login_submit(request):
    if request.method == 'POST':
        username = request.POST.get("uname")
        psw = request.POST.get("psw")

        validated_user = validate_user(username, psw)
        if(validated_user is None):
            messages.add_message(request, messages.INFO, 'Incorrect username or password!')
            return HttpResponseRedirect('/')
        else:
            if(validated_user == 'donor'):
                return render(request, 'donor_home.html')
                #return HttpResponseRedirect('/donor_home')
            else:
                return doctor_home(request, validated_user)
   
    if request.method == 'GET':
        return HttpResponseRedirect('/')

# TODO
def register(request):
    patient = patient_data('2113340')
    print(patient)
    return render(request, '<h1> Hello world </h1>')

# TODO
def doctor_home(request, validated_user=None):
    curr_user = validated_user
    print(curr_user)
    if request.method == 'GET':
        if curr_user == None:
            return HttpResponseRedirect('/')

        if curr_user["username"] != 'doctor' | curr_user["logged_in"] is False:
            return HttpResponseRedirect('/')
    
        return render(request, 'doctor_home.html')
# TODO
def donor_home(request):
    NOT_IMPLEMENTED
    
