from django.shortcuts import render
from .models import Destination
from django.http import HttpResponse


def travel(request):

    dests=Destination.objects.all()
    return render(request,'travel.html',{'dests': dests})
