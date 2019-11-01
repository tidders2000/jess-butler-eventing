from django import forms
from .models import signup

class signupform(forms.ModelForm):
    class Meta:
         model = signup
         fields = ('name','email')