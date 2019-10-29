from django.shortcuts import render, redirect, reverse, HttpResponseRedirect

import json
import requests




def index(request):
    return render(request,'index.html')

def index1(request):
    
    r = requests.get('https://graph.facebook.com/v4.0/me?fields=id%2Cname%2Cfeed&access_token=EAAFwJhMIpkUBAJZCGoIvHYcqeprUqWGEasJ2pPCjageosx35is5ZAH1gn4xnBhFoKqV6NzAhXn25xvIhYIXkTjODCeKy9FlQSGQX496ZAQ7MuN8FgWLNlTXh1vYBeyE0OtofnxKy80UMBay6aZCqkUCVZAlca1KE5hGaoaZA5q6pcJReZC6bL0eDzHPZCtPNf6ZBRrMmnTYvAxAZDZD')
    json = r.json()
    
    h = requests.get('https://graph.facebook.com/v4.0/me?fields=name%2Cfeed.limit(9)%7Bfull_picture%2Cmessage%2Clink%7D&access_token=EAAFwJhMIpkUBACt4KPaeRa03hc3LNMrhWjIAesibZA2LeKuZCnsm9u6ezo8UbXDlMOODW2QOS9ZBzpJjHobM7IxDarRgIE0lEL3MI7ZBSfnPU64gxTfb0hV2VB2RgZB2wmAxpnag6M1ju2K3RjSAZAY3qFvtsZBBQUZC0nEV85VsWwZDZD')
    json2 = h.json()
    return render(request,"index1.html",{"json":json, "json2":json2})
       
    

 
   
    
