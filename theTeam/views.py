
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login 
from django.contrib.auth.models import User
from django.core.mail import EmailMessage,send_mail
import datetime
from .models import TheTeam

# Create your views here.

def theTeam(request):
    obj = TheTeam.objects.all().filter(active=True)
    x = datetime.datetime.now()
    year = x.strftime("%Y")

    context= {
         "year": year,
         "object_list":obj
    }
    print(context['object_list'])
    return render(request,"theTeamPage.html",context)