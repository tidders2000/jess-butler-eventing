from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from feedback.models import Feedback
import json
import requests
from signup.forms import signupform




def index(request):
    return render(request,'index.html')

def index1(request):
    
    r = requests.get('https://graph.facebook.com/v4.0/me?fields=id%2Cname%2Cfeed&access_token=EAAFwJhMIpkUBAJZCGoIvHYcqeprUqWGEasJ2pPCjageosx35is5ZAH1gn4xnBhFoKqV6NzAhXn25xvIhYIXkTjODCeKy9FlQSGQX496ZAQ7MuN8FgWLNlTXh1vYBeyE0OtofnxKy80UMBay6aZCqkUCVZAlca1KE5hGaoaZA5q6pcJReZC6bL0eDzHPZCtPNf6ZBRrMmnTYvAxAZDZD')
    json = r.json()
    
    h = requests.get('https://graph.facebook.com/v5.0/230231543752378?fields=feed.limit(9)%7Bmessage%2Cpermalink_url%2Cfull_picture%7D&access_token=EAAFwJhMIpkUBAI8drgzZAd3I8KntuoA6ZB9ZCTT3P1fjLkizWc4Tr3QbSqLHbGAIJZBVyIXOX1zfLXhHbkvYbnEROCSqaITuYh0IoPz7KDfDfuCZC9VqFViun185jcwPfPIZBZCHz9E1VPLXrnfgLJ70Igdez7AHqdgaiK574DuHAZDZD')
    json2 = h.json()
    fb=Feedback.objects.all()
    Signupform=signupform()
    return render(request,"index1.html",{"json":json, "json2":json2, 'signupform':Signupform, "fb":fb})
       
    

 
   
    
