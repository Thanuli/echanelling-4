from turtle import home
from django.urls import URLPattern, path
from .views import HomeTemplateView, AppointmentTemplateView, ManageAppointmentTemplateView, about, afterlogin, contactus, doctorlist, login_request, logout_request, register_request, book
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView
from .import views

class CustomLoginView(LoginView):
    template_name = 'login.html'
# urls.py

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", HomeTemplateView.as_view(), name="home"),
    path("appointment/", AppointmentTemplateView.as_view(), name="appointment"),
    path("manage-appointments/", ManageAppointmentTemplateView.as_view(), name="manage"),
    path("", include("django.contrib.auth.urls")),  # Include login, logout, password reset URLs
    path('about/',about,name='about'),
    path('contactus/',contactus,name='contactus'),
    path("register/", register_request, name="register"),
    path("login/", login_request, name="login"),
    path("logout/", logout_request, name= "logout"),
    path("doctorlist/", doctorlist, name="doctorlist"),
    path("afterlogin/", afterlogin, name="afterlogin"),
    path("accounts/profile/", HomeTemplateView.as_view(), name="accounts/profile/"),
    path('add_doctor_profile/', views.add_doctor_profile, name='add_doctor_profile'),
    path('remove_doctor/<int:doctor_id>/', views.remove_doctor, name='remove_doctor'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
