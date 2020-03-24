from django import forms
from django.forms import ModelForm
from .models import *

class ContactForm(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Review
        fields = ['firstname','lastname','email','phone','message']