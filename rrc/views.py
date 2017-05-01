from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import RrcProfileForm, UserForm, CampEditForm
from .filters import DonorFilter,RrcFilter

from .models import Rrc
from camp.models import Camp
from donor.models import Donor
from datetime import datetime, timedelta

# Create your views here.
def index(request):
	user_list = Rrc.objects.all()
	user_filter = RrcFilter(request.GET, queryset=user_list)
	return render(request, 'rrc.html', {'filter': user_filter})
   


def detail(request, rrc_id):
	list = Rrc.objects.filter(id=rrc_id)
	return render(request,
	        'detail.html',
	        context={'list':list},
	    )

def home(request):
	user = request.user
	if request.method == "POST":
			#uform = UserForm(request.POST)
			pform = RrcProfileForm(request.POST)
			if pform.is_valid():
				#user.username = uform.cleaned_data['username']
				#user.email = uform.cleaned_data['email']
				
				user.rrc.name = pform.cleaned_data['name']
				user.rrc.district = pform.cleaned_data['district']
				user.rrc.address = pform.cleaned_data['address']
				user.rrc.contact = pform.cleaned_data['contact']
				user.rrc.save()
				user.save()

				return HttpResponseRedirect('/rrc/profile')
			else:
				return HttpResponse('INCORRECT')	
	else:
		uform = UserForm(instance = user)
		pform = RrcProfileForm(instance = user.rrc)
		return render(request,
	        'homerrc.html',
	        context={'uform':uform,'pform':pform},
	        )
def camps(request):
	user = request.user
	list = Camp.objects.filter(user=user)
	return render(
        request,
        'camprrc.html',
        context={'list':list},
    )

def campdetail(request, camp_id):
	list = Camp.objects.filter(id=camp_id)
	return render(request,
	        'campdetails.html',
	        context={'list':list},
	    )

def campedit(request, camp_id):
	instance = Camp.objects.get(id=camp_id)
	if request.method == "POST":
			pform = CampEditForm(request.POST)
			if pform.is_valid():
				instance.name = pform.cleaned_data['name']
				instance.district = pform.cleaned_data['district']
				instance.address = pform.cleaned_data['address']
				instance.contact = pform.cleaned_data['contact']
				instance.user = request.user 
				instance.save()
				

				return HttpResponseRedirect('/rrc/camps/')
			else:
				return HttpResponse('INCORRECT')		
	else:
		pform = CampEditForm(instance = instance)
		return render(request,
	        'campedit.html',
	        context={"pform":pform},
	        )


def campdelete(request, camp_id):
	instance = Camp.objects.get(id=camp_id)
	instance.delete()
	return HttpResponseRedirect('/rrc/camps')


def campcreate(request):
	if request.method == "POST":
			pform = CampEditForm(request.POST)
			if pform.is_valid():
				instance = pform.save(commit=False)
				instance.user = request.user
				instance = instance.save()				

				return HttpResponseRedirect('/rrc/camps/')
			else:
				return HttpResponse('INCORRECT')		
	else:
		pform = CampEditForm()
		return render(request,
	        'campedit.html',
	        context={"pform":pform},
	        )


def donordetail(request, donor_id):
	list = Donor.objects.filter(id=donor_id)
	return render(request,
	        'donordetail.html',
	        context={'list':list},
	    )
def donor(request):
	buffer = datetime.now()-timedelta(days=90)
	user_list = Donor.objects.filter(last_donated__lte=buffer).order_by('last_donated')
	user_filter = DonorFilter(request.GET, queryset=user_list)
	return render(request, 'donorrrc.html', {'filter': user_filter})