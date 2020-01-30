from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login 
from django.contrib.auth.models import User

from django.core.mail import EmailMessage,send_mail
import datetime





def HomePage(request):
    return render(request,"homepage.html",{})




def theTeam(request):
    return render(request,"theTeamPage.html",{})