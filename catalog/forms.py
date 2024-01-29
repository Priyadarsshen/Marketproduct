from django.db import models  
from django.forms import fields  
from .models import * 
from django import forms  
  
  
class UserImage(forms.ModelForm):  
    class Meta:   
        model = Products   
        fields = '__all__'