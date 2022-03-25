from http.client import NOT_IMPLEMENTED
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .forms import user_register_form


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
            return render(request, 'doctor_home.html')
        else:
            return render(request, 'donor_home.html')
    