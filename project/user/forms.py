from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserLocation

User = get_user_model()

class UserRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

class UserLocationForm(forms.ModelForm):
    class Meta:
        model = UserLocation
        fields = ['LATITUDE', 'LONGITUDE']