from django.contrib import admin
from .models import Appointment,Doctor,Patient, book
from .models import SignUp
from django.contrib import admin

# Register your models here.

admin.site.register(Appointment)
admin.site.register(SignUp)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(book)