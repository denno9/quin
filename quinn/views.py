from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login 
from django.contrib.auth.models import User
from django.core.mail import EmailMessage,send_mail
import datetime





def HomePage(request):
    return render(request,"homepage.html",{})



def errorPage(request):
    return render(request,"erroPage.html",{})



def aboutPage(request):
    return render(request,"aboutPage.html", {})








def expertisePage(request):
    return render(request,"expertisePage.html",{})