from django import forms
from django.contrib.auth.models import User, Group
from .models import Rrc
from camp.models import Camp
from django.contrib.auth.forms import UserCreationForm

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email"]

class RrcProfileForm(forms.ModelForm):
    class Meta:
        model = Rrc
        exclude = ["user"]

class CampEditForm(forms.ModelForm):
	class Meta:
		model = Camp
		exclude = ["user"]
