from django.shortcuts import render, redirect, reverse

def index(request):
    return render(request,'index.html')

# Create your views here.
