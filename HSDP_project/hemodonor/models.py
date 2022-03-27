from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class donor_data(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    weight = models.IntegerField()
    hemoglobin = models.IntegerField()
    blood_pressure = models.IntegerField()
    donation_interval = models.IntegerField(default=0)
    gender = models.CharField(max_length=20, default='null')
