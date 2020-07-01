from datetime import datetime

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import CreateView
from .forms import UserRegistrationForm, UserLocationForm
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from .models import UserLoginLogout, UserLocation

from django.contrib.auth.signals import user_logged_in, user_logged_out

User = get_user_model()

class RegisterView(CreateView):
    template_name = 'accounts/register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('login')

def welcome_page(request):
    template_name = 'index.html'
    return render(request, template_name)

def user_login_time(request, **kwargs):
    x = datetime.now()
    try:
        user = UserLoginLogout.objects.get(USER = request.user, DATE = x.date())
    except: 
        user = UserLoginLogout.objects.create(USER = request.user, DATE = x.date(), LOGIN = x.time())
    return user

def user_location_view(request):
    x = datetime.now()
    if request.is_ajax():
        queryDict = request.GET
        data = dict(queryDict)
        latitude = float(data['latitude'][0])
        longitude = float(data['longitude'][0])

        user_location = UserLocation.objects.create(USER = request.user, DATE = x.date(), LATITUDE = latitude,\
            LONGITUDE = longitude)
    
        return HttpResponse(content_type='json')

def user_logout_time(request, **kwargs):
    x = datetime.now()
    user = UserLoginLogout.objects.get(USER = request.user, DATE = x.date())
    user.LOGOUT = x.time()
    user.save()
    return user


user_logged_in.connect(user_login_time)
user_logged_out.connect(user_logout_time)