from django.shortcuts import render
from .models import Feedback

def feedback (request):
    fb=Feedback.objects.all()
    return render (request,'feedback.html',{'fb':fb})
