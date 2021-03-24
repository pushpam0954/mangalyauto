from django.shortcuts import render

# Create your views here.

from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.mail import send_mail

from django.conf import settings
from .forms import contactformemail
def Home(request):
        return render(request,'Home.html')


def about(request):
    return render(request,'about.html')





def Contactus(request):
    return render(request,'Contactus.html')


def Automotive(request):
    return render(request,'Automotive.html')

def Defence(request):
    return render(request,'Defence.html')

def Ancillary(request):
    return render(request,'Ancillary.html')

def Technology(request):
    return render(request,'Technology.html')




def Automotive(request):
    return render(request,'Automotive.html')



def Base(request):
    return render(request,'Base.html')



