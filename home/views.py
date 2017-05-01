from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth.models import User, Group
 
def index(request):
    return render(
        request,
        'index.html',
        context={},
    )

def about(request):
    return render(
        request,
        'about.html',
        context={},
    )

def logged(request):
    group1 = Group.objects.get(name="Donor").user_set.all()
    group2 = Group.objects.get(name="RRC").user_set.all()
    if request.user in group1:
        #return HttpResponse("donor")
        return HttpResponseRedirect("/donor/profile")
    elif request.user in group2:
        #return HttpResponse("RRC")
        return HttpResponseRedirect("/rrc/profile")

    else:
        return HttpResponseRedirect("/")
