from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect, HttpResponse
from .forms import DonorRegistrationForm, RrcRegistrationForm
from donor.models import Donor
from rrc.models import Rrc
# Create your views here.


def register(request):
	return render(request,
	        'reg_choice.html',
	        context={}
	    )




def register_donor(request):
	if request.method == 'POST':
		form = DonorRegistrationForm(request.POST)
		if form.is_valid():
			form.save()


			user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],)

                                  
			if user is not None:

				user.groups.add(Group.objects.get(name='Donor'))
				Donor.objects.create(user=user)
				user.donor.save()


				login(request, user)
			return HttpResponseRedirect('/logged')
		else:
			return HttpResponse('INCORRECT')
	else:
		form = DonorRegistrationForm()
		
		return render(request,
	        'reg_form1.html',
	        context={'form':form}
	    )

def register_rrc(request):
	if request.method == 'POST':
		form = RrcRegistrationForm(request.POST)
		if form.is_valid():
			form.save()

			user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],)

                                  
			if user is not None:
				user.groups.add(Group.objects.get(name='RRC'))
				Rrc.objects.create(user=user)
				user.rrc.save()

				login(request, user)
			return HttpResponseRedirect('/logged')
			                              
			
			return HttpResponseRedirect('/logged')
		else:
			return HttpResponse('INCORRECT')
	else:
		form = RrcRegistrationForm()
		args = {'form':form}
		return render(request,
	        'reg_form1.html',
	        context={'form':form}
	    )


