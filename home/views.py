from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from django.contrib import messages
from feedback.models import Feedback
import json
import requests
from .models import sign
from .forms import signupform

from django.conf import settings


def index(request):

    fb_access = settings.FB_ACCESS

    r = requests.get(
        'https://graph.facebook.com/v4.0/me?fields=id%2Cname%2Cfeed&access_token='+fb_access)
    json = r.json()
    api_key = settings.API_KEY
    h = requests.get(
        'https://graph.facebook.com/v5.0/230231543752378?fields=feed.limit(9)%7Bmessage%2Cpermalink_url%2Cfull_picture%7D&access_token='+fb_access)
    json2 = h.json()
    fb = Feedback.objects.all()
    Signupform = signupform()
    if request.method == 'POST':

        signup = signupform(request.POST)
        if signup.is_valid():
            signup.save(commit=True)
            signup.save
            messages.error(request, 'email added')
        return redirect(reverse('index'))
    return render(request, "index.html", {"api_key": api_key, "json": json, "json2": json2, 'signupform': Signupform, "fb": fb})
