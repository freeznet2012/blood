from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect, HttpResponse
from .forms import RequestCreationForm
from .models import Request
from datetime import datetime, timedelta
from .filters import RequestFilter

# Create your views here.

def request(request):
	last_month = datetime.today() - timedelta(days=1)
	user_list = Request.objects.filter(date_of_request__date__gte=last_month).order_by('date_of_request')
	user_filter = RequestFilter(request.GET, queryset=user_list)
	return render(request, 'request.html', {'filter': user_filter})


def create(request):
	if request.method == 'POST':
		form = RequestCreationForm(request.POST)
		if form.is_valid():
			form.save()

			return HttpResponseRedirect('/request/index')                      
			
		else:
			return HttpResponse('INCORRECT')
	else:
		form = RequestCreationForm()
		
		return render(request,
	        'reg_form.html',
	        context={'form':form}
	    )

def detail(request, request_id):
	list = Request.objects.filter(id=request_id)
	return render(request,
	        'details.html',
	        context={'list':list},
	    )