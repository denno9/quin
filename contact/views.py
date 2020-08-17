
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,get_user_model
from django.contrib.auth.models import User
from django.utils.http import is_safe_url
from .forms import ContactForm
from django.urls import reverse

import datetime


from django.http import HttpResponseRedirect

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

def login_Page(request):
    next_url = request.GET.get('next') 
    next_url1 = request.POST.get('next') 
    redirect_url = next_url or next_url1 or None
    
    if request.method== "POST":
        username = request.POST.get("email")
        password = request.POST.get("password")
        print(username)
        print(password)
        user = authenticate(request, username=username, password=password)
        # print(user)
        if user is not None:
           
            login(request,user)
        
            if request.user.is_admin or request.user.is_superuser:
                return redirect('admin:index')
           
        else:
            if is_safe_url(redirect_url, request.get_host()):
                print(request.get_host())

                return redirect(redirect_url)
            else:
                return redirect("/")
            print("invalid ........")      
    return  redirect("/") 