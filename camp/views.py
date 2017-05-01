from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Camp
import datetime
# Create your views here.
def index(request):
	list = Camp.objects.filter(date__date__gte=datetime.date.today()).order_by('date')
	return render(request,
        'camp.html',
        context={'list':list},
    )

def detail(request, camp_id):
	list = Camp.objects.filter(id=camp_id)
	return render(request,
	        'detail.html',
	        context={'list':list},
	    )