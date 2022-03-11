from django.urls import path
from . import views

urlpatterns = [
    path('', views.login),
    path('login_submit/', views.login_submit),
    path('register/', views.register),
    path('doctor_home/', views.doctor_home),
    path('donor_home/', views.donor_home),
]