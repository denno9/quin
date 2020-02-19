from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login 
from django.contrib.auth.models import User
from django.core.mail import EmailMessage,send_mail
import datetime





def HomePage(request):
    x = datetime.datetime.now()
    year = x.strftime("%Y")
    context= {
         "year": year
    }
    return render(request,"homepage.html",context)



def errorPage(request):
    return render(request,"erroPage.html",{})



def aboutPage(request):
    x = datetime.datetime.now()
    year = x.strftime("%Y")
    context= {
         "year": year
    }
    return render(request,"aboutPage.html",context)








def expertisePage(request):
    x = datetime.datetime.now()
    year = x.strftime("%Y")
    context= {
         "year": year
    }
    return render(request,"expertisePage.html",context)