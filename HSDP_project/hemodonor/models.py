from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class donor_data(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    weight = models.IntegerField()
    hemoglobin = models.IntegerField()
    blood_pressure = models.IntegerField()
