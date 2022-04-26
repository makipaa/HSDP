from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', views.register),
    path('home/', views.home, name='home'),
    path('donor_home/<donor_id>/', views.doctor_donor, name='doctor_donor'),
    path('donor_past_data/', views.donor_full_data, name='donor_past_data'),
    path('donor_past_data/<donor_id>/', views.doctor_donor_full_data, name='doctor_donor_full_data')
]