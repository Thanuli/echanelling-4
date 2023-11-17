from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.core.mail import EmailMessage, message
from django.conf import settings
from django.contrib import messages
from .models import Appointment
from django.views.generic import ListView
import datetime
from django.template import Context
from django.template.loader import render_to_string, get_template
from .forms import NewUserForm
from django.shortcuts import render

from re import U
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.core.mail import EmailMessage, message
from django.conf import settings
from django.contrib import messages
from .models import Appointment
from django.views.generic import ListView
import datetime
from django.template import Context
from django.template.loader import render_to_string, get_template

class HomeTemplateView(TemplateView):
    template_name = "index (1).html"
    
    def post(self, request):
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        email = EmailMessage(
            subject= f"{name} from doctor family.",
            body=message,
            from_email=settings.EMAIL_HOST_USER,
            to=[settings.EMAIL_HOST_USER],
            reply_to=[email]
        )
        email.send()
        return HttpResponse("Email sent successfully!")





from django.http import HttpResponseRedirect  # Import HttpResponseRedirect

class AppointmentTemplateView(TemplateView):
    template_name = "appointment.html"

    def post(self, request):
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")  # Corrected variable name
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        message = request.POST.get("request")

        appointment = Appointment.objects.create(
            first_name=fname,
            last_name=lname,
            email=email,
            phone=mobile,
            request=message,
        )

        appointment.save()

        messages.add_message(request, messages.SUCCESS, f"Thanks {fname} for making an appointment, we will email you ASAP!")
        return HttpResponseRedirect(request.path)

    
def book(request):
    if request.method == "POST":
        your_name = request.POST['your_name']
        your_phone = request.POST['your_phone']
        your_email = request.POST['your_email']
        your_address = request.POST['your_address']
        your_schedule = request.POST['your_schedule']
        your_date = request.POST['your_date']
        your_message = request.POST['your_message']

        return render(request, 'appointment.html', {
            'your_name': your_name,
            'your_phone': your_phone,
            'your_email': your_email,
            'your_address': your_address,
            'your_schedule': your_schedule,
            'your_date': your_date,
            'your_message': your_message
        })

    else:
        return render(request, 'index (1).html', {})

class ManageAppointmentTemplateView(ListView):
    template_name = "manage-appointments.html"
    model = Appointment
    context_object_name = "appointments"
    login_required = True
    paginate_by = 3


    def post(self, request):
        date = request.POST.get("date")
        appointment_id = request.POST.get("appointment-id")
        appointment = Appointment.objects.get(id=appointment_id)
        appointment.accepted = True
        appointment.accepted_date = datetime.datetime.now()
        appointment.save()

        data = {
            "fname":appointment.first_name,
            "date":date,
        }

        message = get_template('email.html').render(data)
        email = EmailMessage(
            
            subject= "{} from doctor family.",
            body=message,
            from_email=settings.EMAIL_HOST_USER,
            to=[settings.EMAIL_HOST_USER],

        )
        email.send()
        return HttpResponse("Email sent successfully!")

def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        appointments = Appointment.objects.all()
        context.update({   
            "title":"Manage Appointments"
        })
        return context
        messages.add_message(request, messages.SUCCESS, f"You accepted the appointment of {appointment.first_name}")
        return HttpResponseRedirect(request.path)
    
def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("appointment")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="register (1).html", context={"register_form": form})

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("doctorlist")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})
    
# Create your views here.
def contactus(request):
    return render(request, 'contactus.html')


def about(request):
    return render(request, 'about.html')


def home(request):
    return render(request, 'home.html')


def index(request):
    if not request.user.is_staff:
        return redirect('login')
    return render(request, 'index.html')

def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("home")


def appointment(request):
    if request.method == "POST":
        your_name = request.POST['your_name']
        your_phone = request.POST['your_phone']
        your_email = request.POST['your_email']
        your_address = request.POST['your_address']
        your_schedule = request.POST['your_schedule']
        your_date = request.POST['your_date']
        your_message = request.POST['your_message']

        return render(request, 'appoinment.html', {
            'your_name': your_name,
            'your_phone': your_phone,
            'your_email': your_email,
            'your_address': your_address,
            'your_schedule': your_schedule,
            'your_date': your_date,
            'your_message': your_message
        })

    else:
        return render(request, 'home.html', {})
    
def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        appointments = Appointment.objects.all()
        context.update({   
            "title":"Manage Appointments"
        })
        return context
def doctorlist(request):
    return render(request, 'doctorlist.html')

def afterlogin(request):
    return render(request, 'afterlogin.html')

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import DoctorProfileForm

@login_required
def add_doctor_profile(request):
    if request.method == 'POST':
        form = DoctorProfileForm(request.POST, request.FILES)
        if form.is_valid():
            doctor_profile = form.save(commit=False)
            doctor_profile.user = request.user
            doctor_profile.save()
            return redirect('doctorlist')  # Redirect to the doctor list or another page
    else:
        form = DoctorProfileForm()

    return render(request, 'doctorprofile.html', {'form': form})

from .models import DoctorProfile  # Import the DoctorProfile model

def doctorlist(request):
    doctors = DoctorProfile.objects.all()  # Fetch all doctor profiles
    return render(request, 'doctorlist.html', {'doctors': doctors})

from django.shortcuts import redirect, get_object_or_404
from .models import DoctorProfile  # Import your DoctorProfile model

def remove_doctor(request, doctor_id):
    if request.user.is_staff:
        doctor = get_object_or_404(DoctorProfile, pk=doctor_id)
        doctor.delete()
    return redirect('doctorlist')  # Redirect back to the doctor list after removal
