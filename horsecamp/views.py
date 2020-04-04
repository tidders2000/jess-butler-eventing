from django.shortcuts import render

# Create your views here.
def horsecamp(request):
     return render(request,'horsecamp.html')

def lessons(request):
     return render(request,'lessons.html')