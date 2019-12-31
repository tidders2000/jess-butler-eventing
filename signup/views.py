from django.shortcuts import render, redirect,reverse
from.forms import signupform
from .models import signup
from django.contrib import messages

# Create your views here.
""" a view that allows users to view sign up and opt out"""
def signups(request):
    
    Signupform=signupform()
    
    return render(request,'signup.html',{'signupform':Signupform})
    
""" a view that adds email to signup model ready for mail outs"""
def emailadd(request):
    
      if request.method=="POST":
        
        signup = signupform(request.POST)
        if signup.is_valid():
         signup.save(commit=False)
         
         signup.save
         messages.error(request, 'email added')
        return redirect(reverse('index'))