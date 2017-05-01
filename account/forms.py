from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm

class DonorRegistrationForm(UserCreationForm):
	email = forms.EmailField(required=True)
	
	class Meta:
		model = User
		fields = (
			'username',
			'first_name',
			'last_name',
			'email',
			'password1',
			'password2',
			)						

	def save(self, commit=True):
		user = super(DonorRegistrationForm, self).save(commit=False)
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.email = self.cleaned_data['email']
		if commit:
			user.save()			


		return user


class RrcRegistrationForm(UserCreationForm):
	email = forms.EmailField(required=True)
	
	class Meta:
		model = User
		fields = (
			'username',
			'first_name',
			'last_name',
			'email',
			'password1',
			'password2',
			)						

	def save(self, commit=True):
		user = super(RrcRegistrationForm, self).save(commit=False)
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.email = self.cleaned_data['email']


		if commit:
			user.save()


		return user