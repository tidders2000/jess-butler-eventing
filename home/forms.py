from django import forms
from .models import sign

class signupform(forms.ModelForm):
    class Meta:
         model = sign
         fields = ('name','email')