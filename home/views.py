from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from django.contrib import messages
from feedback.models import Feedback
import json
import requests
from .models import sign
from .forms import signupform






def index(request):
    
    r = requests.get('https://graph.facebook.com/v4.0/me?fields=id%2Cname%2Cfeed&access_token=EAAFwJhMIpkUBAB7RVKxV9UzCliSIGN8pBcxcfiTzByHu7o0yui9lJWmrNfnvdoKd0v5hQ6v8ZB2QTiZCr7yOETobw9f6rd5icrhuzOue2PStqyfk0V7ZCcUYHMaisdPslWs3lZB5ZAI68DdVt4fvG9k5y4keN0PY0F5X4YwYS6gZDZD')
    json = r.json()
    
    h = requests.get('https://graph.facebook.com/v5.0/230231543752378?fields=feed.limit(9)%7Bmessage%2Cpermalink_url%2Cfull_picture%7D&access_token=EAAFwJhMIpkUBAB7RVKxV9UzCliSIGN8pBcxcfiTzByHu7o0yui9lJWmrNfnvdoKd0v5hQ6v8ZB2QTiZCr7yOETobw9f6rd5icrhuzOue2PStqyfk0V7ZCcUYHMaisdPslWs3lZB5ZAI68DdVt4fvG9k5y4keN0PY0F5X4YwYS6gZDZD')
    json2 = h.json()
    fb=Feedback.objects.all()
    Signupform=signupform()
    if request.method=='POST':
    
        signup = signupform(request.POST)
        if signup.is_valid():
         signup.save(commit=True)
         signup.save
         messages.error(request, 'email added')
        return redirect(reverse('index'))
    return render(request,"index.html",{ 'signupform':Signupform, "json":json, "json2":json2,"fb":fb})
       
    

 
   
    
