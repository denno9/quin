
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login 
from django.contrib.auth.models import User
from .forms import ContactForm
from django.core.mail import EmailMessage,send_mail
import datetime

# Create your views here.
def contactPage(request):
    form = ContactForm(request.POST or None)
    x = datetime.datetime.now()
    year = x.strftime("%Y")
    context= {
        "form":form,
         "year": year
    }
    return render(request,"contactPage.html",context)
