from django import forms
from django.contrib.auth.models import User, Group
from .models import Donor
from django.contrib.auth.forms import UserCreationForm

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email"]
    username = forms.CharField(disabled=True)

class DonorProfileForm(forms.ModelForm):
    class Meta:
        model = Donor
        exclude = ["user"]