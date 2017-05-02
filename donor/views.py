from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import DonorProfileForm, UserForm
from .models import Donor
from request.models import Request
from datetime import datetime, timedelta

# Create your views here.
def home(request):
	user = request.user
	if request.method == "POST":
			uform = UserForm(request.POST)
			pform = DonorProfileForm(request.POST)
			if pform.is_valid():
				#user.username = uform.cleaned_data['username']
				#user.email = uform.cleaned_data['email']
				
				user.donor.name = pform.cleaned_data['name']
				user.donor.blood = pform.cleaned_data['blood']
				user.donor.district = pform.cleaned_data['district']
				user.donor.address = pform.cleaned_data['address']
				user.donor.pincode = pform.cleaned_data['pincode']
				user.donor.contact = pform.cleaned_data['contact']
				user.donor.weight = pform.cleaned_data['weight']
				user.donor.dob = pform.cleaned_data['dob']
				user.donor.last_donated = pform.cleaned_data['last_donated']
				user.donor.gender = pform.cleaned_data['gender']
				user.donor.save()
				user.save()

				return HttpResponseRedirect('/logged')
			else:
				return HttpResponse('INCORRECT')	
	else:
		uform = UserForm(instance = user)
		pform = DonorProfileForm(instance = user.donor)
		return render(request,
	        'homedonor.html',
	        context={'uform':uform,'pform':pform},
	        )

def requests(request):
	last_month = datetime.today() - timedelta(days=1)
	t1 = Donor.objects.get(user=request.user)
	bloodtemp = t1.blood
	list = Request.objects.filter(date_of_request__date__gte=last_month, blood=bloodtemp).order_by('date_of_request')
	return render(
        request,
        'requestdonor.html',
        context={'list':list},
    )