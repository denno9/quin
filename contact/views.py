
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login 
from django.contrib.auth.models import User
from .forms import ContactForm
from django.core.mail import EmailMessage,send_mail
from django.conf import settings
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

    if request.method == "POST":
        if form.is_valid():
            fullname = form.cleaned_data.get("fullname")
            sender_email  = form.cleaned_data.get("email")
            sender = settings.EMAIL_HOST_USER
            subject = form.cleaned_data.get("subject")
            sms = "jina: " + fullname + "\n"  + "email: "+ sender_email + "\n" +"request: "+ form.cleaned_data.get("body") + "\n"
            recepient = ['info@qcc.co.tz',send_mail]
            context['form'] = ContactForm()
           
            send_mail(subject,sms,sender, recepient,fail_silently=True)
            print(sender_email)
            print(subject)
            print(sms)
            
            form.save()
            return redirect('/')
        
    return render(request,"contactPage.html",context)
