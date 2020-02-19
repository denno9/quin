
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login 
from django.contrib.auth.models import User
from django.core.mail import EmailMessage,send_mail
import datetime

# Create your views here.

def theTeam(request):
    x = datetime.datetime.now()
    year = x.strftime("%Y")
    context= {
         "year": year
    }
    return render(request,"theTeamPage.html",context)