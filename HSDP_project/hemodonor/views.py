from http.client import NOT_IMPLEMENTED
from django.shortcuts import render
from django.http import HttpResponseRedirect
from utils import validate_user
from django.contrib import messages

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

            return render(request, 'doctor_home.html')
    if request.method == 'GET':
        return HttpResponseRedirect('/')

# TODO
def register():
    NOT_IMPLEMENTED

# TODO
def doctor_home():
    NOT_IMPLEMENTED

# TODO
def donor_home():
    NOT_IMPLEMENTED