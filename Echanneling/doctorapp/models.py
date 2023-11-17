from django.db import models
from django.db import models
from datetime import date
from tokenize import Name
from unittest.util import _MAX_LENGTH

class Appointment(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    request = models.TextField(blank=True)
    sent_date = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=False)
    accepted_date = models.DateTimeField(auto_now=False, null=True, blank=True)

    def __str__(self):
        return f"Appointment for {self.first_name}"

    class Meta:
        ordering = ["-sent_date"]


class book(models.Model):
    your_name=models.CharField(max_length=255, default="Nuva")
    your_phone=models.IntegerField(default="0123456789")
    your_email=models.EmailField(max_length=255, default="nuvanthaabey@gmail.com")
    your_address=models.CharField(max_length=255, default="Nuva")
    your_schedule=models.CharField(max_length=255, default="Nuva")
    your_date=models.CharField(max_length=255, default="Nuva")
    your_message=models.TextField(max_length=255, default="Nuva")        

class SignUp(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    accepted = models.BooleanField(default=False)
    accepted_date = models.DateTimeField(auto_now=False, null=True, blank=True)


# Create your models here.
class Doctor(models.Model):
    Name = models.CharField(max_length=40)
    Specialty = models.CharField(max_length=40)
    Reg_number = models.IntegerField()

    def __str__(self):
        return self.Name

class Patient(models.Model):
    Name = models.CharField(max_length=60)
    Sex = models.CharField(max_length=10)
    Age = models.IntegerField()
    ContactNo = models.IntegerField(null=True)

from django.db import models
from django.contrib.auth.models import User

class DoctorProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link each profile to a user
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    hospital = models.CharField(max_length=100)
    available_time = models.TextField()
    profile_image = models.ImageField(upload_to='doctor_profiles/', blank=True, null=True)

    def __str__(self):
        return self.name
